from django import forms


class LinkForm(forms.Form):
    full_link = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input your link for shortener',
        'aria-label': "Recipient's",
        'aria-describedby': 'button-addon2'
    }))
    designed_link = forms.CharField(max_length=20, min_length=6, required=False,
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Enter which link you would like'
                                    }))
