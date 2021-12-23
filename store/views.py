from django.views.generic import ListView
from .models import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


def index(request):
    return render(request, "index.html")


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


def categories(request):
    products(request)
    category = Category.objects.all()
    return render(request, 'category/categories.html', {'category': category})


def category_add(request):
    return render(request, 'category/categories_add.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def product_add(request):
    print(request.POST)
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
    return render(request, "products/products_edit.html", {"products": products, "product": product})


def subcategory(request):
    subcat = SubCategory.objects.all()
    return render(request, 'subcategory/subcategory.html', {'subcat': subcat})


def subcat_add(request):
    return render(request, 'subcategory/subcategory_add.html')
