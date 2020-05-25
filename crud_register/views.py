from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient_B00, Patient_B01, Patient_B02
from .serializers import PatientB00Serializer, PatientB01Serializer, PatientB02Serializer
import coreapi
from rest_framework.schemas import AutoSchema

class PatientB00View(viewsets.ModelViewSet):
    queryset = Patient_B00.objects.all()
    serializer_class = PatientB00Serializer


class PatientB01View(viewsets.ModelViewSet):
    queryset = Patient_B01.objects.all()
    serializer_class = PatientB01Serializer


class PatientB02View(viewsets.ModelViewSet):
    queryset = Patient_B02.objects.all()
    serializer_class = PatientB02Serializer
