# Generated by Django 4.2.3 on 2023-08-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMR', '0002_vehiculo_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]