from django.urls import path
from .import views
from .views import upload_basket

app_name='shopping'

urlpatterns = [
    path('basket/upload/', upload_basket, name='upload-basket'),
    path(views.cart_detail, name='cart_detail'),
    path(views.cart_add, name='cart_add'),
    path(views.cart_remove , name='cart_remove'),  
]