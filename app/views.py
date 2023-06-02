from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from openpyxl import Workbook

from app.forms import DoctorCreationForm, PatientCreationForm
from app.models import Doctor, Patient
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
    success_url = reverse_lazy("hospital:doctors")


class PatientDeleteView(TitleMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy("hospital:doctors")
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
            item.insurance_company.name if item.insurance_company else "Не застрахован"
        ]
        sheet.append(row)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=patients.xlsx"

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