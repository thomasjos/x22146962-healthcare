from django.db import models
from django.urls import reverse

class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    blood_type = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient} - {self.doctor} - {self.date} {self.time}'
        
class MedicalRecord(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.date}"

    def get_absolute_url(self):
        return reverse('medicalrecord_detail', args=[str(self.pk)])
        
        
class Billing(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    medical_record = models.ForeignKey('MedicalRecord', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient} - {self.date}'
