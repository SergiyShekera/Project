from django.urls import path
from cupons.views import CuponApply

app_name='cupons'

urlpatterns = [
    path('apply', CuponApply, name='apply')
]
