from django.urls import path
from cupons.views import Cupon_Apply

app_name='cupons'

urlpatterns = [
    path('apply', Cupon_Apply, name='apply')
]
