from django import forms
from app import models
from tempus_dominus.widgets import DatePicker


class DoctorCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-2", "placeholder": "Введите имя"}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-2", "placeholder": "Введите фамилию"}
        )
    )

    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-2", "placeholder": "Введите отчество"}
        )
    )

    specialty = forms.ModelChoiceField(
        queryset=models.Specialty.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите специальность",
            }
        ),
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите номер телефона",
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите адрес эл. почты",
            }
        )
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите адрес проживания",
            }
        )
    )

    class Meta:
        model = models.Doctor
        fields = (
            "first_name",
            "last_name",
            "surname",
            "specialty",
            "phone_number",
            "email",
            "address",
        )


class PatientCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-2", "placeholder": "Введите имя"}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-2", "placeholder": "Введите фамилию"}
        )
    )

    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-2", "placeholder": "Введите отчество"}
        )
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите номер телефона",
            }
        )
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите адрес проживания",
            }
        )
    )

    insurance_company = forms.ModelChoiceField(
        queryset=models.InsuranceCompany.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите страховую компанию",
            }
        ),
    )

    class Meta:
        model = models.Patient
        fields = (
            "first_name",
            "last_name",
            "surname",
            "phone_number",
            "address",
            "insurance_company",
        )


class InsuranceCompanyCreationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите название компании",
            }
        )
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите номер телефона",
            }
        )
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите адрес",
            }
        )
    )

    class Meta:
        model = models.InsuranceCompany
        fields = (
            "name",
            "phone_number",
            "address",
        )


class SpecialtyForm(forms.ModelForm):
    specialty = forms.ModelChoiceField(
        queryset=models.Specialty.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите специальность",
            }
        ),
    )


class AppointmentCreationForm(forms.Form):
    patient = forms.ModelChoiceField(
        queryset=models.Patient.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите пациента",
            }
        ),
    )

    specialty = forms.ModelChoiceField(
        queryset=models.Specialty.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите специальность",
            }
        ),
    )

    doctor = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите доктора",
            }
        ),
    )

    talon = forms.ModelChoiceField(
        queryset=models.Talon.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите доктора",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["doctor"].queryset = models.Doctor.objects.none()
        self.fields["talon"].queryset = models.Talon.objects.none()

    class Meta:
        fields = ("doctor", "patient", "specialty")


class BillCreationForm(forms.ModelForm):
    appointment = forms.ModelChoiceField(
        queryset=models.Appointment.objects.filter(bill__isnull=True),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите прием",
            }
        ),
    )

    amount = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите счет за прием",
            }
        )
    )

    class Meta:
        model = models.Bill
        fields = (
            "appointment",
            "amount",
        )


class PaymentCreationForm(forms.ModelForm):
    bill = forms.ModelChoiceField(
        queryset=models.Bill.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите страховую копанию",
            }
        ),
    )

    amount = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Введите счет за прием",
            }
        )
    )

    date = forms.DateField(
        widget=DatePicker(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Выберите дату",
            }
        )
    )

    class Meta:
        model = models.Payment
        fields = (
            "bill",
            "amount",
            "date",
        )
