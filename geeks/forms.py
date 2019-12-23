from django import forms

class GeeksForm(forms.Form):
    title         = forms.CharField(initial = "Method 2 ")
    description   = forms.CharField(initial = "Method 2 description")
    available     = forms.BooleanField(initial = True)
    email         = forms.EmailField(initial = "abc@gmail.com")


