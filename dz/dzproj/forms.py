from django import forms

class WareForm(forms.Form):
    wid = forms.DecimalField(max_digits=1)
    image = forms.ImageField()
    name = forms.CharField(max_length=100)
    description = forms.CharField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.CharField(max_length=100)