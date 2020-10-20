from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product
from .forms import CartForm
from .models import Cart
from .forms import QuantityForm

# Create your views here.
def upload_basket(request,product_id):
    product=Product.objects.filter(id=product_id) 
    return render(request,'Upload_basket.html',{'product':product})

def cart_details(request,product_id):
    product=Product.objects.filter(id=product_id)
    return render(request,'cart_details.html',{'product':product})



   

# def show_basket(request):
#     if request.method == "POST":
#          form = CartForm(request.POST,request.FILES)
#          if  form.is_valid():
#              form.save()
#          return redirect('product_list')    
#     else:
#        form = CartForm
#        return render(request,'show_basket.html',{'form':form})

# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         # cd = form.cleaned_data
#         # cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
#      return redirect('cart:cart_details')


# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_details')


# def cart_detail(request):
#     cart = Cart(request)
#     for item in Cart.objects.filter():
#        # item['CartAddProductForm'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
#      return render(request, 'Cart/details.html', {'cart': cart})


# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = Product.objects.filter(category=category)

#     context = {
#         'category': category,
#         'categories': categories,
#         'products': products
#     }
#     return render(request, 'catalogue/product_list.html', context)


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     context = {
#         'product': product,
#         'cart_product_form': cart_product_form
#     }
#     return render(request, 'catalogue/details.html', context)


          