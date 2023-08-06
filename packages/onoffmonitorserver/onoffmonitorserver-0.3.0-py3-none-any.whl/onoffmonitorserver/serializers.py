from rest_framework.serializers import ModelSerializer, ValidationError, CurrentUserDefault, HiddenField

from . import models


class MonitorSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = models.Monitor
        fields = ['id', 'name', 'gpio_mode', 'user']


class DeviceSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    def validate(self, attrs):
        print(attrs)
        if attrs['monitor'].user != attrs['user']:
            raise ValidationError('Device owner must be the current user')
        return super().validate(attrs)

    class Meta:
        model = models.Device
        fields = ['id', 'name', 'user', 'monitor', 'gpio_input', 'gpio_led']


class StatusSerializer(ModelSerializer):
    user = CurrentUserDefault()

    def validate(self, attrs):
        if attrs['device'].user != self.user(self):
            raise ValidationError('Device owner must be the current user')
        return super().validate(attrs)

    class Meta:
        model = models.Status
        fields = ['id', 'device', 'status', 'time']
