from django import forms
from app_002_mixins.models import *

class testInfoForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter name'}), max_length=100, required=True, error_messages={'required': 'Name is required.'})
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter phone'}), max_length=15, required=False, error_messages={'required': 'Phone is required.'})
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter address'}), max_length=200, required=False, error_messages={'required': 'Address is required.'})
    #Validation for phone number
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone
    
    class Meta:
        model = testInfo
        fields = ['name', 'phone', 'address']