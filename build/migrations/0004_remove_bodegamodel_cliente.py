# Generated by Django 3.0.7 on 2020-09-26 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0003_bodegamodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodegamodel',
            name='cliente',
        ),
    ]
