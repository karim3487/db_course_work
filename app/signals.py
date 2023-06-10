import datetime

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from datetime import timedelta

from .models import Schedule, Talon, Appointment


@receiver(post_save, sender=Schedule)
def generate_talons_for_schedule(sender, instance, created, **kwargs):
    if created:
        schedule = instance
        day_of_week = schedule.day_of_week

        today = datetime.date.today()
        offset = (day_of_week - today.weekday()) % 7

        next_weekday = today + timedelta(days=offset)
        weekdays = [next_weekday + timedelta(weeks=i) for i in range(4)]

        doctor = schedule.doctor

        for weekday in weekdays:
            current_time = schedule.start_time
            while current_time < schedule.end_time:
                talon = Talon.objects.create(
                    doctor=doctor,
                    date=weekday,
                    time=current_time,
                )
                current_datetime = datetime.datetime.combine(weekday, current_time)
                current_datetime += timedelta(minutes=30)
                current_time = current_datetime.time()


@receiver(post_delete, sender=Appointment)
def clean_talon_data(sender, instance, **kwargs):
    appointment = instance
    talons = Talon.objects.filter(
        doctor=appointment.doctor,
        patient=appointment.patient,
        date=appointment.date,
        time=appointment.time
    )

    if len(talons) == 1:
        talons[0].patient = None
        talons[0].save()
    else:
        print("len of talons", len(talons))
