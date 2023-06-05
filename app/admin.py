from django.contrib import admin

from app import models
admin.site.register(models.Specialty)
admin.site.register(models.Schedule)
admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.InsuranceCompany)
admin.site.register(models.Bill)
admin.site.register(models.Payment)
admin.site.register(models.Appointment)
