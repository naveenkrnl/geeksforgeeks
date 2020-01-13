from django.urls import path

# importing views from views..py
from .views import update_view ,detail_view

urlpatterns = [
    path('<id>/', detail_view ),
    path('<id>/update', update_view ),
]
