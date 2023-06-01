from django.urls import path

from . import views
from .views import DoctorCreateView, DoctorsListView

app_name = "doc"

urlpatterns = [
    path("", views.index, name="index"),
    # path("doctors/", views.doctor_list, name="doctors"),
    path("doctors/", DoctorsListView.as_view(), name="doctors"),
    path("doctors/create", DoctorCreateView.as_view(), name="create_doc"),
]
