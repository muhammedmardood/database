from django import forms
from django.forms import fields
from .models import Pdf

class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ("uploader",'pdf')