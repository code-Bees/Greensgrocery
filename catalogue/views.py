from django.shortcuts import render
from .models import Product


# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request, 'product_list.html', {'product': product})
    
    
 



 

      
 

 


 