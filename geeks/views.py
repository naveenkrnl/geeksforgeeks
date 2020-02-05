# import Http Response from django
from django.shortcuts import render
 
# create a function
def geeks_view(request):
    # return response
    return render(request,"geeks.html")

def nav_view(request):
    # return response
    return render(request,"nav.html")