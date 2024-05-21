from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombreCategoria)


class marca(models.Model):
    idMarca = models.AutoField(primary_key=True)
    nombreMarca = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombreMarca)


class proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)
    nombreProveedor = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombreProveedor)


class cargo(models.Model):
    idCargo= models.AutoField(primary_key=True)
    nombreCargo = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombreCargo)


class producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=20, blank=False, null=False)
    stockProducto = models.IntegerField()
    descripcionProducto = models.CharField(max_length=100, blank=False, null=False)
    precioProducto = models.IntegerField()
    imagenProducto = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey("categoria", on_delete=models.CASCADE)
    marca = models.ForeignKey("marca", on_delete=models.CASCADE)
    proveedor = models.ForeignKey("proveedor", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreProducto)


class empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    pNombreEmpleado = models.CharField(max_length=20, blank=False, null=False)
    sNombreEmpleado = models.CharField(max_length=20, blank=False, null=False)
    pApellidoEmpleado = models.CharField(max_length=20, blank=False, null=False)
    sApellidoEmpleado = models.CharField(max_length=20, blank=False, null=False)
    direccionEmpleado = models.CharField(max_length=100, blank=False, null=False)
    edad = models.IntegerField()
    cargo = models.ForeignKey("cargo", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pNombreEmpleado)+" "+str(self.pApellidoEmpleado)