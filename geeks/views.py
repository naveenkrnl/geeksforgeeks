# import Http Response from django
from django.shortcuts import render

# create a function
def geeks_view(request):
    # create a dictionary
    context = {
        "var1":None,
        "var2":None,
        "var3":"GeeksForGeeks"
    }
    # return response
    return render(request,"geeks.html",context)