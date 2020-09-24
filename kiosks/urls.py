from django.urls import path
from .import views
from .views import upload_kiosk

urlpatterns = [
    path('kiosks/upload/', upload_kiosk, name='upload_kiosk'),
    #path('owner/upload/', upload_owner, name='upload-owner'),
    
]