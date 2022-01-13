from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage


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


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def categories(request):
    category = Category.objects.all()
    return render(request, 'category/categories.html', {'category': category, 'request': request})


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
    if request.method == "POST":
        a = request.POST
        try:
            upload_photo = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(upload_photo.name, upload_photo)
            file_url = fss.url(file)
            category.name = a['name']
            category.image = file_url
            category.active = a['active']
            category.save()
        except:
            category.name = a['name']
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
    if request.method == "POST" and request.FILES['image']:
        upload_photo = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload_photo.name, upload_photo)
        file_url = fss.url(file)
        a = request.POST
        product = Product.objects.create(
            name=a['name'],
            code=a['code'],
            model=a['model'],
            description=a['description'],
            type=a['type'],
            image=file_url,
            price=a['price'],
            active=a['active']
        )
        product.save()
        return redirect('/products')
    return render(request, 'products/products_add.html', {'categories': categories, 'subcat': subcat})


def product_edit(request, id):
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    if request.method == "POST":
        a = request.POST
        try:
            upload_photo = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(upload_photo.name, upload_photo)
            file_url = fss.url(file)
            product.name = a['name']
            product.code = a['code']
            product.model = a['model']
            product.image = file_url
            product.description = a['description']
            product.type = a['type']
            product.price = a['price']
            product.active = a['active']
            product.save()
        except:
            product.name = a['name']
            product.code = a['code']
            product.model = a['model']
            product.description = a['description']
            product.type = a['type']
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
    if request.method == "POST" and request.FILES['image']:
        upload_photo = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload_photo.name, upload_photo)
        file_url = fss.url(file)
        a = request.POST
        subcat = SubCategory.objects.create(
            name=a['name'],
            image=file_url,
            active=a['active']
        )
        subcat.save()
        return redirect('/subcat')
    return render(request, 'subcategory/subcategory_add.html', {'category': category})


def subcat_edit(request, id):
    subcats = SubCategory.objects.all()
    subcate = SubCategory.objects.get(id=id)
    if request.method == "POST":
        a = request.POST
        try:
            upload_photo = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(upload_photo.name, upload_photo)
            file_url = fss.url(file)
            subcate.name = a['name']
            subcate.image = file_url
            subcate.active = a['active']
            subcate.save()
        except:
            subcate.name = a['name']
            subcate.active = a['active']
            subcate.save()
        return redirect('/subcat')
    return render(request, "subcategory/subcategory_edit.html", {"subcats": subcats, "subcate": subcate})


def subcat_delete(request, id):
    subcat = SubCategory.objects.get(id=id)
    subcat.delete()
    return redirect('/subcat')
