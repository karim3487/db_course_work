from django import forms

from app.models import Doctor, InsuranceCompany, Patient, Appointment, Bill
from tempus_dominus.widgets import DateTimePicker, DatePicker


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

    speciality = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-2", "placeholder": "Введите специальность"}
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
        model = Doctor
        fields = (
            "first_name",
            "last_name",
            "surname",
            "speciality",
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
        queryset=InsuranceCompany.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите страховую компанию",
            }
        ),
    )

    class Meta:
        model = Patient
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
        model = InsuranceCompany
        fields = (
            "name",
            "phone_number",
            "address",
        )


class AppointmentCreationForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите доктора",
            }
        ),
    )

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите пациента",
            }
        ),
    )

    datetime = forms.DateTimeField(
        widget=DateTimePicker(
            attrs={
                "class": "form-control py-2",
                "placeholder": "Выберите время и дату",
            }
        )
    )

    class Meta:
        model = Appointment
        fields = (
            "doctor",
            "patient",
            "datetime",
        )


class BillCreationForm(forms.ModelForm):
    appointment = forms.ModelChoiceField(
        queryset=Appointment.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select py-2",
                "placeholder": "Выберите прием",
            }
        ),
    )

    is_amount_insured = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "placeholder": "Введите номер телефона",
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
        model = Bill
        fields = (
            "appointment",
            "is_amount_insured",
            "amount",
        )
