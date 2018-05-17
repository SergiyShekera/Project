from django.urls import path
from cart.views import CartAdd, CartRemove, CartDetail

app_name='cart'

urlpatterns = [
    path('remove/<product_id>', CartRemove, name='CartRemove'),
    path('add/<product_id>', CartAdd, name='CartAdd'),
    path('', CartDetail, name='CartDetail')
]