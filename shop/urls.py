from django.urls import path
from shop.views import ProductList, ProductDetail
# from django.contrib.auth.decorators import login_required
#
# urlpatterns = [
#
#     path('all', views.ProductList, name='ProductListByCategory'),
#     path('add', add_stud),
#     path('attadd', attestat_add),
#     path('attall', all_att),
#     path('find', find_students)
#
# ]
from . import views

app_name='shop'

urlpatterns = [
    path('', ProductList, name='ProductList' ),
    path('<category_slug>/', ProductList, name='ProductListByCategory' ),
    path('<int:id>/<slug:slug>/', ProductDetail, name='ProductDetail' )
]

# urlpatterns = [
#     path('all', all_groups),
#     path('add', add_group),
#     path('<int:id>', GetGroup.as_view())
# ]