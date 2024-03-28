from django import forms

class WareForm(forms.Form):
    wid = forms.DecimalField(label='Номер товара')
    image = forms.ImageField(label='Ваше изображение')