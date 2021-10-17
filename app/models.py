from django.db import models

# Create your models here.
class Paciente(models.Model):
    name = models.CharField("First name", max_length=255, blank = True, null = True)
    email = models.EmailField()
    subject = models.CharField("Subject", max_length=255, blank = True, null = True)
    message = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.name