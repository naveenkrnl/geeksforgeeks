from django.shortcuts import render
from .forms import GeeksForm

def handle_uploaded_file(f):  
    with open('geeks/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)  
# Create your views here.
def home_view(request):
    context={}
    if request.POST:
        form=GeeksForm(request.POST)
        print(request.POST)
    else:
        form=GeeksForm()
    context['form']=form
    return render(request,"home.html",context)