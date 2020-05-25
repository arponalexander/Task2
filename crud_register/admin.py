from django.contrib import admin
from .models import Patient_B00, Patient_B01, Patient_B02


class CRUDAdminLook1(admin.ModelAdmin):
    list_display = ['patient_Rec']


class CRUDAdminLook2(admin.ModelAdmin):
    list_display = ['patient_Insurance_Rec']


class CRUDAdminLook3(admin.ModelAdmin):
    list_display = ['patient_Guardian_Rec']


admin.site.register(Patient_B00, CRUDAdminLook1)
admin.site.register(Patient_B01, CRUDAdminLook2)
admin.site.register(Patient_B02, CRUDAdminLook3)
