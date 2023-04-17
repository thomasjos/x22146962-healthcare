from django import forms
from .models import Patient, Doctor, Appointment, MedicalRecord, Billing

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'email', 'phone', 'specialty')
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient', 'doctor', 'date', 'time')
        

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'date', 'description']
        
class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient','medical_record', 'date', 'amount',]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
