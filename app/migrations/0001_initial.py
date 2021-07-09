# Generated by Django 3.2.3 on 2021-07-06 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_cargo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id_perfil', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'perfil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_turno', models.IntegerField(primary_key=True, serialize=False)),
                ('hora_ini', models.DateField()),
                ('hora_ter', models.DateField()),
            ],
            options={
                'db_table': 'turno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vale',
            fields=[
                ('id_vale', models.IntegerField(primary_key=True, serialize=False)),
                ('id_empleado_vale', models.IntegerField()),
                ('valor', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vale',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('n_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('subtotal', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('detalles', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=254)),
                ('clave', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVale',
            fields=[
                ('cantidad', models.IntegerField()),
                ('id_vale_detalle', models.OneToOneField(db_column='id_vale_detalle', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.vale')),
            ],
            options={
                'db_table': 'detalle_vale',
                'managed': False,
            },
        ),
    ]
