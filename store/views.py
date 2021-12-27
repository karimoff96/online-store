from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserForm, UserRegistrationForm


@login_required
def index(request):
    product = len(Product.objects.all())
    category = len(Category.objects.all())
    subcate = len(SubCategory.objects.all())
    user = len(Users.objects.all())
    return render(request, "index.html",
                  {'product': product, 'category': category, 'subcate': subcate, 'user': user})


def log_in(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect('/index')
    else:
        return render(request, 'login.html')


def categories(request):
    category = Category.objects.all()
    return render(request, 'category/categories.html', {'category': category})


def category_add(request):
    if request.method == "POST" and request.FILES['image']:
        upload_photo = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload_photo.name, upload_photo)
        file_url = fss.url(file)
        a = request.POST
        category = Category.objects.create(
            name=a['name'],
            image=file_url,
            active=a['active']
        )
        category.save()
        return redirect('/categories')
    return render(request, 'category/category_add.html')


def category_edit(request, id):
    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        a = request.POST
        category.name = a['name']
        category.image = a['image']
        category.active = a['active']
        category.save()
        return redirect('/categories')
    return render(request, 'category/category_edit.html', {'categories': categories, 'category': category})


def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/categories')


def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def product_add(request):
    categories = Category.objects.all()
    subcat = SubCategory.objects.all()
    if request.method == "POST":
        a = request.POST
        product = Product.objects.create(
            name=a['name'],
            code=a['code'],
            model=a['model'],
            datetime=a['cr_on'],
            description=a['description'],
            type=a['type'],
            image=a['image'],
            price=a['price'],
            active=a['active']
        )
        product.save()
        return redirect('/products')
    return render(request, 'products/products_add.html', {'categories': categories, 'subcat': subcat})


def product_edit(request, id):
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        a = request.POST
        product.name = a['name']
        product.code = a['code']
        product.model = a['model']
        product.datetime = a['cr_on']
        product.description = a['description']
        product.type = a['type']
        product.image = a['image']
        product.price = a['price']
        product.active = a['active']
        product.save()
        return redirect('/products')
    return render(request, "products/products_edit.html", {"products": products, "product": product})


def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/products')


def subcategory(request):
    subcat = SubCategory.objects.all()
    return render(request, 'subcategory/subcategory.html', {'subcat': subcat})


def subcat_add(request):
    category = Category.objects.all()
    if request.method == 'POST':
        a = request.POST
        subcat = SubCategory.objects.create(
            name=a['name'],
            cr_on=a['cr_on'],
            image=a['image'],
            active=a['active']
        )
        subcat.save()
        return redirect('/subcat')
    return render(request, 'subcategory/subcategory_add.html', {'category': category})


def subcat_edit(request, id):
    subcats = SubCategory.objects.all()
    subcate = SubCategory.objects.get(id=id)
    if request.method == 'POST':
        a = request.POST
        subcate.name = a['name']
        subcate.cr_on = a['cr_on']
        subcate.image = a['image']
        subcate.active = a['active']
        subcate.save()
        return redirect('/subcat')
    return render(request, "subcategory/subcategory_edit.html", {"subcats": subcats, "subcate": subcate})


def subcat_delete(request, id):
    subcat = SubCategory.objects.get(id=id)
    subcat.delete()
    return redirect('/subcat')
