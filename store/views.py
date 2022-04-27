from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from .carrito import Carrito
# Create your views here.

def home(request):
    return render(request, 'store/index.html')

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'store/collections.html', context)


def collectionsview(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category':category}
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products': products}
        else:
            messages.error(request, "Producto no encontrado")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    
    return render(request, 'store/products/view.html', context)

"""
# ------------------------------------------ #
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('productview')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('productview')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('productview')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('productview')
# ------------------------------------------ #
"""