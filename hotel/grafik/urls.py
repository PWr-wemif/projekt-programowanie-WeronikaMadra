from django.urls import path, include
from . import views

app_name ="grafik"

urlpatterns = [
    path("",views.test)
]
