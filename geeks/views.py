from django.shortcuts import get_object_or_404,render ,HttpResponseRedirect

from .models import GeeksModel


# delete view for details
def delete_view(request,id):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id=id)


    if request.method=="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)