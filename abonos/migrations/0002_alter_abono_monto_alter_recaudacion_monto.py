# Generated by Django 4.0 on 2022-01-13 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abono',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='recaudacion',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]