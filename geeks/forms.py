from django import forms


class GeeksForm(forms.Form):
    name         = forms.CharField()
    geeks_field  = forms.FilePathField(path="geeksforgeeks/")
    