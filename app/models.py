from django.db import models

# Create your models here.
class Paciente(models.Model):
    prontuario = models.CharField("Prontuario", max_length=255, blank = True, null = True)
    name = models.CharField("Nome", max_length=255, blank = True, null = True)
    responsavel = models.CharField("responsavel", max_length=255, blank = True, null = True)
    idade = models.DateField('idade', blank = True, null = True)
    address = models.CharField("Endereço", max_length=255, blank = True, null = True)
    email = models.EmailField()
    cpf = models.CharField("cpf", max_length=255, blank = True, null = True)
    message = models.TextField("mensagem",  blank=True, null=True)
    createdAt = models.DateTimeField("Criado em", auto_now_add=True)
    phone = models.CharField('Telefone', max_length=12, blank = True, null = True)

    def __str__(self):
        return self.name

class Questionario(models.Model):
    escolha = (('Sim', 'Sim'), ('Não', 'Não'))
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    um = models.CharField("um", max_length=10, choices=escolha, blank = True, null = True)
    dois = models.CharField("dois", max_length=10, choices=escolha, blank = True, null = True)
    tres = models.CharField("tres", max_length=10, choices=escolha, blank = True, null = True)
    quatro = models.CharField("quatro", max_length=10, choices=escolha, blank = True, null = True)
    cinco = models.CharField("cinco", max_length=10, choices=escolha, blank = True, null = True)
    seis = models.CharField("seis", max_length=10, choices=escolha, blank = True, null = True)
    sete = models.CharField("sete", max_length=10, choices=escolha, blank = True, null = True)
    oito = models.CharField("oito", max_length=10, choices=escolha, blank = True, null = True)
    nove = models.CharField("nove", max_length=10, choices=escolha, blank = True, null = True)
    dez = models.CharField("dez", max_length=10, choices=escolha, blank = True, null = True)
    onze = models.CharField("onze", max_length=10, choices=escolha, blank = True, null = True)
    dose = models.CharField("dose", max_length=10, choices=escolha, blank = True, null = True)
    treze = models.CharField("treze", max_length=10, choices=escolha, blank = True, null = True)
    quatorze = models.CharField("quatorze", max_length=10, choices=escolha, blank = True, null = True)
    quinze = models.CharField("quinze", max_length=10, choices=escolha, blank = True, null = True)
    desesseis = models.CharField("desesseis", max_length=10, choices=escolha, blank = True, null = True)
    desessete = models.CharField("desessete", max_length=10, choices=escolha, blank = True, null = True)
    dezoito = models.CharField("dezoito", max_length=10, choices=escolha, blank = True, null = True)
    dezenove = models.CharField("dezenove", max_length=10, choices=escolha, blank = True, null = True)
    vinte = models.CharField("vinte", max_length=10, choices=escolha, blank = True, null = True)
    vinteum = models.CharField("vinteum", max_length=10, choices=escolha, blank = True, null = True)
    vintedois = models.CharField("vintedois", max_length=10, choices=escolha, blank = True, null = True)
    vintetres = models.CharField("vintetres", max_length=10, choices=escolha, blank = True, null = True)

    

    def __str__(self):
        return self.paciente.name




     
