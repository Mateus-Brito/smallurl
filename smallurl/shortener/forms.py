from django import forms

from .models import Shortener


class ShortenerForm(forms.ModelForm):

    full_url = forms.URLField(
        error_messages={"required": "The link url field is required."},
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter the link here",
            }
        ),
    )

    class Meta:
        model = Shortener
        fields = ("full_url",)
