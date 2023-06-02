from django.urls import path

from . import views
from .views import (
    DoctorCreateView,
    DoctorListView,
    export_doctors,
    DoctorDeleteView,
    DoctorUpdateView,
    PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView, export_patients,
)

app_name = "hospital"

urlpatterns = [
    path("", views.index, name="index"),

    # doctor
    path("doctors/", DoctorListView.as_view(), name="doctors"),
    path("doctors/create", DoctorCreateView.as_view(), name="create_doc"),
    path("doctors/<pk>/update", DoctorUpdateView.as_view(), name="update_doc"),
    path("doctors/<pk>/delete", DoctorDeleteView.as_view(), name="delete_doc"),
    path("doctors/export/", export_doctors, name="export_doctors"),

    # patient
    path("patients/", PatientListView.as_view(), name="patients"),
    path("patients/create", PatientCreateView.as_view(), name="create_pat"),
    path("patients/<pk>/update", PatientUpdateView.as_view(), name="update_pat"),
    path("patients/<pk>/delete", PatientDeleteView.as_view(), name="delete_pat"),
    path("patients/export/", export_patients, name="export_patients"),

]
