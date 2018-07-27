from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from cart.forms import Cart_Add_Product_Form
from django.template.context_processors import csrf
from rest_framework import generics
from .serializers import Category_Serializer, Category_Create_Serializer
from .serializers import Product_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


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


class Category_Create_View(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):

        Cat = Category_Create_Serializer(data=request.data)

        if Cat.is_valid():

            Cat.save()

            return Response({"status": "Create"})


def Product_List(request, category_slug=None):

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


def Product_Detail(request, id, slug):

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = Cart_Add_Product_Form()
    context = {'product': product, 'cart_product_form': cart_product_form}
    context.update(csrf(request))
    return render_to_response('shop/product/detail.html', context)

def Shop_main(request):
    return render_to_response('Shop-main.html')