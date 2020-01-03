# Generated by Django 3.0.2 on 2020-01-03 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_mensalista'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimentosMensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataPagamento', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('mensalista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.mensalista')),
            ],
        ),
    ]