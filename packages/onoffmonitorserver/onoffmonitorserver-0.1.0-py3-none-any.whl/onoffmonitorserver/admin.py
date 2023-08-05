from django.contrib import admin
from . import models

admin.site.register((
    models.Monitor,
    models.Device,
    models.Status
))
