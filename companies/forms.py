import re

from django import forms

from companies.models import Offer, Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'email', 'phone', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'name': 'Company Name',
            'email': 'Company Email',
            'phone': 'Company Phone Number',
            'address': 'Company Address'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['name'].disabled = True

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()

        pattern = r'^\+?\d{7,15}$'

        if not re.match(pattern, phone):
            raise forms.ValidationError(
                'Enter a valid phone number: only digits allowed, '
                'and optional + at the beginning (7–15 digits total).'
            )

        return phone


class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = [
            'company',
            'title',
            'description',
            'pickup_location',
            'delivery_location',
            'price',
        ]

        widgets = {
            'company': forms.Select(attrs={
                'class': 'form-select',
            }),

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter offer title...'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe the load, cargo type, weight, special requirements...'
            }),

            'pickup_location': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'delivery_location': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price in EUR',
                'min': '0',
                'step': '1.00'
            }),
        }

        labels = {
            'company': 'Company',
            'title': 'Offer Title',
            'description': 'Offer Description',
            'pickup_location': 'Pickup Location',
            'delivery_location': 'Delivery Location',
            'price': 'Price (€)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['company'].disabled = True

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError('Price must be greater than 0.')
        return price