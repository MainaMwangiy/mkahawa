from rest_framework import viewsets
from menu.models import Menu
from menu.serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    
    queryset = Menu.objects.all()

    def get_queryset(self):
        return Menu.objects.all()