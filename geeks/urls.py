from django.urls import path

# importing views from views..py
from .views import GeeksCreate
urlpatterns = [
    path('create/', GeeksCreate.as_view() ),
]
