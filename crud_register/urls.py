from django.urls import path,include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('Patient_B00', views.PatientB00View)
routers.register('Patient_B01', views.PatientB01View)
routers.register('Patient_B02', views.PatientB02View)

urlpatterns = [
    path('', include(routers.urls))
]