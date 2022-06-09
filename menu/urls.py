from rest_framework.routers import DefaultRouter
from .viewsets import MenuViewSet
from django.urls import path, include

router = DefaultRouter()

router.register('menu', MenuViewSet)

urlpatterns = [
    path ('api/', include(router.urls))
]