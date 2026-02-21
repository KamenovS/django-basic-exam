import re

from django import forms
from django.utils import timezone
from drivers.models import Driver, DriverAvailability


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'category', 'email', 'phone', 'trailer_type']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter driver`s name'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select',
            }),

            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter driver`s email'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter driver`s phone number'
            }),

            'trailer_type': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['name'].disabled = True

        self.fields['category'].choices = [
            choice for choice in self.fields['category'].choices if choice[0] != ''
        ]
        self.fields['trailer_type'].choices = [
            choice for choice in self.fields['trailer_type'].choices if choice[0] != ''
        ]

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()

        pattern = r'^\+?\d{7,15}$'

        if not re.match(pattern, phone):
            raise forms.ValidationError(
                'Enter a valid phone number: only digits allowed, '
                'and optional + at the beginning (7–15 digits total).'
            )

        return phone


class DriverAvailabilityForm(forms.ModelForm):
    class Meta:
        model = DriverAvailability
        fields = ['driver', 'current_location', 'available_from', 'description']

        widgets = {
            'driver': forms.Select(attrs={
                'class': 'form-select',
            }),

            'current_location': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'available_from': forms.DateInput(attrs={
                    'type': 'date',
                    'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['driver'].disabled = True

        self.fields['driver'].choices = [
            choice for choice in self.fields['driver'].choices if choice[0] != ''
        ]

    def clean_available_from(self):
        available_from = self.cleaned_data.get('available_from')
        today = timezone.now().date()

        if available_from < today:
            raise forms.ValidationError('Available date cannot be earlier than today.')

        return available_from