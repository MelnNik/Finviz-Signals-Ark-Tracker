from rest_framework import serializers
from .models import Trade

class TradeSerializer(serializers.ModelSerializer):
  time = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
  class Meta:
    model = Trade
    fields = '__all__'
