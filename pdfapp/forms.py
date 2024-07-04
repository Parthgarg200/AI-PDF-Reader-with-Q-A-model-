from django import forms
from .models import UploadedPDF
#from pdfapp.views import upload_pdf

# class UploadPDFForm(forms.Form):
#     file=forms.FileField()




class UploadPDFForm(forms.ModelForm):
    class Meta:
        model = UploadedPDF
        fields = ['file']
