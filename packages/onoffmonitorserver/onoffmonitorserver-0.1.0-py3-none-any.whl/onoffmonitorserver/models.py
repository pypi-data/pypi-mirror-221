"""
Model classes to represent database tables
"""
from django.conf import settings
from django.db import models
from django.utils import timezone


class Monitor(models.Model):
    """
    Model for storing data about a monitor (such as "garage")
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.user})'


class Device(models.Model):
    """
    Model for storing data about a device (such as "boiler")
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    gpio_pin = models.PositiveSmallIntegerField(
        verbose_name='GPIO pin on monitor')

    def __str__(self):
        return f'{self.name} ({self.user})'


class Status(models.Model):
    """
    Model for storing the status of a device (on or off) at a given time
    """
    STATUS_CHOICES = (
        (0, 'Off'),
        (1, 'On'),
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=0)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.device} {self.STATUS_CHOICES[int(self.status)][1]}'

    class Meta:
        """Metadata form Status Model"""
        verbose_name_plural = 'Statuses'
