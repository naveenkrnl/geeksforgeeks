# import form class from django
from django import forms

<<<<<<< HEAD
class GeeksForm(forms.Form):
    geeks_field = forms.CharField(disabled=True)
=======
# import GeeksModel from models.py
from .models import GeeksModel

# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model=GeeksModel
        fields = "__all__"
>>>>>>> c6b83e68efb3c0574ef5e786ce6d862062ebeeaa
