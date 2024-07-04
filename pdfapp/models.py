from django.db import models

# Create your models here.


# class UploadedPDF(models.Model):
#     file = models.FileField(upload_to='uploads/')



class UploadedPDF(models.Model):
    file = models.FileField(upload_to='uploads/')

    class Meta:
        app_label = 'pdfapp'
