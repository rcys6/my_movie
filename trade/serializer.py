from rest_framework import serializers


from .models import Card,Order

class CardSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_name','card_price','info','duration']


class OrderSerialzer(serializers.ModelSerializer):
    card= CardSerialzer()
    class Meta:
        model = Order
        fields = ['order_sn','pay_status','order_mount','created_at','card']