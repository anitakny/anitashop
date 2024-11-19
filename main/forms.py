from django import forms
from main.models import ProductForm
from django.utils.html import strip_tags

class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductForm
        fields = ['name', 'price', 'quantity', 'description']

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)  