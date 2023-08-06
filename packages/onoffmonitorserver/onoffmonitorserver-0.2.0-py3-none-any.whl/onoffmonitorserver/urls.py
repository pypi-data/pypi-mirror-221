from rest_framework.routers import DefaultRouter

from .views import MonitorViewSet, DeviceViewSet, StatusViewSet

router = DefaultRouter()
router.register('monitor', MonitorViewSet)
router.register('device', DeviceViewSet)
router.register('status', StatusViewSet)

urlpatterns = router.urls
