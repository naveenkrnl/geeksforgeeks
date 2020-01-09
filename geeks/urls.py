from django.urls import path

# importing views from views..py
from .views import update_view

urlpatterns = [
    path('<id>/update', update_view ),
]
