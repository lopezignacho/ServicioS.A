from django.db.models.expressions import Value
from systemvales.settings import DEBUG
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.shortcuts import get_object_or_404
from app.models import Perfil, Cargo, Turno

# Create your models here.

#Manager de Usuario nuevo
class UsuarioManager(BaseUserManager):
    #métodoo para crear usuario
    def create_user(self, email, rut_sin_dv, dv, nombre, apellido_p, apellido_m, id_perfil_usuario, id_cargo_usuario, id_turno_usuario, password=None):
        #validamos que se ingresen los datos
        if not email:
            raise ValueError("Los usuarios deben tener un email")
        if not rut_sin_dv:
            raise ValueError("Los usuarios deben tener un rut")
        if not dv:
            raise ValueError("Los usuarios deben tener un dígito verificador")
        if not nombre:
            raise ValueError("Los usuarios deben tener un nombre")
        if not apellido_p:
            raise ValueError("Los usuarios deben tener un apellido paterno")
        if not apellido_m:
            raise ValueError("Los usuarios deben tener un apellido materno")
        if not id_perfil_usuario:
            raise ValueError("Los usuarios deben tener un tipo de perfil")
        if not id_cargo_usuario:
            raise ValueError("Los usuarios deben tener un tipo de cargo")
        if not id_turno_usuario:
            raise ValueError("Los usuarios deben tener un turno")

        #definimos el usuario con sus datos
        usuario = self.model(
            email = self.normalize_email(email),
            rut_sin_dv = rut_sin_dv,
            dv = dv,
            nombre = nombre,
            apellido_p = apellido_p,
            apellido_m = apellido_m,
            id_perfil_usuario = id_perfil_usuario,
            id_cargo_usuario = id_cargo_usuario,
            id_turno_usuario = id_turno_usuario
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    #método para crear súper usuario
    def create_superuser(self, email, rut_sin_dv, dv, nombre, apellido_p, apellido_m, id_perfil_usuario, id_cargo_usuario, id_turno_usuario, password):
        #definimos el usuario con sus datos        
        turno_instance = get_object_or_404(Turno, pk=id_turno_usuario)                
        cargo_instance = get_object_or_404(Cargo, pk=id_cargo_usuario)
        perfil_instance = get_object_or_404(Perfil, pk=id_perfil_usuario)
        usuario = self.create_user(
            email = self.normalize_email(email),
            rut_sin_dv = rut_sin_dv,
            dv = dv,
            nombre = nombre,
            apellido_p = apellido_p,
            apellido_m = apellido_m,
            id_perfil_usuario = perfil_instance,
            id_cargo_usuario = cargo_instance,
            id_turno_usuario = turno_instance,
            password = password
        )
        usuario.is_admin = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario
        

#Modelo de Usuario nuevo
class Cuenta(AbstractBaseUser):
    #Requeridos
    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    date_joined         = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    #añadidos
    rut_sin_dv          = models.IntegerField(unique=True)
    dv                  = models.CharField(max_length=1)
    nombre              = models.CharField(max_length=20)
    apellido_p          = models.CharField(max_length=20)
    apellido_m          = models.CharField(max_length=20)
    #Foreign Keys
    id_perfil_usuario   = models.ForeignKey('app.Perfil', models.DO_NOTHING, db_column='id_perfil') 
    id_cargo_usuario    = models.ForeignKey('app.Cargo', models.DO_NOTHING, db_column='id_cargo')
    id_turno_usuario    = models.ForeignKey('app.Turno', models.DO_NOTHING, db_column='id_turno')

    #Variable usada para logearse
    USERNAME_FIELD       = 'rut_sin_dv'
    #Campo usado para definir los campos obligatorios
    REQUIRED_FIELDS      = ['email', 'dv', 'nombre', 'apellido_p', 'apellido_m', 'id_perfil_usuario',\
         'id_cargo_usuario', 'id_turno_usuario']

    #aquí le decimos dónde está el manager
    objects = UsuarioManager()

    def __str__(self):
        string=str(self.rut_sin_dv)+"-"+str(self.dv)
        return string

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

#nos vamos a settings a declarar el usuario