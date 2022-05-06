from django.urls import path
from . import views, ajax, restAPIs
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'warehouse/', views.warehouse, name='warehouse'),

    path('sensorData/<int:pk>/<int:items>/',
         restAPIs.sensorsDataView.as_view()),
]
