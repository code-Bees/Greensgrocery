from django.urls import path
from .import views
from .views import upload_basket

urlpatterns = [
    path('basket/upload/<int:product_id>/', upload_basket, name='upload-basket'),
    #path('show/basket/' ,show_basket, name='show-basket'),

    # path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    # path('cart/cart_remove/', views.cart_remove, name='cart_clear'),
    # path('cart/cart_detail/',views.cart_detail,name='cart_details'),
]