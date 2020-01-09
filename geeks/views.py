from django.shortcuts import render

# relative import of forms
from .models import GeeksModel

# pass id attribute from urls
def update_view(request,id):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id=id)
        
    return render(request, "update_view.html", context)


# from django.shortcuts import render
# from .forms import GeeksForm

# # creating a home view
# def home_view(request):
#     context = {}
#     form = GeeksForm(request.POST or None)
#     context['form'] = form
#     return render(request, "home.html", context)