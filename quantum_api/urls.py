from django.urls import path,include
from rest_framework import routers
from . import views
from .views import UploadViewSet


router = routers.DefaultRouter()
router.register(r'analyze', UploadViewSet, basename="analyze")
router.register(r'simulate', UploadViewSet, basename="simulate")

urlpatterns = [
    path('', include(router.urls)),
  ]