from django.shortcuts import render, redirect
from django.urls import reverse
from .models import marca, categoria, proveedor, producto, cargo, empleado
import requests

from django.conf import settings
from django.http import JsonResponse
from transbank.webpay.webpay_plus.transaction import (
    Transaction,
    WebpayOptions,
    IntegrationCommerceCodes,
    IntegrationApiKeys,
)
from transbank.common.integration_type import IntegrationType

# Create your views here.


def index(request):
    return render(request, "core/index.html")


def Nosotros(request):
    return render(request, "core/Nosotros.html")


def Contacto(request):
    return render(request, "core/Contacto.html")


def Login(request):
    return render(request, "core/Login.html")


def registro(request):
    return render(request, "core/registro.html")


def crud_cuentas(request):
    if request.method != "POST":
        carg = cargo.objects.all()

        context = {
            "cargo": carg,
        }
        return render(request, "core/crud_cuentas.html", context)
    else:
        p_nombre_empleado = request.POST["txtPrimer_nombre_Empleado"]
        s_nombre_empleado = request.POST["txtSegundo_nombre_Empleado"]
        p_apellido_empleado = request.POST["txtPrimer_Apellido"]
        s_apellido_empleado = request.POST["txtSegundo_Apellido"]
        direccion_empleado = request.POST["txtDireccion"]
        edad_empleado = request.POST["txtEdad"]
        id_cargo = request.POST["cargo"]

        objCargo = cargo.objects.get(idCargo=id_cargo)

        emp = empleado.objects.create(
            pNombreEmpleado=p_nombre_empleado,
            sNombreEmpleado=s_nombre_empleado,
            pApellidoEmpleado=p_apellido_empleado,
            sApellidoEmpleado=s_apellido_empleado,
            direccionEmpleado=direccion_empleado,
            edad=edad_empleado,
            cargo=objCargo,
        )
        emp.save()

        context = {"mensaje": "Exito"}
        return render(request, "core/resultado.html", context)


def crud_productos(request):
    if request.method != "POST":
        mar = marca.objects.all()
        cat = categoria.objects.all()
        pro = proveedor.objects.all()

        context = {
            "marca": mar,
            "categoria": cat,
            "proveedor": pro,
        }
        return render(request, "core/crud_productos.html", context)

    else:
        nombre_producto = request.POST["txtNombre_Producto"]
        sotck_producto = request.POST["txtstock_Producto"]
        descripcion_producto = request.POST["txtdescripcion_Producto"]
        precio_producto = request.POST["txtPrecio_Producto"]
        imagen_producto = request.FILES["imagen_producto"]
        id_marca = request.POST["marca"]
        id_categoria = request.POST["categoria"]
        id_proveedor = request.POST["proveedor"]

        objMarca = marca.objects.get(idMarca=id_marca)
        objCategoria = categoria.objects.get(idCategoria=id_categoria)
        objProveedor = proveedor.objects.get(idProveedor=id_proveedor)

        cli = producto.objects.create(
            nombreProducto=nombre_producto,
            stockProducto=sotck_producto,
            descripcionProducto=descripcion_producto,
            precioProducto=precio_producto,
            imagenProducto=imagen_producto,
            categoria=objCategoria,
            marca=objMarca,
            proveedor=objProveedor,
        )
        cli.save()

        context = {"mensaje": "Exito"}
        return render(request, "core/resultado.html", context)


def resultado(request):
    context = {}
    return render(request, "core/resultado.html", context)


def pedido(request):
    context = {}
    return render(request, "core/pedido.html", context)


def pago(request):
    buy_order = request.POST["ordenCompra"]
    session_id = request.POST["idSesion"]
    amount = request.POST["monto"]
    return_url = "http://127.0.0.1:8000/retorno_pago"

    transaction = Transaction(
        WebpayOptions(
            IntegrationCommerceCodes.WEBPAY_PLUS,
            IntegrationApiKeys.WEBPAY,
            IntegrationType.TEST,
        )
    )

    response = transaction.create(buy_order, session_id, amount, return_url)
    token = response["token"]
    url = response["url"]

    return render(request, "core/pago.html", {"url": url, "token": token})


def retorno_pago(request):
    token = request.GET.get("token_ws")

    transaction = Transaction(
        WebpayOptions(
            IntegrationCommerceCodes.WEBPAY_PLUS,
            IntegrationApiKeys.WEBPAY,
            IntegrationType.TEST,
        )
    )

    response = transaction.commit(token)

    status = response["status"]
    amount = response["amount"]
    buy_order = response["buy_order"]

    context = {
        "status": status,
        "amount": amount,
        "buy_order": buy_order,
    }

    return render(request, "core/retorno_pago.html", context)


def productos(request):
    url = "http://localhost:8000/api/productos"

    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud a la API: {e}")
        datos = None

    context = {"productos": datos}

    return render(request, "core/productos.html", context)


def producto(request):
    return render(request, "core/productos.html")
