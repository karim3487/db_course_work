from django import forms

from app.models import Doctor, InsuranceCompany, Patient


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
