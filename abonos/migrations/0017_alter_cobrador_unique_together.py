# Generated by Django 4.0.1 on 2022-02-19 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abonos', '0016_concepto_alter_abono_concepto'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cobrador',
            unique_together={('nombre',)},
        ),
    ]
