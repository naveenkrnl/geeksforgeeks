from django.shortcuts import render
from .forms import GeeksForm

# Create your views here.
def home_view(request):
    context ={}
    if request.method=="POST":
        form = GeeksForm(request.POST)
        if form.is_valid():
            temp=form.cleaned_data.get("geeks_field")
            print(type(temp))
    else:
        form=GeeksForm()
    context['form']=form
    return render(request, "home.html", context)