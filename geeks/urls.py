from django.urls import path

# importing views from views..py
from .views import geeks_view , nav_view

urlpatterns = [
    path('1/', geeks_view, name = "template1"),
    path('2/', nav_view,name = "template2"),
]