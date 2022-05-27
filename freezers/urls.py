from django.urls import path
from . import views, restAPIs

urlpatterns = [
    path("freezerWarehouse/", views.freezerWarehouse, name="freezerWarehouse"),
    path("freezerDevice/<int:pk>/", views.freezerDevice, name="freezerDevice"),
    path("freezerData/<int:pk>/", restAPIs.freezerData, name="freezerData"),
]
