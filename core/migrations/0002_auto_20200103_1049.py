# Generated by Django 3.0.2 on 2020-01-03 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='dono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pessoa'),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='modelo',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
