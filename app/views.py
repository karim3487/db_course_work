from django.db.models import Sum, F
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from openpyxl import Workbook

from app.forms import (
    DoctorCreationForm,
    PatientCreationForm,
    InsuranceCompanyCreationForm,
)
from app.models import Doctor, Patient, InsuranceCompany, Bill, Payment
from common.views import TitleMixin


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# DOCTOR:---------------------------------------------------------------------------------------------------------------
class DoctorListView(TitleMixin, ListView):
    model = Doctor
    template_name = "doctor/list.html"
    title = "Врачи"
    header = "Таблица с врачами"

    def get_queryset(self):
        queryset = super(DoctorListView, self).get_queryset()
        return queryset.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DoctorListView, self).get_context_data()
        return context


class DoctorCreateView(TitleMixin, CreateView):
    model = Doctor
    form_class = DoctorCreationForm
    template_name = "doctor/create.html"
    success_url = reverse_lazy("hospital:doctors")
    title = "Добавление врача"


class DoctorUpdateView(TitleMixin, UpdateView):
    model = Doctor
    form_class = DoctorCreationForm
    title = "Изменение врача"
    template_name = "doctor/update.html"
    success_url = reverse_lazy("hospital:doctors")


class DoctorDeleteView(TitleMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy("hospital:doctors")
    template_name = "confirm_delete.html"
    title = "Удаление врача"


def export_doctors(request):
    queryset = Doctor.objects.all()

    workbook = Workbook()
    sheet = workbook.active

    headers = ["ФИО", "Специальность", "Номер телефона", "E-mail", "Адрес"]
    sheet.append(headers)

    for item in queryset:
        row = [
            item.full_name,
            item.speciality,
            item.phone_number,
            item.email,
            item.address,
        ]
        sheet.append(row)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=doctors.xlsx"

    workbook.save(response)

    return response


# PATIENT:--------------------------------------------------------------------------------------------------------------
class PatientListView(TitleMixin, ListView):
    model = Patient
    template_name = "patient/list.html"
    title = "Пациенты"
    header = "Таблица с пациентами"

    def get_queryset(self):
        queryset = super(PatientListView, self).get_queryset()
        return queryset.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PatientListView, self).get_context_data()
        return context


class PatientCreateView(TitleMixin, CreateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = "patient/create.html"
    success_url = reverse_lazy("hospital:patients")
    title = "Добавление пациента"


class PatientUpdateView(TitleMixin, UpdateView):
    model = Patient
    form_class = PatientCreationForm
    title = "Изменение пациента"
    template_name = "patient/update.html"
    success_url = reverse_lazy("hospital:patients")


class PatientDeleteView(TitleMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy("hospital:patients")
    template_name = "confirm_delete.html"
    title = "Удаление пациента"


def export_patients(request):
    queryset = Patient.objects.all()

    workbook = Workbook()
    sheet = workbook.active

    headers = ["ФИО", "Номер телефона", "Адрес", "Страховая компания"]
    sheet.append(headers)

    for item in queryset:
        row = [
            item.full_name,
            item.phone_number,
            item.address,
            item.insurance_company.name if item.insurance_company else "Не застрахован",
        ]
        sheet.append(row)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=patients.xlsx"

    workbook.save(response)

    return response


# INS_COMPANIES---------------------------------------------------------------------------------------------------------
class InsuranceCompanyListView(TitleMixin, ListView):
    model = InsuranceCompany
    template_name = "ins_company/list.html"
    title = "Страховые компании"
    header = "Таблица со страховыми компаниями"

    def get_queryset(self):
        queryset = super(InsuranceCompanyListView, self).get_queryset()
        return queryset.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InsuranceCompanyListView, self).get_context_data()
        return context


class InsuranceCompanyCreateView(TitleMixin, CreateView):
    model = InsuranceCompany
    form_class = InsuranceCompanyCreationForm
    template_name = "ins_company/create.html"
    success_url = reverse_lazy("hospital:ins_companies")
    title = "Добавление страховой компании"


class InsuranceCompanyUpdateView(TitleMixin, UpdateView):
    model = InsuranceCompany
    form_class = InsuranceCompanyCreationForm
    title = "Изменение страховой компании"
    template_name = "ins_company/update.html"
    success_url = reverse_lazy("hospital:ins_companies")


class InsuranceCompanyDeleteView(TitleMixin, DeleteView):
    model = InsuranceCompany
    success_url = reverse_lazy("hospital:ins_companies")
    template_name = "confirm_delete.html"
    title = "Удаление страховой компании"


def export_ins_companies(request):
    queryset = InsuranceCompany.objects.all()

    workbook = Workbook()
    sheet = workbook.active

    headers = ["Название", "Номер телефона", "Адрес"]
    sheet.append(headers)

    for item in queryset:
        row = [
            item.name,
            item.phone_number,
            item.address,
        ]
        sheet.append(row)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=companies.xlsx"

    workbook.save(response)

    return response


# BILL_PAYMENTS:--------------------------------------------------------------------------------------------------------
class BillPaymentListView(TitleMixin, ListView):
    template_name = "bill_payments/list.html"
    context_object_name = "bill_payments"
    title = "Счета"
    header = "Таблица с счетами"

    def get_queryset(self):
        queryset = Bill.objects.annotate(total_payment=Sum("payment__amount")).annotate(
            balance=F("amount") - F("total_payment")
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_payment_sum = Payment.objects.aggregate(total=Sum("amount"))["total"]
        context["total_payment_sum"] = total_payment_sum
        return context


def export_bill_payments(request):
    queryset = Bill.objects.annotate(total_payment=Sum("payment__amount")).annotate(
        balance=F("amount") - F("total_payment")
    )
    total_payment_sum = Payment.objects.aggregate(total=Sum("amount"))["total"]

    workbook = Workbook()
    sheet = workbook.active

    headers = ["Сумма", "Дата отправки", "Общая сумма платежей", "Остаток"]
    sheet.append(headers)

    for item in queryset:
        row = [
            item.amount,
            item.date_sent,
            item.total_payment,
            item.balance if item.balance > 0 else "Оплачено"
        ]
        sheet.append(row)

    sheet.append(["Всего заработано", total_payment_sum])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=bill_payments.xlsx"

    workbook.save(response)

    return response

# def patient_list(request):
#     patients = Patient.objects.all()
#     return render(request, 'patient_list.html', {'patients': patients})
#
#
# def patient_detail(request, patient_id):
#     patient = get_object_or_404(Patient, id=patient_id)
#     return render(request, 'patient_detail.html', {'patient': patient})
#
#
# def appointment_list(request):
#     appointments = Appointment.objects.all()
#     return render(request, 'appointment_list.html', {'appointments': appointments})
#
#
# def appointment_detail(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id)
#     return render(request, 'appointment_detail.html', {'appointment': appointment})
#
#
# def bill_list(request):
#     bills = Bill.objects.all()
#     return render(request, 'bill_list.html', {'bills': bills})
