from django import forms

class ArrayLength(forms.Form):
    n = forms.IntegerField(label='Length of array to sort', max_length=100)