# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'cargo'


class DetalleVale(models.Model):
    cantidad = models.IntegerField()
    vale_id_vale = models.OneToOneField('Vale', models.DO_NOTHING, db_column='vale_id_vale', primary_key=True)
    servicio_id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_id_servicio')

    class Meta:
        managed = False
        db_table = 'detalle_vale'
        unique_together = (('vale_id_vale', 'servicio_id_servicio'),)


class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    perfil_id_perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_id_perfil')
    cargo_id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='cargo_id_cargo')
    turno_id_turno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='turno_id_turno')
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido_p = models.CharField(max_length=2)
    apellido_m = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    rut_sin_dv = models.IntegerField()
    dv = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'empleado'


class Perfil(models.Model):
    id_perfil = models.BooleanField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'perfil'


class Servicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'servicio'


class Sucursal(models.Model):
    id_sucursal = models.BooleanField(primary_key=True)
    direccion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Turno(models.Model):
    id_turno = models.BooleanField(primary_key=True)
    hora_ini = models.DateField()
    hora_ter = models.DateField()

    class Meta:
        managed = False
        db_table = 'turno'


class Vale(models.Model):
    id_vale = models.IntegerField(primary_key=True)
    sucursal_id_sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='sucursal_id_sucursal')
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')
    valor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vale'


class Venta(models.Model):
    n_venta = models.IntegerField(primary_key=True)
    vale_id_vale = models.ForeignKey(Vale, models.DO_NOTHING, db_column='vale_id_vale')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'venta'