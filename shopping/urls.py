from django.urls import path
from .import views
from .views import upload_basket,cart_details

urlpatterns = [
    path('basket/upload/<int:product_id>/', upload_basket, name='upload-basket'),
    path('cart/details/<int:product_id>/' ,cart_details, name='cart-details'),

]