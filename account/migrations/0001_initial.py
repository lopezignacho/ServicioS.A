# Generated by Django 3.1.2 on 2021-07-03 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('rut_sin_dv', models.IntegerField(unique=True)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_p', models.CharField(max_length=20)),
                ('apellido_m', models.CharField(max_length=20)),
                ('id_cargo_usuario', models.ForeignKey(db_column='id_cargo', on_delete=django.db.models.deletion.DO_NOTHING, to='app.cargo')),
                ('id_perfil_usuario', models.ForeignKey(db_column='id_perfil', on_delete=django.db.models.deletion.DO_NOTHING, to='app.perfil')),
                ('id_turno_usuario', models.ForeignKey(db_column='id_turno', on_delete=django.db.models.deletion.DO_NOTHING, to='app.turno')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]