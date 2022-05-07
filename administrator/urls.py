from django.urls import path
from . import views, ajax, restAPIs

urlpatterns = [
    path("", views.index, name="index"),
    path("freezerWarehouse/", views.freezerWarehouse, name="freezerWarehouse"),
    path("freezerDevice/<int:pk>/", views.freezerDevice, name="freezerDevice"),
    path(r"warehouse/", views.warehouse, name="warehouse"),
    path("freezerData/<int:pk>/", restAPIs.freezerData, name="freezerData"),
]
