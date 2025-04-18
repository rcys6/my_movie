from django.shortcuts import render
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

from .models import Card,Order
from .serializer import CardSerialzer
from .permision import IsAdminUserOrReadOnly
from utils.error import TradeError,response_data
from utils.common import get_random_code
from account.models import Profile
from utils.zhifubao import AliPay


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerialzer
    permission_classes = [IsAdminUserOrReadOnly] # 权限类


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