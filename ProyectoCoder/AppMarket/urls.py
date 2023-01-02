from django.urls import path
from AppMarket import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('producto/', views.producto, name='Productos'),
    path('categoria/', views.categoria, name='Categoria'),
    path('vendedor/', views.vendedor, name='Vendedor'),
    path('productoApi/', views.productoapi),
    path('vendedorApi/', views.vendedorapi),
    path('categoriaApi/', views.categoriaapi),
    path('buscarProducto/', views.buscarproducto, name='Buscar Producto'),
    path('buscar/', views.buscar), 
    path('buscarVendedor/', views.buscarvendedor, name='Buscar Vendedor'),
    path('buscarv/', views.buscarv),
    path('buscarCategoria/', views.buscarcategoria, name='Buscar Categoria'),
    path('buscarc/', views.buscarc),
    path('producto/list/', views.ProductoList.as_view(), name='Producto List'),
    path('producto/create/', views.ProductoCreate.as_view(), name='Producto Create'),
    path('producto/edit/<pk>',views.ProductoEdit.as_view(), name='Producto Edit'),
    path('producto/detail/<pk>',views.ProductoDetail.as_view(), name='Producto Detail'),
    path('producto/delete/<pk>',views.ProductoDelete.as_view(), name='Producto Delete'),
    path('vendedor/list/', views.VendedorList.as_view(), name='Vendedor List'),
    path('vendedor/create/', views.VendedorCreate.as_view(), name='Vendedor Create'),
    path('vendedor/edit/<pk>',views.VendedorEdit.as_view(), name='Vendedor Edit'),
    path('vendedor/detail/<pk>',views.VendedorDetail.as_view(), name='Vendedor Detail'),
    path('vendedor/delete/<pk>',views.VendedorDelete.as_view(), name='Vendedor Delete'),
    path('categoria/list/', views.CategoriaList.as_view(), name='Categoria List'),
    path('categoria/create/', views.CategoriaCreate.as_view(), name='Categoria Create'),
    path('categoria/edit/<pk>',views.CategoriaEdit.as_view(), name='Categoria Edit'),
    path('categoria/detail/<pk>',views.CategoriaDetail.as_view(), name='Categoria Detail'),
    path('categoria/delete/<pk>',views.CategoriaDelete.as_view(), name='Categoria Delete'),
    


]