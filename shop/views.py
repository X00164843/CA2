from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def allProdCat(request, category_id=None):
    page = None
    products = None
    if category_id != None:
        page = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=page, available=True)
    else:
        products = Product.objects.all().filter(available=True)

    return render(request,'shop/category.html',{'category':page, 'products':products})

def prod_detail(request, category_id, product_id):
    try:
        product = Product.objects.get(category_id = category_id, id=product_id)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product':product})
