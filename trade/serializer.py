from rest_framework import serializers


from .models import Card

class CardSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_name','card_price','info','duration']