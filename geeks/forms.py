from django import forms

# creating a form
class GeeksForm(forms.Form):
    # specify fields for model
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)