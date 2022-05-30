# Generated by Django 2.2.1 on 2022-04-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220425_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='email'),
        ),
    ]