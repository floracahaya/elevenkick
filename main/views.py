from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm   


# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'ElevenKick',
        'name': 'Flora Cahaya Putri',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# API: JSON semua produk
def products_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

# API: JSON by ID
def product_json_by_id(request, pk):
    product = get_object_or_404(Product, pk=pk)
    json_data = serializers.serialize("json", [product])  # serialize butir tunggal sebagai list
    return HttpResponse(json_data, content_type="application/json")

# API: XML semua produk
def products_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

# API: XML by ID
def product_xml_by_id(request, pk):
    product = get_object_or_404(Product, pk=pk)
    xml_data = serializers.serialize("xml", [product])
    return HttpResponse(xml_data, content_type="application/xml")

def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "product_list.html", context)

def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:product_list')
    else:
        form = ProductForm()
    return render(request, "product_add.html", {"form": form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "product_detail.html", context)