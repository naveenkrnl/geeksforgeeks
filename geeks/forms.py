from django import forms
<<<<<<< HEAD
 
# creating a form 
class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    img = forms.FileField()
=======

class GeeksForm(forms.Form):
    title         = forms.CharField()
    description   = forms.CharField()
>>>>>>> f777a26cbd66f7a203bad6744fcf646d8e8ba0df
