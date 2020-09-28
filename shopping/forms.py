from django import forms
from .models import Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields ='__all__' 

        widgets={
            'product':forms.TextInput(attrs={'class':'form-control'}),
            'date_created':forms.TextInput(attrs={'class':'form-control'}),
            'total_price':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control'}),
        
         }



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)