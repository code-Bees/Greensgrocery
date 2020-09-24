from django import forms
from .models import Cart
from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)




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

       