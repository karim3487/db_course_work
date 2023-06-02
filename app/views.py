from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from openpyxl import Workbook

from app.forms import DoctorCreationForm
from app.models import Doctor
from common.views import TitleMixin


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class DoctorsListView(TitleMixin, ListView):
    model = Doctor
    template_name = "doctor/list.html"
    title = "Врачи"
    header = "Таблица с врачами"

    def get_queryset(self):
        queryset = super(DoctorsListView, self).get_queryset()
        return queryset.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DoctorsListView, self).get_context_data()
        return context


class DoctorCreateView(TitleMixin, CreateView):
    model = Doctor
    form_class = DoctorCreationForm
    template_name = "doctor/create.html"
    success_url = reverse_lazy('doc:doctors')
    title = "Добавление врача"


class DoctorUpdateView(TitleMixin, UpdateView):
    model = Doctor
    form_class = DoctorCreationForm
    title = "Изменение врача"
    template_name = 'doctor/update.html'
    success_url = reverse_lazy('doc:doctors')


class DoctorDeleteView(TitleMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy('doc:doctors')
    template_name = "doctor/confirm_delete.html"
    title = "Удаление врача"


def export_doctors(request):
    queryset = Doctor.objects.all()

    workbook = Workbook()
    sheet = workbook.active

    headers = ['ФИО', 'Специальность', 'Номер телефона', 'E-mail', 'Адрес']
    sheet.append(headers)

    for item in queryset:
        row = [item.full_name, item.speciality, item.phone_number, item.email, item.address]
        sheet.append(row)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=doctors.xlsx'

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
