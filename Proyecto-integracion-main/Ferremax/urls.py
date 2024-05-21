from django.urls import path, include
from rest_framework import routers
from .api import ProductoViewSet

from .views import (
    index,
    Nosotros,
    Contacto,
    Login,
    registro,
    crud_cuentas,
    crud_productos,
    resultado,
    pedido,
    pago,
    retorno_pago,
    productos,
    producto,
)

router = routers.DefaultRouter()
router.register("api/productos", ProductoViewSet, "productos")

urlpatterns = [
    path("", index, name="index"),
    path("Nosotros", Nosotros, name="Nosotros"),
    path("Contacto", Contacto, name="Contacto"),
    path("Login", Login, name="Login"),
    path("registro", registro, name="registro"),
    path("crud_cuentas", crud_cuentas, name="crud_cuentas"),
    path("crud_productos", crud_productos, name="crud_productos"),
    path("resultado", resultado, name="resultado"),
    path("pedido", pedido, name="pedido"),
    path("pago", pago, name="pago"),
    path("retorno_pago", retorno_pago, name="retorno_pago"),
    path("productos", productos, name="productos"),
    path("", include(router.urls)),
    path("producto", producto, name="producto"),
]
