from django.shortcuts import render
from .forms import InputForm
 
# Create your views here.
# def home_view(request):
#     context ={}
#     context['form']= InputForm()
#     return render(request, "home.html", context)







def home_view(request):
    context ={}

    # dictionary for initial data with 
    # field names as keys

    # add the dictionary during initialization
    form = InputForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        print(type(request.FILES['img']))

        
    context['form']= form
    return render(request, "home.html", context)


# from django.shortcuts import render
# from .forms import GeeksForm

# # creating a home view
# def home_view(request):
#     context = {}
#     form = GeeksForm(request.POST or None)
#     context['form'] = form
#     return render(request, "home.html", context)