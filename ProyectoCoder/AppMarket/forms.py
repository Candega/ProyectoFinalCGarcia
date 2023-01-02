from django import forms

class ProductoFormulario(forms.Form):       
    Titulo=forms.CharField ()
    Autor=forms.CharField ()
    Precio=forms.FloatField()
    Editorial=forms.CharField ()

class VendedorFormulario(forms.Form):
    Libreria=forms.CharField ()
    Email=forms.EmailField()
    Tel_libreria=forms.IntegerField()
    Ubicacion=forms.CharField ()

class CategoriaFormulario(forms.Form):
    Genero=forms.CharField ()
    Fecha_publicacion=forms.DateField()
    Tipo_contenido=forms.CharField ()