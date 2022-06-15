from django.urls import path
from . import views, restAPIs

urlpatterns = [
    path("main/", views.smartracks, name="smartracks"),
    path("warehouse/<int:pk>/", views.warehouse, name="warehouse"),


    path("cloud/<int:pk>/", restAPIs.warehouseData, name="cloudWarehouse"),
]
