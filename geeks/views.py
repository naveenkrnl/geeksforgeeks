# import generic UpdateView
from django.views.generic.edit import DeleteView

# Relative import of GeeksModel
from .models import GeeksModel

class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = GeeksModel
    
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url="/"