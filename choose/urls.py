from django.urls import path
from . import views

urlpatterns = [
    path('get_available_choices', views.get_available_choices),
]
