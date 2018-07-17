from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import Cart_Add_Product_Form
from cupons.forms import Cupon_Aplly_Form



@require_POST
def Cart_Add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = Cart_Add_Product_Form(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])

    return redirect('cart:CartDetail')

def Cart_Remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')

def Cart_Detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = Cart_Add_Product_Form(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    cupon_apply_form = Cupon_Aplly_Form()
    return render(request, 'cart/detail.html',
                 {'cart': cart, 'cupon_apply_form': cupon_apply_form})



