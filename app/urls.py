from django.urls import path

from . import views
from .views import (
    DoctorCreateView,
    DoctorListView,
    export_doctors,
    DoctorDeleteView,
    DoctorUpdateView,
    PatientListView,
    PatientCreateView,
    PatientUpdateView,
    PatientDeleteView,
    export_patients,
    InsuranceCompanyListView,
    InsuranceCompanyCreateView,
    InsuranceCompanyUpdateView,
    InsuranceCompanyDeleteView,
    export_ins_companies,
    BillPaymentListView,
    export_bill_payments,
    BillListView,
    BillCreateView,
    BillUpdateView,
    BillDeleteView,
    export_bills,
    AppointmentListView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
    export_appointments,
    PaymentListView,
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    export_payments,
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
    # insurance_company
    path(
        "insurance-companies/", InsuranceCompanyListView.as_view(), name="ins_companies"
    ),
    path(
        "insurance-companies/create",
        InsuranceCompanyCreateView.as_view(),
        name="create_ins_company",
    ),
    path(
        "insurance-companies/<pk>/update",
        InsuranceCompanyUpdateView.as_view(),
        name="update_ins_company",
    ),
    path(
        "insurance-companies/<pk>/delete",
        InsuranceCompanyDeleteView.as_view(),
        name="delete_ins_company",
    ),
    path(
        "insurance-companies/export/", export_ins_companies, name="export_ins_companies"
    ),
    # appointment
    path("appointments/", AppointmentListView.as_view(), name="appointments"),
    path("appointments/reg", views.registration_view, name="reg_app"),
    path("ajax/load-doctors", views.load_doctors, name="ajax_load_doctors"),
    path("ajax/load-talons", views.load_talons, name="ajax_load_talons"),
    path("appointments/create", AppointmentCreateView.as_view(), name="create_app"),
    path(
        "appointments/<pk>/update", AppointmentUpdateView.as_view(), name="update_app"
    ),
    path(
        "appointments/<pk>/delete", AppointmentDeleteView.as_view(), name="delete_app"
    ),
    path("appointments/export/", export_appointments, name="export_appointments"),
    # bill
    path("bills/", BillListView.as_view(), name="bills"),
    path("bills/create", BillCreateView.as_view(), name="create_bill"),
    path("bills/<pk>/update", BillUpdateView.as_view(), name="update_bill"),
    path("bills/<pk>/delete", BillDeleteView.as_view(), name="delete_bill"),
    path("bills/export/", export_bills, name="export_bills"),
    # payment
    path("payments/", PaymentListView.as_view(), name="payments"),
    path("payments/create", PaymentCreateView.as_view(), name="create_payment"),
    path("payments/<pk>/update", PaymentUpdateView.as_view(), name="update_payment"),
    path("payments/<pk>/delete", PaymentDeleteView.as_view(), name="delete_payment"),
    path("payments/export/", export_payments, name="export_payments"),
    # bill_payment
    path("bill-payments/", BillPaymentListView.as_view(), name="bill-payments"),
    path("bill-payments/export/", export_bill_payments, name="export_bill_payments"),
]
