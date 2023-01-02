from django.shortcuts import render
from django.http import HttpResponse
from AppMarket.models import Producto, Vendedor, Categoria
from django.core import serializers
from AppMarket.forms import ProductoFormulario, VendedorFormulario, CategoriaFormulario

# Create your views here.
def inicio(request):
    return render(request, 'AppMarket/inicio.html')

def producto(request):
    return render(request, 'AppMarket/producto.html')

def vendedor(request):
    return render(request, 'AppMarket/vendedor.html')

def categoria(request):
    return render(request, 'AppMarket/categoria.html')

def productoapi(request):
    produc=Producto.objects.all()
    return HttpResponse (serializers.serialize('json',produc))

def vendedorapi(request):
    vendedores=Vendedor.objects.all()
    return HttpResponse (serializers.serialize('json',vendedores))

def categoriaapi (request):
    categoria_todos=Categoria.objects.all()
    return HttpResponse (serializers.serialize('json',categoria_todos))

def producto(request): 
    if request.method == "POST":
            miFormulario = ProductoFormulario(request.POST) 
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                productos = Producto(Titulo=informacion["Titulo"], Autor=informacion["Autor"], Precio=informacion["Precio"], Editorial=informacion["Editorial"])
                productos.save()
                return render(request, "AppMarket/inicio.html")
    else:
        miFormulario = ProductoFormulario()
    return render(request, "AppMarket/producto.html", {"miFormulario": miFormulario})

def vendedor(request): 
    if request.method == "POST":
            miFormulario = VendedorFormulario(request.POST) 
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                vendedor = Vendedor(Libreria=informacion["Libreria"], Email=informacion["Email"], Tel_libreria=informacion["Tel_libreria"], Ubicacion=informacion["Ubicacion"])
                vendedor.save()
                return render(request, "AppMarket/inicio.html")
    else:
        miFormulario = VendedorFormulario()
    return render(request, "AppMarket/vendedor.html", {"miFormulario": miFormulario})

def categoria(request): 
    if request.method == "POST":
            miFormulario = CategoriaFormulario(request.POST) 
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                categoria = Categoria(Genero=informacion["Genero"], Fecha_publicacion=informacion["Fecha_publicacion"], Tipo_contenido=informacion["Tipo_contenido"])
                categoria.save()
                return render(request, "AppMarket/inicio.html")
    else:
        miFormulario = CategoriaFormulario()
    return render(request, "AppMarket/categoria.html", {"miFormulario": miFormulario})

#Busqueda Producto
def buscarproducto(request):
    return render(request, 'AppMarket/buscarProducto.html')

def buscar (request):
    if request.GET['Titulo']:
        Titulo = request.GET['Titulo']
        produc= Producto.objects.filter(Titulo=Titulo)
        return render(request,'AppMarket/resultadoProducto.html',{"produc":produc,"Titulo":Titulo})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#Busqueda Vendedor: 
def buscarvendedor(request):
    return render(request,'AppMarket/buscarVendedor.html')

def buscarv (request):
    if request.GET['Ubicacion']:
        Ubicacion = request.GET['Ubicacion']
        vende = Vendedor.objects.filter(Ubicacion=Ubicacion)
        return render(request,'AppMarket/resultadoVendedor.html',{"vende":vende,"Ubicacion":Ubicacion})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#BusquedaCategoria
def buscarcategoria(request):
    return render(request, 'AppMarket/buscarCategoria.html')

def buscarc (request):
    if request.GET['Tipo_contenido']:
        Tipo_contenido = request.GET['Tipo_contenido']
        categ = Categoria.objects.filter(Tipo_contenido=Tipo_contenido)
        return render(request,'AppMarket/resultadoCategoria.html',{"categ":categ,"Tipo_contenido":Tipo_contenido})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#CRUD
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

#CRUD Producto
class ProductoList(ListView):
    model = Producto
    template = 'AppMarket/producto_list.html'

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    success_url = '/AppMarket/producto/list'

class ProductoEdit(UpdateView):
    model = Producto
    fields = '__all__'
    success_url = '/AppMarket/producto/list'

class ProductoDetail(DetailView):
    model = Producto
    template = 'AppMarket/producto_detail.html'

class ProductoDelete(DeleteView):
    model = Producto
    #fields = '__all__'
    success_url = '/AppMarket/producto/list'

#CRUD Vendedor
class VendedorList(ListView):
    model = Vendedor
    template = 'AppMarket/vendedor_list.html'

class VendedorCreate(CreateView):
    model = Vendedor
    fields = '__all__'
    success_url = '/AppMarket/vendedor/list'

class VendedorEdit(UpdateView):
    model = Vendedor
    fields = '__all__'
    success_url = '/AppMarket/vendedor/list'

class VendedorDetail(DetailView):
    model = Vendedor
    template = 'AppMarket/vendedor_detail.html'

class VendedorDelete(DeleteView):
    model = Vendedor
    #fields = '__all__'
    success_url = '/AppMarket/vendedor/list'

#CRUD Categoria
class CategoriaList(ListView):
    model = Categoria
    template = 'AppMarket/categoria_list.html'

class CategoriaCreate(CreateView):
    model = Categoria
    fields = '__all__'
    success_url = '/AppMarket/categoria/list'

class CategoriaEdit(UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = '/AppMarket/categoria/list'

class CategoriaDetail(DetailView):
    model = Categoria
    template = 'AppMarket/categoria_detail.html'

class CategoriaDelete(DeleteView):
    model = Categoria
    #fields = '__all__'
    success_url = '/AppMarket/categoria/list'    
