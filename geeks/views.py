# import Http Response from django
from django.shortcuts import render

# create a function
def geeks_view(request):
    # create a dictionary
    context = {
        "data" : [1,2,3,4,5,6,7,8,9,10],
    }
    # return response
    return render(request,"geeks.html",context)