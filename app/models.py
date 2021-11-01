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

class Questionario(models.Model):
    escolha = (('Sim', 'Sim'), ('Não', 'Não'))
            
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,blank=True, null=True)
    um = models.CharField("um", max_length=10, choices=escolha)
    dois = models.CharField("dois", max_length=10, choices=escolha)
    tres = models.CharField("tres", max_length=10, choices=escolha)
    quatro = models.CharField("quatro", max_length=10, choices=escolha)
    cinco = models.CharField("cinco", max_length=10, choices=escolha)
    seis = models.CharField("seis", max_length=10, choices=escolha)
    sete = models.CharField("sete", max_length=10, choices=escolha)
    oito = models.CharField("oito", max_length=10, choices=escolha)
    nove = models.CharField("nove", max_length=10, choices=escolha)
    dez = models.CharField("dez", max_length=10, choices=escolha)
    onze = models.CharField("onze", max_length=10, choices=escolha)
    dose = models.CharField("dose", max_length=10, choices=escolha)
    treze = models.CharField("treze", max_length=10, choices=escolha)
    quatorze = models.CharField("quatorze", max_length=10, choices=escolha)
    quinze = models.CharField("quinze", max_length=10, choices=escolha)
    desesseis = models.CharField("desesseis", max_length=10, choices=escolha)
    desessete = models.CharField("desessete", max_length=10, choices=escolha)
    dezoito = models.CharField("dezoito", max_length=10, choices=escolha)
    dezenove = models.CharField("dezenove", max_length=10, choices=escolha)
    vinte = models.CharField("vinte", max_length=10, choices=escolha)
    vinteum = models.CharField("vinteum", max_length=10, choices=escolha)
    vintedois = models.CharField("vintedois", max_length=10, choices=escolha)
    vintetres = models.CharField("vintetres", max_length=10, choices=escolha)




     
