from django.contrib import admin

from app.models import Doctor, Patient, InsuranceCompany, Payment, Bill

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(InsuranceCompany)
admin.site.register(Bill)
admin.site.register(Payment)
