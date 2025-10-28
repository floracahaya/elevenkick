from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'nama_aplikasi' : 'ElevenKick',
        'name': 'Flora Cahaya Putri',
        'class': 'PBP E',
        'npm' : '2406350955',
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username' : request.user.username,
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    context = {
        'form': form
    }
    return render(request, "create_product.html", context)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    price = request.POST.get("price")   
    user = requesedit.user

    new_product = Product(
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        price=price,  
        user=user
    )
    new_product.save()
    return HttpResponse(b"CREATED", status=201)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@csrf_exempt
@require_POST
def update_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    # ownership check -- require authenticated user and owner
    if not request.user.is_authenticated or request.user != product.user:
        return JsonResponse({'detail': 'Forbidden'}, status=403)

    # sanitize and update fields (only the ones provided)
    name = request.POST.get("name")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured_raw = request.POST.get("is_featured")
    price_raw = request.POST.get("price")

    try:
        if name is not None:
            product.name = strip_tags(name)
        if description is not None:
            product.description = strip_tags(description)
        if category is not None:
            product.category = category
        if thumbnail is not None:
            product.thumbnail = thumbnail
        if is_featured_raw is not None:
            product.is_featured = (is_featured_raw == 'on' or is_featured_raw.lower() == 'true')
        if price_raw is not None and price_raw != '':
            try:
                product.price = int(price_raw)
            except ValueError:
                # ignore invalid price and keep old
                pass
        product.save()
        return JsonResponse({'detail': 'UPDATED'}, status=200)
    except Exception as e:
        return JsonResponse({'detail': 'ERROR', 'error': str(e)}, status=500)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    if not request.user.is_authenticated or request.user != product.user:
        return JsonResponse({'detail': 'Forbidden'}, status=403)

    try:
        product.delete()
        return JsonResponse({'detail': 'DELETED'}, status=200)
    except Exception as e:
        return JsonResponse({'detail': 'ERROR', 'error': str(e)}, status=500)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.select_related('user').all().order_by('-date_added')
    data = []
    for product in product_list:
        data.append({
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price,
            'date_added': product.date_added.isoformat() if product.date_added else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        })
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)

        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price,
            'date_added': product.date_added.isoformat() if product.date_added else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@require_POST
@csrf_protect
def register_ajax(request):
    username = (request.POST.get('username') or '').strip()
    password1 = (request.POST.get('password1') or '').strip()
    password2 = (request.POST.get('password2') or '').strip()

    errors = {}
    
    # Validasi
    if not username:
        errors['username'] = ['Username is required']
    elif len(username) < 3:
        errors['username'] = ['Username must be at least 3 characters']
    elif User.objects.filter(username=username).exists():
        errors['username'] = ['Username already exists']
    
    if not password1:
        errors['password1'] = ['Password is required']
    elif len(password1) < 8:
        errors['password1'] = ['Password must be at least 8 characters']
    
    if not password2:
        errors['password2'] = ['Password confirmation is required']
    elif password1 != password2:
        errors['password2'] = ['Passwords do not match']
    
    if errors:
        return JsonResponse({
            'status': 'error',
            'errors': errors
        }, status=400)

    # Buat user baru
    try:
        new_user = User.objects.create_user(username=username, password=password1)
        new_user.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Registration successful'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        response.set_cookie('username', user.username) 
        return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)


@require_POST
@csrf_protect
def login_ajax(request):
    username = (request.POST.get('username') or '').strip()
    password = (request.POST.get('password') or '').strip()

    if not username or not password:
        return JsonResponse({'detail': 'MISSING_FIELDS', 'errors': {'non_field': 'Username dan password wajib.'}}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse({'detail': 'INVALID_CREDENTIALS'}, status=401)

    login(request, user)
    return JsonResponse({'detail': 'LOGGED_IN', 'redirect': '/'}, status=200)

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('username')
    return response 


@require_POST
@csrf_protect
def logout_ajax(request):
    logout(request)
    response = JsonResponse({
        'status': 'success',
        'message': 'You have been logged out successfully.'
    })
    response.delete_cookie('last_login')
    response.delete_cookie('username')
    return response
