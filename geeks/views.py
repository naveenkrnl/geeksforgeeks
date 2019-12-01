from django.shortcuts import render
from .forms import GeeksForm
from .models import GeeksModel

# Create your views here.
def home_view(request):
    context ={}
    form = GeeksForm(request.POST or None)
    context['form']= form
    if request.POST:
        if form.is_valid():
            temp=form.cleaned_data.get("geeks_field")
            print(type(temp))
    return render(request, "home.html", context)