from .models import producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
  queryset = producto.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = ProductoSerializer