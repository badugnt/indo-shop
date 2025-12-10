from itertools import product
import json
from typing import Never
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
import requests
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    context = {
        
        'nama_toko': 'Indo Shop',
        'npm' : '2406410494',
        'name': request.user.username,
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'active_category': '' # Tambahkan default kosong
    }

    return render(request, "main.html", context)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return JsonResponse({'message': 'Produk berhasil ditambahkan!', 'id': str(product_entry.id)}, status=201)
        return JsonResponse({'error': form.errors}, status=400)
    else:
        # Untuk modal/form AJAX, jika perlu
        form = ProductForm()
        context = {'form': form}
        return render(request, "create_product.html", context)

@login_required(login_url='/login')
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
        filter_type = request.GET.get("filter", "all")
        category_filter = request.GET.get("category", "") # Ambil parameter category
        
        # 1. Base Query
        if filter_type == "all":
            product_list = Product.objects.all()
        else:
            product_list = Product.objects.filter(user=request.user)
            
        # 2. Apply Category Filter if exists
        if category_filter:
             product_list = product_list.filter(category=category_filter)

        data = [{
            'id': str(product.id)
            ,'name': product.name
            ,'price': product.price
            ,'category': product.category
            ,'description': product.description
            ,'user_id': product.user_id
            , 'thumbnail': product.thumbnail
            , 'is_featured': product.is_featured
            , 'rating': product.rating
        }
                for product in product_list]
        
        return JsonResponse(data, safe=False)

def show_json_asc(request):
    #  product_list = Product.objects.all()
    #  json_data = serializers.serialize("json", product_list)
    #  return HttpResponse(json_data, description_type="application/json")
        filter_type = request.GET.get("sort", "asc")  
        if filter_type == "asc":
            product_list = Product.objects.all().order_by("price")
        else :
            product_list = Product.objects.all().order_by("-price")
        data = [{
            'id': str(product.id)
            ,'name': product.name
            ,'price': product.price
            ,'category': product.category
            ,'description': product.description
            ,'user_id': product.user_id
            , 'thumbnail': product.thumbnail
            , 'is_featured': product.is_featured
            , 'rating': product.rating
        }
                for product in product_list]
        
        return JsonResponse(data, safe=False)
    
def show_xml_by_id(request, product_id):
    try:
        product_list = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, description_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'description': product.description,
            'user': product.user_id,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'rating': product.rating,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


    
def register(request):
    if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "Account created successfully!"}, status=200)
            else:
                return JsonResponse({"errors": form.errors}, status=400)
    elif request.method == "GET":
        form = UserCreationForm()
        # Mengirimkan objek 'form' ke konteks template
        return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        errors = {}

        if not username:
            errors['username'] = 'Username is required.'
        if not password:
            errors['password'] = 'Password is required.'

        if errors:
            return JsonResponse({'success': False, 'errors': errors}, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = JsonResponse({'success': True, 'message': 'Login successful!'})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            errors['__all__'] = 'Invalid username or password.'
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    elif request.method == 'GET':
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login.html', context)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return redirect('main:show_main')

    if request.method == 'POST':
        # Bagian ini adalah API untuk AJAX
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Produk berhasil diperbarui!'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    
    # Bagian ini untuk menampilkan halaman saat pertama kali diakses
    form = ProductForm(instance=product)
    context = {
        'form': form,
        'product': product
    }
    return render(request, "edit_product.html", context)
    



def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return JsonResponse({'message': 'Produk berhasil dihapus!'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def sort_product_category(request, category):
    # Kita tetap ambil list di sini (opsional jika mau render SSR awal)
    product_list = Product.objects.filter(category=category)
    filter_param = request.GET.get("filter")

    if filter_param == "my":
        product_list = product_list.filter(user=request.user)
    
    context = {
        'product_list': product_list,
        'active_category': category # PENTING: Kirim info kategori ke template
    }
    return render(request, "main.html", context)



@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        price = request.POST.get("price", 0)
        description = request.POST.get("description")
        category = request.POST.get("category")
        thumbnail = request.POST.get("thumbnail")
        is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
        user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)


def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

@csrf_exempt
def create_product_flutter(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        price = strip_tags(data.get("price", ""))
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        rating = data.get("rating", 0.0)
        print(request.user)
        print(request.user.username)
        user = request.user
        
        new_product = Product(
            price=price,
            name=name, 
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            rating=rating,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)