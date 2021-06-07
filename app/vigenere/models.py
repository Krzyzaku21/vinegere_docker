from django.db import models
from django.core.exceptions import ValidationError


class EncryptVigenere(models.Model):
    plain_text = models.CharField(max_length=25, blank=False, null=False)
    plain_key = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.plain_text


class DecryptVigenere(models.Model):
    encrypt_text = models.CharField(max_length=25, blank=False)
    plain_key = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.encrypt_text
