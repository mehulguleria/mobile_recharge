from rest_framework import serializers
from datetime import datetime

class rechargeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.CharField()
    title = serializers.CharField()
    detail = serializers.CharField()

class historySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    phone = serializers.IntegerField()
    title = serializers.CharField()
    ammount = serializers.IntegerField()
    detail = serializers.CharField()
    recharge_date = serializers.DateTimeField()