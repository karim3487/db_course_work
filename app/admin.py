from django.contrib import admin

from app.models import Doctor, Patient, InsuranceCompany

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(InsuranceCompany)
