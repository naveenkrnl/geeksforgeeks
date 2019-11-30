from django.shortcuts import render
from .forms import GeeksForm
from .models import GeeksModel
# Create your views here.
def home_view(request):
    context ={}
    if request.method=="POST":
        form = GeeksForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("geeks_field")
            obj = GeeksModel.objects.create(title=name,img=img)
            obj.save()
            print(obj)
    else:
        form=GeeksForm()
    context['form']=form
    return render(request, "home.html", context)