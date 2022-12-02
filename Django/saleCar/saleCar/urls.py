from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cars.views import CarViewSet, ColorViewSet

router = routers.DefaultRouter()
router.register('car', CarViewSet, basename='Car')
router.register('color', ColorViewSet, basename='Color')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
