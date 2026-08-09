from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all().order_by("-created_at")[:4]

    return render(request, "home/index.html", {
        "products": products
    })


def products(request):
    products = Product.objects.all().order_by("-created_at")

    return render(request, "home/products.html", {
        "products": products
    })


def product_detail(request, product_id):
    product = Product.objects.filter(
        id=product_id
    ).first()

    return render(request, "home/product_detail.html", {
        "product": product
    })