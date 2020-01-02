from django import forms

class GeeksForm(forms.Form):
    title         = forms.CharField()
    description   = forms.CharField()
