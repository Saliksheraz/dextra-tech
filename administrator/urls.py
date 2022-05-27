from django.urls import path
from . import views, ajax, restAPIs

urlpatterns = [
    path("", views.index, name="index"),
    
    path(r"adminPanel/", views.adminPanel, name="adminPanel"),
]
