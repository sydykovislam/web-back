from django.shortcuts import render
from django.http import JsonResponse

from .cart import Cart
from apps.products.models import ProductItem


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart-detail.html', locals())

def change_quantity(request):
    quantity = int(request.GET.get('quantity'))
    price = ProductItem.objects.get(pk=int(request.GET.get('id')[8:])).price    
    date = {'total_price': price*quantity}
    return JsonResponse(date)

def item_ad(request):
    print(request.POST)
    if request.POST.get('remove'):
        cart = Cart(request)
        cart.remove(request.POST.get('id'))
        return JsonResponse({'status': '200'})