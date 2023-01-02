from django.db import models

# Create your models here.
class Producto(models.Model):
    Titulo=models.CharField (max_length=200)
    Autor=models.CharField (max_length=200)
    Precio=models.FloatField()
    Editorial=models.CharField (max_length=100)

class Vendedor(models.Model):
    Libreria=models.CharField (max_length=100)
    Email=models.EmailField(max_length=100)
    Tel_libreria=models.IntegerField(40)
    Ubicacion=models.CharField (max_length=200)

class Categoria(models.Model):
    Genero=models.CharField (max_length=50)
    Anio_publicacoin=models.IntegerField()
    Tipo_contenido=models.CharField (max_length=100)