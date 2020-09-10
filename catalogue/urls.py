from django.urls import path
from . import views
from .views import product_list, details

urlpatterns = [
    path('templates/', product_list, name='product_list'),
    path('products/<int :product_id>/',details,name='details')

]