from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form subscribe for email"""
    class Meta:
        model = Contact
        fields = '__all__'