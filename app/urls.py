from django.urls import path

from . import views

app_name = "hospital"

urlpatterns = [
    path("", views.index, name="index"),
    # doctor
    path("doctors/", views.DoctorListView.as_view(), name="doctors"),
    path("doctors/create", views.DoctorCreateView.as_view(), name="create_doc"),
    path("doctors/<pk>/update", views.DoctorUpdateView.as_view(), name="update_doc"),
    path("doctors/<pk>/delete", views.DoctorDeleteView.as_view(), name="delete_doc"),
    path("doctors/export/", views.export_doctors, name="export_doctors"),
    # patient
    path("patients/", views.PatientListView.as_view(), name="patients"),
    path("patients/create", views.PatientCreateView.as_view(), name="create_pat"),
    path("patients/<pk>/update", views.PatientUpdateView.as_view(), name="update_pat"),
    path("patients/<pk>/delete", views.PatientDeleteView.as_view(), name="delete_pat"),
    path("patients/export/", views.export_patients, name="export_patients"),
    # insurance_company
    path(
        "insurance-companies/", views.InsuranceCompanyListView.as_view(), name="ins_companies"
    ),
    path(
        "insurance-companies/create",
        views.InsuranceCompanyCreateView.as_view(),
        name="create_ins_company",
    ),
    path(
        "insurance-companies/<pk>/update",
        views.InsuranceCompanyUpdateView.as_view(),
        name="update_ins_company",
    ),
    path(
        "insurance-companies/<pk>/delete",
        views.InsuranceCompanyDeleteView.as_view(),
        name="delete_ins_company",
    ),
    path(
        "insurance-companies/export/", views.export_ins_companies, name="export_ins_companies"
    ),
    # specialty
    path("appointments/select-specialty", views.SpecialtySelectView.as_view(), name="select_spec"),
    # appointment
    path("appointments/", views.AppointmentListView.as_view(), name="appointments"),
    path("appointments/create", views.AppointmentCreateView.as_view(), name="create_app"),
    path(
        "appointments/<pk>/update", views.AppointmentUpdateView.as_view(), name="update_app"
    ),
    path(
        "appointments/<pk>/delete", views.AppointmentDeleteView.as_view(), name="delete_app"
    ),
    path("appointments/export/", views.export_appointments, name="export_appointments"),
    # bill
    path("bills/", views.BillListView.as_view(), name="bills"),
    path("bills/create", views.BillCreateView.as_view(), name="create_bill"),
    path("bills/<pk>/update", views.BillUpdateView.as_view(), name="update_bill"),
    path("bills/<pk>/delete", views.BillDeleteView.as_view(), name="delete_bill"),
    path("bills/export/", views.export_bills, name="export_bills"),
    # payment
    path("payments/", views.PaymentListView.as_view(), name="payments"),
    path("payments/create", views.PaymentCreateView.as_view(), name="create_payment"),
    path("payments/<pk>/update", views.PaymentUpdateView.as_view(), name="update_payment"),
    path("payments/<pk>/delete", views.PaymentDeleteView.as_view(), name="delete_payment"),
    path("payments/export/", views.export_payments, name="export_payments"),
    # bill_payment
    path("bill-payments/", views.BillPaymentListView.as_view(), name="bill-payments"),
    path("bill-payments/export/", views.export_bill_payments, name="export_bill_payments"),
]
