from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


def phone_number(phone):
    if not isinstance(phone, str) or len(phone) != 10:
        raise serializers.ValidationError(_('Wrong phone number'))

    return phone


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[phone_number])
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user
