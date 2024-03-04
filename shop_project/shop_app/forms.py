from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        labels = {
            "name": "название",
            'description': "описание",
            'price': "цена",
            "number": "количество",
            'product_added': "дата добавления",
            'image': "фото"  
        }

# class ProductForm(forms.Form):
#    name = forms.CharField(max_length=50)
#    description = forms.CharField(widget=forms.Textarea)
#    price = forms.DecimalField(max_digits=10, decimal_places=2)
#    number = forms.IntegerField()
#    product_added = forms.DateField()
#    image = forms.ImageField(default=None)
