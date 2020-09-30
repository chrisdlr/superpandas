# Generated by Django 3.0.7 on 2020-09-28 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0005_bodegamodel_ruta'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('serie', models.CharField(default=0, max_length=200)),
                ('proveedor', models.CharField(default=0, max_length=200)),
                ('plan', models.CharField(default=0, max_length=200)),
                ('dias', models.CharField(default=0, max_length=200)),
                ('prioridad', models.CharField(default=0, max_length=200)),
                ('movimientos', models.CharField(default=0, max_length=200)),
                ('tipo_servicio', models.CharField(default=0, max_length=200)),
                ('fecha_recepcion', models.CharField(default=0, max_length=200)),
                ('codigo_cliente', models.CharField(default=0, max_length=200)),
                ('sala_ventas', models.CharField(default=0, max_length=200)),
                ('columna1', models.CharField(default=0, max_length=200)),
                ('mesa', models.CharField(default=0, max_length=200)),
                ('ruta', models.CharField(default=0, max_length=200)),
                ('nombre_cliente', models.CharField(default=0, max_length=200)),
                ('nombre_calle_direccion', models.CharField(default=0, max_length=200)),
                ('colonia_barrio_distrito', models.CharField(default=0, max_length=200)),
                ('departamento', models.CharField(default=0, max_length=200)),
                ('referencia', models.CharField(default=0, max_length=200)),
                ('dni_ruc', models.CharField(default=0, max_length=200)),
                ('contacto', models.CharField(default=0, max_length=200)),
                ('telefono', models.CharField(default=0, max_length=200)),
                ('horario_atencion', models.CharField(default=0, max_length=200)),
                ('modelo_ef', models.CharField(default=0, max_length=200)),
                ('logo', models.CharField(default=0, max_length=200)),
                ('tamaño', models.CharField(default=0, max_length=200)),
                ('activo', models.CharField(default=0, max_length=200)),
                ('status_validacion', models.CharField(default=0, max_length=200)),
                ('fecha_validacion', models.CharField(default=0, max_length=200)),
                ('motivo_rechazo', models.CharField(default=0, max_length=200)),
                ('explicacion_rechazo', models.CharField(default=0, max_length=200)),
                ('bonificacion', models.CharField(default=0, max_length=200)),
                ('proceso_ejecucion', models.CharField(default=0, max_length=200)),
                ('fecha_ejecucion', models.CharField(default=0, max_length=200)),
            ],
            options={
                'verbose_name': 'CloudModel',
                'verbose_name_plural': 'CloudModels',
                'ordering': ['id'],
            },
        ),
    ]
