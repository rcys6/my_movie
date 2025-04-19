from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from django.db import transaction

from rest_framework.permissions import IsAuthenticated,SAFE_METHODS
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta

from .models import Card,Order
from .serializer import CardSerialzer,OrderSerialzer
from .permision import IsAdminUserOrReadOnly
from utils.error import TradeError,response_data
from utils.common import get_random_code
from utils.filters import OrderFilter
from account.models import Profile
from utils.zhifubao import AliPay


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerialzer
    permission_classes = [IsAdminUserOrReadOnly] # 权限类

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerialzer
    filterset_class = OrderFilter

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated() ]
        return [IsAdminUserOrReadOnly()]



class AlipayAPIView(APIView):
    def get(self,request):
        card_id = request.GET.get('card_id',None)
        print(card_id)
        try:
            card = Card.objects.get(pk=card_id)
        except:
            return Response(response_data(*TradeError.CardParamError))

        out_trade_no = "pay" + datetime.now().strftime("%Y%m%d%H%M%S") + get_random_code(4)

        try:
            # 创建订单
            uid = 'WdyuEUqDrAVAH63yPUSHY6'
            Order.objects.create(
                # user = Profile.objects.get(uid=request.user), 
                user = Profile.objects.get(pk=uid), 
                order_sn = out_trade_no,
                order_mount = card.card_price,
                card = card,
                pay_time = timezone.now()
            )
            
        except:
            return Response(response_data(*TradeError.OrderCreateError))
            
        #调用支付宝
        try:
            alipay = AliPay()
            pay_url = alipay.trade_page(out_trade_no, str(card.card_price), card.card_name, "支付宝支付", "FAST_INSTANT_TRADE_PAY")
            return Response(pay_url)
        
        except:
            return Response(response_data(*TradeError.PayRequestError))
        

class AlipayCallbackAPIView(APIView):
    def post(self, request):
        params =request.POST.dict()
        print(params)

        # 去除sign 和sign_type
        sign=params.pop('sign')
        sign_type = params.pop('sign_type')

        # 排序
        sorted_list = sorted([(k,v) for k,v in params.items()])
        unsigned_string = '&'.join(f'{k}={v}' for k,v in sorted_list)

        alipay=AliPay()
        if not alipay.verify(unsigned_string,sign):
            print('verify sign error')  
            return Response('Error')
        try:
            order = Order.objects.get(order_sn=params.get('out_trade_no'))
        except:
            return Response('Error')
        
        if params.get('total_amount') != str(order.order_mount):
            return Response('Error')

        if params.get('seller_id') != settings.ALIPAY_SELLER_ID:
            return Response('Error')
        
        if params.get('app_id') != settings.ALIPAY_APP_ID:
            return Response('Error')

        if params.get('trade_status') not in ['TRADE_SUCCESS','TRADE_FINISHED']:
            return Response('Error')
        print('全部验证通过')

        # 事务同步
        with transaction.atomic():
            order.trade_no = params.get('trade_no')
            order.pay_status = params.get('trade_status')
            order.pay_time = timezone.now()
            order.save()
        
            uid = 'WdyuEUqDrAVAH63yPUSHY6'
            # 改profile表
           
            # profile = Profile.objects.get(uid=order.profile.uid)
            profile = Profile.objects.get(uid=uid)
            profile.is_upgrade = 1
            profile.upgrade_time = timezone.now()
            profile.upgrade_count +=1

            # 如果会员未过期，在原来时间基础上再加会员卡时长
            if not profile.expire_time or profile.expire_time < timezone.now():
                profile.expire_time = timezone.now() + timedelta(days=order.card.duration)
            else:
                profile.expire_time = profile.expire_time + timedelta(days=order.card.duration)
            profile.save()
            
        return Response('success')