from django.urls import path
from .import views
from .views import upload_basket

urlpatterns = [
    path('basket/upload/', upload_basket, name='upload-basket'),
    
]