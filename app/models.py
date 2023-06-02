from django.db import models


class BaseDatesModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time of creation")

    updated_at = models.DateTimeField(auto_now=True, help_text="Last update time")

    class Meta:
        abstract = True


class Doctor(BaseDatesModel):
    first_name = models.CharField(max_length=32, help_text="Имя")
    last_name = models.CharField(max_length=32, help_text="Фамилия")
    surname = models.CharField(max_length=32, help_text="Отчество")
    speciality = models.CharField(max_length=64, help_text="Специальность")
    phone_number = models.CharField(max_length=64, help_text="Номер телефона")
    email = models.EmailField()
    address = models.CharField(max_length=254, help_text="Адрес")

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.surname}"

    @property
    def short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.surname[0]}."

    class Meta:
        ordering = ("last_name",)
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    def __str__(self):
        return f"{self.short_name} — {self.speciality}"


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


class Appointment(BaseDatesModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    datetime = models.DateTimeField(help_text="Дата и время приема")

    class Meta:
        ordering = ("datetime",)
        verbose_name = "Прием у врача"
        verbose_name_plural = "Приемы у врачей"

    def __str__(self):
        return f"{self.doctor} - {self.patient.full_name}"


class Bill(BaseDatesModel):
    is_amount_insured = models.BooleanField(default=False)
    date_sent = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ("date_sent",)
        verbose_name = "Счет за прием"
        verbose_name_plural = "Счет за приемы"

    def __str__(self):
        return f"{self.amount}"


class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    class Meta:
        ordering = ("date",)
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.amount}"
