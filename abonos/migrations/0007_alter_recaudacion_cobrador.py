# Generated by Django 4.0.1 on 2022-01-21 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abonos', '0006_alter_abono_cliente_alter_abono_cobrador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recaudacion',
            name='cobrador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='abonos.cobrador'),
        ),
    ]