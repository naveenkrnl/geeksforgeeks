from django.urls import path

# importing views from views..py
from .views import formset_view

urlpatterns = [
    path('', formset_view ),
]
