from django.shortcuts import render,redirect
from .forms import KioskForm,KioskOwnerForm

# Create your views here.

def upload_kiosk(request):
    if request.method == 'POST':
         form = KioskForm(request.POST)
         if  form.is_valid():
             form.save()
         return redirect('upload-product')    
    else:
       form = KioskForm
       return render(request,'upload_kiosk.html',{'form':form})
        

def upload_owner(request):
    if request.method == "POST":
         form = KioskOwnerForm(request.POST,request.FILES)
         if  form.is_valid():
             form.save()
         return redirect('product_list.html')    
    else:
       form = KioskOwnerForm
       return render(request,'upload_kioskOwner.html',{'form':form})
                

    
    
   
    
    
   
       