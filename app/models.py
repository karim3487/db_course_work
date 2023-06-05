from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseDatesModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time of creation")

    updated_at = models.DateTimeField(auto_now=True, help_text="Last update time")

    class Meta:
        abstract = True


class Specialty(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.name


class Schedule(models.Model):
    class DayOfWeeks(models.IntegerChoices):
        MONDAY = 0, _("Понедельник")
        TUESDAY = 1, _("Вторник")
        WEDNESDAY = 2, _("Среда")
        THURSDAY = 3, _("Четверг")
        FRIDAY = 4, _("Пятница")
        SATURDAY = 5, _("Суббота")
        SUNDAY = 6, _("Воскресенье")

    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DayOfWeeks.choices, default=DayOfWeeks.MONDAY)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ("doctor",)
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"

    def __str__(self):
        return f"{self.doctor.short_name}, {self.get_day_of_week_display()}"


class Doctor(BaseDatesModel):
    first_name = models.CharField(max_length=32, help_text="Имя")
    last_name = models.CharField(max_length=32, help_text="Фамилия")
    surname = models.CharField(max_length=32, help_text="Отчество")
    specialty = models.ForeignKey("Specialty", on_delete=models.RESTRICT, help_text="Специальность")
    phone_number = models.CharField(max_length=64, help_text="Номер телефона")
    email = models.EmailField()
    address = models.CharField(max_length=254, help_text="Адрес")

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.surname}"

    @property
    def short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.surname[0]}."

    @property
    def get_specialty(self):
        return self.specialty.name

    class Meta:
        ordering = ("last_name",)
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    def __str__(self):
        return f"{self.short_name}, {self.get_specialty}"


class InsuranceCompany(BaseDatesModel):
    name = models.CharField(max_length=128, help_text="Название компании")
    phone_number = models.CharField(max_length=128, help_text="Номер телефона")
    address = models.CharField(max_length=254, help_text="Адрес страховой компании")

    class Meta:
        ordering = ("name",)
        verbose_name = "Страховая компания"
        verbose_name_plural = "Страховые компании"

    def __str__(self):
        return f"{self.name}"


class Patient(BaseDatesModel):
    first_name = models.CharField(max_length=32, help_text="Имя")
    last_name = models.CharField(max_length=32, help_text="Фамилия")
    surname = models.CharField(max_length=32, help_text="Отчество")
    phone_number = models.CharField(max_length=64, help_text="Номер")
    address = models.CharField(max_length=254, help_text="Адрес")
    insurance_company = models.ForeignKey(
        "InsuranceCompany",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Страховая компания, в которой зарегистрирован пациент (необязательное)",
    )

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.surname}"

    @property
    def short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.surname[0]}."

    class Meta:
        ordering = ("last_name",)
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def __str__(self):
        return f"{self.short_name}"


class Appointment(models.Model):
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date = models.DateField(help_text="Дата приема")
    time = models.TimeField(help_text="Время приема")

    class Meta:
        verbose_name = "Прием у врача"
        verbose_name_plural = "Приемы у врачей"

    def __str__(self):
        return f"{self.doctor} — {self.patient}"


class Bill(models.Model):
    appointment = models.OneToOneField(
        "Appointment", on_delete=models.CASCADE, related_name="bill", default=None
    )
    is_amount_insured = models.BooleanField(default=False)
    date_sent = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ("date_sent",)
        verbose_name = "Счет за прием"
        verbose_name_plural = "Счета за приемы"

    def __str__(self):
        return f"{self.appointment.doctor} - {self.appointment.patient} - {self.amount}"


class Payment(models.Model):
    patient = models.ForeignKey(
        "Patient", null=True, blank=True, on_delete=models.CASCADE, related_name="payment"
    )
    insurance_company = models.ForeignKey(
        "InsuranceCompany",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="payment",
    )
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    class Meta:
        ordering = ("date",)
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.amount}"
