from django.shortcuts import render
from .models import Product


# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request, 'product_list.html', {'product': product})

def details(request,product_id):
    product=Product.objects.get(id=product_id) 
    images=product.images.all()  
    return render(request,'details.html', {'product':product,'images':images})
    
 



 

      
 

 


 