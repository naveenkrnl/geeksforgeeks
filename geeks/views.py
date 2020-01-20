from django.views.generic.list import ListView
from .models import GeeksModel

class GeeksList(ListView):

    # specify the model for list view
    model = GeeksModel

    def get_queryset(self, *args, **kwargs):
        qs=super(GeeksList,self).get_queryset(*args,**kwargs)
        qs=qs.order_by("-id")
        return qs