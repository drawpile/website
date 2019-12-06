from rest_framework import serializers

from dpauth.models import Username, avatar_validator
from dpauth.settings import extauth_settings

class UsernameSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(allow_null=True, required=False, validators=[avatar_validator])
    is_primary = serializers.BooleanField(default=False)

    class Meta:
        model = Username
        fields = ('name', 'is_mod', 'avatar', 'is_primary')

    def validate_name(self, value):
        if Username.exists(value, self.instance.pk if self.instance else None):
            raise serializers.ValidationError("This username is already in use.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user

        if Username.objects.filter(user=user).count() >= extauth_settings['ALT_COUNT']:
            raise serializers.ValidationError("Max username count reached")

        is_primary = validated_data.pop('is_primary', False)
        obj = Username.objects.create(
            user=user,
            **validated_data
        )

        if is_primary:
            obj.make_primary()
        return obj
    
    def update(self, instance, validated_data):
        is_primary = validated_data.pop('is_primary', False)
        super().update(instance, validated_data)
        if is_primary:
            instance.make_primary()
        return instance
