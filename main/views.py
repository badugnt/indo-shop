from django.shortcuts import get_object_or_404, redirect, render
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()
    context = {
        
        'nama_toko': 'Indo Shop',
        'npm' : '2406410494',
        'name': 'Edlyn Marva',
        'class': 'PBP A',
        'product_list': product_list,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
     product_list = Product.objects.all()
     json_data = serializers.serialize("json", product_list)
     return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, news_id):
    try:
        product_list = Product.objects.filter(pk=news_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, news_id):
    try:
     product_list = Product.objects.filter(pk=news_id)
     json_data = serializers.serialize("json", product_list)
     return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)