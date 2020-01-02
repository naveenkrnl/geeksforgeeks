from django.shortcuts import render

# relative import of forms
from .forms import GeeksForm

# importing formset_factory
from django.forms import formset_factory

def formset_view(request):
    context ={}

    # creating a formset and 5 instances of GeeksForm
    GeeksFormSet = formset_factory(GeeksForm, extra = 3)
    formset = GeeksFormSet(request.POST or None)
    
    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
            
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)
















# def home_view(request):
#     context ={}

#     # dictionary for initial data with 
#     # field names as keys

#     # add the dictionary during initialization
#     form = GeeksForm(request.POST or None)

#     context['form']= form
#     return render(request, "home.html", context)


# from django.shortcuts import render
# from .forms import GeeksForm

# # creating a home view
# def home_view(request):
#     context = {}
#     form = GeeksForm(request.POST or None)
#     context['form'] = form
#     return render(request, "home.html", context)