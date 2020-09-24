from django import forms
from .models import Kiosk,KioskOwner
from django import forms




class KioskForm(forms.ModelForm):
    class Meta:
        model = Kiosk
        fields ='__all__'

        widgets={
            'owner':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'date_opened':forms.TextInput(attrs={'class':'form-control'}),
            'street_address':forms.TextInput(attrs={'class':'form-control'}),
            'currency':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'business_type':forms.TextInput(attrs={'class':'form-control'}),
            
         }



class KioskOwnerForm(forms.ModelForm):
    class Meta:
        model = KioskOwner
        fields ='__all__'        

         