# Generated by Django 3.0.2 on 2020-01-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_movimentosmensalista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='modelo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='placa',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
