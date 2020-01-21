from django.urls import path

# importing views from views..py
from .views import GeeksDeleteView
urlpatterns = [
    path('<pk>/delete', GeeksDeleteView.as_view()),
]
