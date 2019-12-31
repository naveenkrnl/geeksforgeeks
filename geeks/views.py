
from django.shortcuts import render
from .forms import GeeksForm

def home_view(request):
    context ={}

    # create object of form
    form = GeeksForm(request.POST or None, request.FILES or None)
    
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form']= form
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