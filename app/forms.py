from django import forms

from app.models import Doctor


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
