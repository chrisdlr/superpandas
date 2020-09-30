# Generated by Django 3.0.7 on 2020-09-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0002_auto_20200924_0349'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodegaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('csd_cvz', models.CharField(default=0, max_length=200)),
                ('cet', models.CharField(default=0, max_length=200)),
                ('nombre_cet', models.CharField(default=0, max_length=200)),
                ('frec', models.CharField(default=0, max_length=200)),
                ('ofvta', models.CharField(default=0, max_length=200)),
                ('oficina_ventas', models.CharField(default=0, max_length=200)),
                ('material', models.CharField(default=0, max_length=200)),
                ('codigo', models.CharField(default=0, max_length=200)),
                ('serie', models.CharField(default=0, max_length=200)),
                ('fuente', models.CharField(default=0, max_length=200)),
                ('pais', models.CharField(default=0, max_length=200)),
                ('cliente', models.CharField(default=0, max_length=200)),
                ('nombre', models.CharField(default=0, max_length=200)),
                ('direccion', models.CharField(default=0, max_length=200)),
                ('distrito', models.CharField(default=0, max_length=200)),
                ('distrito2', models.CharField(default=0, max_length=200)),
                ('activo', models.CharField(default=0, max_length=200)),
                ('tamaño', models.CharField(default=0, max_length=200)),
                ('imagen', models.CharField(default=0, max_length=200)),
                ('año', models.CharField(default=0, max_length=200)),
                ('fecha_ingreso_taller', models.CharField(default=0, max_length=200)),
                ('propiedad', models.CharField(default=0, max_length=200)),
            ],
            options={
                'verbose_name': 'BodegaModel',
                'verbose_name_plural': 'BodegaModels',
                'ordering': ['codigo'],
            },
        ),
    ]