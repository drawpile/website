from rest_framework import serializers

class AuthAttemptSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=22)
    password = serializers.CharField(max_length=512)
    group = serializers.CharField(max_length=64, required=False)
    avatar = serializers.BooleanField(required=False, default=False)
    nonce = serializers.RegexField(r'^[0-9a-fA-F]{1,16}$')

class AccountQuerySerializer(serializers.Serializer):
    username = serializers.CharField(max_length=22)
    group = serializers.CharField(max_length=64, required=False)

