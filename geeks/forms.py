from django import forms

class GeeksForm(forms.Form):
    geeks_field         = forms.CharField(initial="Enter your Name")
