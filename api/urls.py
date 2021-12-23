from .views import ProductAPIView
from django.urls import path

urlpatterns = [
    path('', ProductAPIView.as_view()),
]