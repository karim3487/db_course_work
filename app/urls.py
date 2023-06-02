from django.urls import path

from . import views
from .views import DoctorCreateView, DoctorsListView, export_doctors, DoctorDeleteView, DoctorUpdateView

app_name = "doc"

urlpatterns = [
    path("", views.index, name="index"),
    path("doctors/", DoctorsListView.as_view(), name="doctors"),
    path("doctors/create", DoctorCreateView.as_view(), name="create_doc"),
    path("doctors/<pk>/update", DoctorUpdateView.as_view(), name="update_doc"),
    path('doctors/<pk>/delete', DoctorDeleteView.as_view(), name='delete_doc'),
    path('doctors/export/', export_doctors, name='export_doctors'),
]
