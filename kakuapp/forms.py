from django import forms
from .models import Product, Sale

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SaleForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = Sale
        fields = ['product', 'quantity']
