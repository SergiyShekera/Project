from django.urls import path
from shop.views import ProductList, ProductDetail

app_name='shop'

urlpatterns = [
    path('', ProductList, name='ProductList' ),
    path('<category_slug>/', ProductList, name='ProductListByCategory' ),
    path('<int:id>/<slug:slug>/', ProductDetail, name='ProductDetail' )
]

