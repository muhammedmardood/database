from django.db import models


class Pdf(models.Model):
    name = models.CharField(max_length=100, null=False, default="No name")
    pdf = models.FileField(upload_to='files')
    uploader = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        return super().delete(*args, **kwargs)
