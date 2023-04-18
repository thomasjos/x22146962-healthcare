from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient,Doctor, Appointment, MedicalRecord, Billing
from .forms import PatientForm, DoctorForm, AppointmentForm, MedicalRecordForm, BillingForm


def home(request):
    return render(request, 'Health_Care_app/home.html')
    
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'Health_Care_app/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'Health_Care_app/patient_detail.html', {'patient': patient})

def patient_new(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    return render(request, 'Health_Care_app/patient_edit.html', {'form': form})

def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'Health_Care_app/patient_edit.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('patient_list')
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'Health_Care_app/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'Health_Care_app/doctor_detail.html', {'doctor': doctor})

# @login_required
def doctor_new(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.save()
            # messages.success(request, 'Doctor added successfully.')
            return redirect('doctor_detail', pk=doctor.pk)
    else:
        form = DoctorForm()
    return render(request, 'Health_Care_app/doctor_edit.html', {'form': form})

# @login_required
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            doctor = form.save()
            # messages.success(request, 'Doctor updated successfully.')
            return redirect('doctor_detail', pk=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'Health_Care_app/doctor_edit.html', {'form': form})
    
    
    
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'Health_Care_app/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'Health_Care_app/appointment_detail.html', {'appointment': appointment})

def appointment_new(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm()
    return render(request, 'Health_Care_app/appointment_edit.html', {'form': form})

def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save()
            return redirect('appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'Health_Care_app/appointment_edit.html', {'form': form})
    



def medicalrecord_list(request):
    records = MedicalRecord.objects.all()
    return render(request, 'Health_Care_app/medical_record_list.html', {'records': records})


def medicalrecord_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'Health_Care_app/medical_record_detail.html', {'record': record})


def medicalrecord_new(request):
    if request.method == "POST":
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('medicalrecord_detail', pk=record.pk)
    else:
        form = MedicalRecordForm()
    return render(request, 'Health_Care_app/medical_record_form.html', {'form': form})


def medicalrecord_edit(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == "POST":
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('medicalrecord_detail', pk=record.pk)
    else:
        form = MedicalRecordForm(instance=record)
    return render(request, 'Health_Care_app/medical_record_form.html', {'form': form})


def medicalrecord_delete(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect('medicalrecord_list')
    return render(request, 'Health_Care_app/medicalrecord_confirm_delete.html', {'record': record})
    
def billing_list(request):
    billings = Billing.objects.all()
    return render(request, 'Health_Care_app/billing_list.html', {'billings': billings})

def billing_new(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing_list')
    else:
        form = BillingForm()
    return render(request, 'Health_Care_app/billing_edit.html', {'form': form})

def billing_detail(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    return render(request, 'Health_Care_app/billing_detail.html', {'billing': billing})

def billing_edit(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=billing)
        if form.is_valid():
            form.save()
            return redirect('billing_list')
    else:
        form = BillingForm(instance=billing)
    return render(request, 'Health_Care_app/billing_edit.html', {'form': form})

def billing_delete(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        billing.delete()
        return redirect('billing_list')
    return render(request, 'Health_Care_app/billing_confirm_delete.html', {'billing': billing})
