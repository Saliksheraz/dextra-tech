from django.urls import path
from . import views, ajax, restAPIs

urlpatterns = [
    path("", views.index, name="index"),

    path("freezerWarehouse/", views.freezerWarehouse, name="freezerWarehouse"),
    path("freezerDevice/<int:pk>/", views.freezerDevice, name="freezerDevice"),
    path("freezerData/<int:pk>/", restAPIs.freezerData, name="freezerData"),

    path(r"adminPanel/", views.adminPanel, name="adminPanel"),
]
