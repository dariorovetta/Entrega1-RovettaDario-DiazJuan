# Generated by Django 4.1.1 on 2022-10-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appMVT', '0002_delete_familiar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fechaNacimiento', models.DateField(null=True)),
            ],
        ),
    ]
