from django import forms

from common.models import OfferComment, AvailabilityComment
from companies.models import Company
from drivers.models import Driver


class OfferCommentForm(forms.ModelForm):

    driver = forms.ModelChoiceField(
        queryset=Driver.objects.all(),
        empty_label='Select Driver',
        widget=forms.Select(attrs={
            'class': 'form-select'
            })
    )

    class Meta:
        model = OfferComment
        fields = ['driver', 'message']

        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your message...'
            }),
        }


class AvailabilityCommentForm(forms.ModelForm):

    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        empty_label='Select Company',
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    class Meta:
        model = AvailabilityComment
        fields = ['company', 'message']

        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your message...'
            }),
        }