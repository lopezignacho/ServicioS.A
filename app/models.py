# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Borrar
class Usuario(models.Model):
    username = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.CharField(max_length=254)
    clave = models.CharField(max_length=16)

    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cargo'

    def __str__(self):
        return self.nombre


class DetalleVale(models.Model):
    cantidad = models.IntegerField()
    id_vale_detalle = models.OneToOneField('Vale', models.DO_NOTHING, db_column='id_vale_detalle', primary_key=True)
    id_servicio_detalle = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio_detalle')

    class Meta:
        managed = False
        db_table = 'detalle_vale'
        unique_together = (('id_vale_detalle', 'id_servicio_detalle'),)

    def __str__(self):
        return self.id_vale_detalle + '-' + self.id_servicio_detalle

class Perfil(models.Model):
    id_perfil = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'perfil'
    
    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'servicio'

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'sucursal'

    def __str__(self):
        return self.direccion


class Turno(models.Model):
    id_turno = models.IntegerField(primary_key=True)
    hora_ini = models.DateField()
    hora_ter = models.DateField()

    class Meta:
        managed = False
        db_table = 'turno'

    def __str__(self):
        string=str(self.id_turno)
        return string


class Vale(models.Model):
    id_vale = models.IntegerField(primary_key=True)
    id_sucursal_vale = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='id_sucursal_vale')
    id_empleado_vale = models.IntegerField()
    valor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vale'

    def __str__(self):
        return self.id_vale


class Venta(models.Model):
    n_venta = models.IntegerField(primary_key=True)
    id_vale_venta = models.ForeignKey(Vale, models.DO_NOTHING, db_column='id_vale_venta')
    fecha = models.DateField()
    subtotal = models.IntegerField()
    iva = models.IntegerField()
    detalles = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'

    def __str__(self):
        return self.n_venta