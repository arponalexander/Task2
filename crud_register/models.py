from django.db import models
from phone_field import PhoneField

MALE = 'Male'
FEMALE = 'Female'
OTHER = 'Other'

Gender_Choice = [
    ('Male', MALE),
    ('Female', FEMALE),
    ('Other', OTHER),
]


class Patient_B00(models.Model):
    patient_Rec = models.CharField(max_length=100)
    first_Name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=Gender_Choice, max_length=10)
    birthdate = models.DateField()
    active_status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Patient B00'

    def __str__(self):
        return self.patient_Rec


class Patient_B01(models.Model):
    patient_Insurance_Rec = models.CharField(max_length=100)
    patient_Rec = models.ForeignKey(Patient_B00, on_delete=models.DO_NOTHING)
    insurance_rec = models.CharField(max_length=100)
    first_Name = models.CharField(max_length=100)
    middle_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    date_of_Birth = models.DateField()
    relationship_to_Patient = models.CharField(max_length=100)
    member_Id = models.IntegerField()
    group_Id = models.IntegerField()
    active_status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Patient_B01'

    def __str__(self):
        return self.patient_Insurance_Rec


class Patient_B02(models.Model):
    patient_Guardian_Rec = models.CharField(max_length=100)
    patient_Rec = models.ForeignKey(Patient_B00, on_delete=models.DO_NOTHING)
    relationship_to_Patient = models.ForeignKey(Patient_B01, on_delete=models.DO_NOTHING, max_length=100)
    first_Name = models.CharField(max_length=100)
    middle_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_Code = models.IntegerField()
    phone_Home = PhoneField(blank=True, help_text='Phone Number')
    phone_Work = PhoneField(blank=True, help_text='Phone Number')
    eMail_Address = models.EmailField(max_length=100)
    company_Rec = models.CharField(max_length=100)
    active_status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Patient_B02'

    def __str__(self):
        return self.patient_Guardian_Rec
