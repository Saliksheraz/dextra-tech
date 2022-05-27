from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.smartracks, name="smartracks"),
    path("warehouse/<int:pk>/", views.warehouse, name="warehouse"),
]
