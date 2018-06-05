from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.template.context_processors import csrf
from rest_framework import generics
from .serializers import Category_Serializer
from .serializers import Product_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Product_List_View(generics.ListAPIView):

    queryset = Product.objects.filter(available=True)
    serializer_class = Product_Serializer

class Category_List_View(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = Category_Serializer

class Product_Detail_View(APIView):

    queryset = Product.objects.all()

    def get(self, request, id):
        product = get_object_or_404(Product, id=id, available=True)
        serializer = Product_Serializer(product)
        return Response(serializer.data)

class Product_Category_List_View(APIView):

    queryset = Category.objects.all()

    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = Category_Serializer(category)
        return Response(serializer.data)



def ProductList(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render_to_response('shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    }
                  )


def ProductDetail(request, id, slug):

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    context.update(csrf(request))
    return render_to_response('shop/product/detail.html', context)

def Shop_main(request):
    return render_to_response('Shop-main.html')