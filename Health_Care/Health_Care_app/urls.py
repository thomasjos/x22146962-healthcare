from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/new/', views.patient_new, name='patient_new'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/new/', views.doctor_new, name='doctor_new'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/new/', views.appointment_new, name='appointment_new'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),
    
    path('medicalrecords/', views.medicalrecord_list, name='medicalrecord_list'),
    path('medicalrecords/new/', views.medicalrecord_new, name='medicalrecord_new'),
    path('medicalrecords/<int:pk>/', views.medicalrecord_detail, name='medicalrecord_detail'),
    path('medicalrecords/<int:pk>/edit/', views.medicalrecord_edit, name='medicalrecord_edit'),
    path('medicalrecords/<int:pk>/delete/', views.medicalrecord_delete, name='medicalrecord_delete'),
    
    path('billings/', views.billing_list, name='billing_list'),
    path('billings/new/', views.billing_new, name='billing_new'),
    path('billings/<int:pk>/', views.billing_detail, name='billing_detail'),
    path('billings/<int:pk>/edit/', views.billing_edit, name='billing_edit'),
    path('billings/<int:pk>/delete/', views.billing_delete, name='billing_delete'),
    
]
