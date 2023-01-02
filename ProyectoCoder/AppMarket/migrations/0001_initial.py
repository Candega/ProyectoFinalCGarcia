# Generated by Django 4.1.3 on 2023-01-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genero', models.CharField(max_length=50)),
                ('Fecha_publicacion', models.DateField()),
                ('Tipo_contenido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('Autor', models.CharField(max_length=200)),
                ('Precio', models.FloatField()),
                ('Editorial', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Libreria', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Tel_libreria', models.IntegerField(verbose_name=40)),
                ('Ubicacion', models.CharField(max_length=200)),
            ],
        ),
    ]
