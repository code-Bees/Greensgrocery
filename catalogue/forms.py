from django import forms
from .models import Product
from django import forms




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =["title","category","description","supplier_price","supplier","selling_price","number_in_stock","kiosk","product_image"]

        widgets={
               'title':forms.TextInput(attrs={'class':'form-control'}),
               'category':forms.TextInput(attrs={'class':'form-control'}),
               'description':forms.TextInput(attrs={'class':'form-control'}),
               'supplier_price':forms.TextInput(attrs={'class':'form-control'}),
               'supplier':forms.TextInput(attrs={'class':'form-control'}),
               'selling_price':forms.TextInput(attrs={'class':'form-control'}),
               'number_in_stock':forms.TextInput(attrs={'class':'form-control'}),
               'kiosk':forms.TextInput(attrs={'class':'form-control'}),
               'product_image':forms.FileInput(attrs={'class':'form-control'}),


            }