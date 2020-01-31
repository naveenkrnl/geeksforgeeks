# import Http Response from django
from django.shortcuts import render
 
# create a function
def geeks_view(request):
    # create a dictionary
    context = {
        "data" : False,
    }
    # return response
    return render(request,"geeks.html",context)