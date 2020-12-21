from django.shortcuts import render, redirect

from apps.cart.cart import Cart
from .models import Product


def main_page(request):
    if 'name' in request.GET:
        products = Product.objects.filter(name__icontains=request.GET.get('name'))
    else:
        products = Product.objects.all().order_by('-pk')
    return render(request, 'main-page.html', locals())

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        cart = Cart(request)
        data = request.POST
        pr_item = product.product_items.get(pk=int(data.get('product-id')))
        cart.add(pr_item, int(data.get('quantity')))
    return render(request, 'product-detail.html', locals())
