from django import forms
from .models import Link


class LinkForm(forms.Form):
    full_link = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input your link for shortener',
            'aria-label': "Recipient's",
            'aria-describedby': 'button-addon2'
        })
    )
    designed_link = forms.CharField(
        max_length=20,
        min_length=6,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter which link you would like'
        })
    )


class LinkModelForm(forms.ModelForm):
    full_link = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'form-control my-2',
            'placeholder': 'Input your link for shortener',
            'readonly': ''
        })
    )
    short_link = forms.CharField(
        max_length=6,
        min_length=6,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter which link you would like'
        })
    )
    designed_link = forms.CharField(
        max_length=20,
        min_length=6,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter which link you would like2'
        })
    )

    class Meta:
        model = Link
        fields = ('full_link', 'short_link', 'designed_link')
