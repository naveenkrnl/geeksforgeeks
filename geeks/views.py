from django.shortcuts import render

# relative import of forms
from .models import GeeksModel

# importing formset_factory
from django.forms import modelformset_factory

def modelformset_view(request):
    context ={}

    # creating a formset and 5 instances of GeeksForm
    GeeksFormSet = modelformset_factory(GeeksModel, fields=['title','description'],extra=2)
    formset = GeeksFormSet(request.POST or None)
    
    # print formset data if it is valid
    if formset.is_valid():
        formset.save()
            
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)
















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