from django.shortcuts import render,redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
 
# Create your views here.
def product_list(request ):
    product = Product.objects.all()
    return render(request, 'Product_list.html', {'product': product})

def details(request,product_id):
    product=Product.objects.filter(id=product_id) 
    return render(request,'details.html', {'product':product,})

def upload_product(request):
    if request.method == 'POST':
        import pdb
        pdb.set_trace()
        form = ProductForm(request.POST,request.FILES)
        if  form.is_valid():
             form.save()
        return redirect('product-list')    
    else:
       form = ProductForm
       return render (request,'upload_product.html',{'form':form})



    
    
   
       
    
        


    
 



 

      
 

 


 