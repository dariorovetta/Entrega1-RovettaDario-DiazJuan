# Generated by Django 4.1.2 on 2022-10-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_extensionusuario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensionusuario',
            name='descripcion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='extensionusuario',
            name='red_social',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
