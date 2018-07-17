from django.urls import path
from cart.views import Cart_Add, Cart_Remove, Cart_Detail

app_name='cart'

urlpatterns = [
    path('remove/<product_id>', Cart_Remove, name='CartRemove'),
    path('add/<product_id>', Cart_Add, name='CartAdd'),
    path('', Cart_Detail, name='CartDetail')
]