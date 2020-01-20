from django.urls import path

# importing views from views..py
from .views import GeeksUpdateView
urlpatterns = [
    path('<pk>/update', GeeksUpdateView.as_view()),
]
