from django.urls import path

# importing views from views..py
from .views import modelformset_view

urlpatterns = [
    path('', modelformset_view ),
]
