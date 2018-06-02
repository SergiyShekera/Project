from django.urls import path
from shop.views import ProductList, ProductDetail
from shop.views import Product_List_View, Product_Detail_View, Product_Category_List_View

app_name='shop'

urlpatterns = [

    path('api/prod-list', Product_List_View.as_view()),
    path('api/prod-detail/<int:id>/', Product_Detail_View.as_view()),
    path('api/prod-category-list/<int:id>/', Product_Category_List_View.as_view()),

    path('', ProductList, name='ProductList' ),
    path('<category_slug>/', ProductList, name='ProductListByCategory' ),
    path('<int:id>/<slug:slug>/', ProductDetail, name='ProductDetail' ),

    path('<category_slug>/', Product_List_View.as_view(), name='prod_list'),
    path('<int:id>/<slug:slug>/', Product_Detail_View.as_view(), name='prod_detail'),


]