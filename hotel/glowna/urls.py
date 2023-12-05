from django.urls import path, include
from . import views

app_name = "Główna"

urlpatterns = [
    path("",views.gl)
]