from django import forms
from main.models import ProductForm

class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductForm
        fields = ['name', 'price', 'quantity']
