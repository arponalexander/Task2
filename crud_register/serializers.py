from rest_framework import serializers
from .models import Patient_B00, Patient_B01, Patient_B02


class PatientB00Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient_B00
        fields = '__all__'


class PatientB01Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient_B01
        fields = '__all__'


class PatientB02Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient_B02
        fields = '__all__'
