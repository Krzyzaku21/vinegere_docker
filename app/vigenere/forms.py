from django import forms
from .models import EncryptVigenere, DecryptVigenere


class EncryptVigenereForm(forms.ModelForm):
    class Meta:
        model = EncryptVigenere
        fields = ['plain_text', 'plain_key', ]


class DecryptVigenereForm(forms.ModelForm):
    class Meta:
        model = DecryptVigenere
        fields = ['encrypt_text', 'plain_key', ]
