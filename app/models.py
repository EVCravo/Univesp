from django.db import models

# Create your models here.
class Paciente(models.Model):
    name = models.CharField("Nome", max_length=255, blank = True, null = True)
    responsavel = models.CharField("responsavel", max_length=255, blank = True, null = True)
    idade = models.DateField('idade', blank = True, null = True)
    address = models.CharField("Endereço", max_length=255, blank = True, null = True)
    email = models.EmailField()
    message = models.TextField("mensagem",  blank=True, null=True)
    createdAt = models.DateTimeField("Criado em", auto_now_add=True)
    phone = models.CharField('Telefone', max_length=12, blank = True, null = True)

    def __str__(self):
        return self.name