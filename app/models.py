from distutils.command.upload import upload
from django.db import models

# Banco de dados Pacinete

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField("foto", upload_to='images/',blank = True, null = True)
    prontuario = models.CharField("Prontuario", max_length=255, blank = True, null = True)
    name = models.CharField("Nome", max_length=255, blank = False, null = True)
    responsavel = models.CharField("responsavel", max_length=255, blank = False, null = True)
    idade = models.DateField('idade', blank = False, null = True)
    rua = models.CharField("rua", max_length=255, blank = False, null = True)
    email = models.EmailField("email", max_length=255, blank = True, null = True)
    cpf = models.CharField("cpf", max_length=255, blank = False, null = True)
    message = models.TextField("mensagem",  blank=True, null=True)
    createdAt = models.DateTimeField("Criado em", auto_now_add=True)
    phone = models.CharField('Telefone', max_length=12, blank = False, null = True)
    cep = models.CharField("cep", max_length=255, blank = True, null = True)
    bairro = models.CharField("bairro", max_length=255, blank = True, null = True)
    cidade = models.CharField("cidade", max_length=255, blank = False, null = True)
    
    @property
    def get_photo_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        else:
            return "/media/images/user.jpg"

    def __str__(self):
        return self.name

# Banco de Dados do questionario vinculado com BD Paciente
class Questionario(models.Model):
    escolha = (('Sim', 'Sim'), ('Não', 'Não'))
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    um = models.CharField("Seu filho gosta de se balançar, de pular no seu joelho, etc?", max_length=10, choices=escolha, blank = True, null = True)
    dois = models.CharField("Seu filho tem interesse por outras crianças?", max_length=10, choices=escolha, blank = True, null = True)
    tres = models.CharField("Seu filho gosta de subir em coisas, como escadas ou móveis?", max_length=10, choices=escolha, blank = True, null = True)
    quatro = models.CharField("Seu filho gosta de brincar de esconder e mostrar o rosto ou de esconde-esconde?", max_length=10, choices=escolha, blank = True, null = True)
    cinco = models.CharField("Seu filho já brincou de faz-de-conta, como, por exemplo, fazer de conta que está falando no telefone ou que está cuidando da boneca, ou qualquer outra brincadeira de faz-de-conta?", max_length=10, choices=escolha, blank = True, null = True)
    seis = models.CharField("Seu filho já usou o dedo indicador dele para apontar, para pedir alguma coisa?", max_length=10, choices=escolha, blank = True, null = True)
    sete = models.CharField("Seu filho já usou o dedo indicador dele para apontar, para indicar interesse em algo?", max_length=10, choices=escolha, blank = True, null = True)
    oito = models.CharField("Seu filho consegue brincar de forma correta com brinquedos pequenos (ex. carros ou blocos), sem apenas colocar na boca, remexer no brinquedo ou deixar o brinquedo cair?", max_length=10, choices=escolha, blank = True, null = True)
    nove = models.CharField("O seu filho alguma vez trouxe objetos para você (pais) para lhe mostrar este objeto?", max_length=10, choices=escolha, blank = True, null = True)
    dez = models.CharField("O seu filho olha para você no olho por mais de um segundo ou dois?", max_length=10, choices=escolha, blank = True, null = True)
    onze = models.CharField("O seu filho já pareceu muito sensível ao barulho (ex. tapando os ouvidos)?", max_length=10, choices=escolha, blank = True, null = True)
    doze = models.CharField("O seu filho sorri em resposta ao seu rosto ou ao seu sorriso?", max_length=10, choices=escolha, blank = True, null = True)
    treze = models.CharField("O seu filho imita você? (ex. você faz expressões/caretas e seu filho imita)?", max_length=10, choices=escolha, blank = True, null = True)
    quatorze = models.CharField("O seu filho responde quando você chama ele pelo nome?", max_length=10, choices=escolha, blank = True, null = True)
    quinze = models.CharField("Se você aponta um brinquedo do outro lado do cômodo, o seu filho olha para ele?", max_length=10, choices=escolha, blank = True, null = True)
    desesseis = models.CharField("Seu filho já sabe andar?", max_length=10, choices=escolha, blank = True, null = True)
    desessete = models.CharField("O seu filho olha para coisas que você está olhando?", max_length=10, choices=escolha, blank = True, null = True)
    dezoito = models.CharField("O seu filho faz movimentos estranhos com os dedos perto do rosto dele?", max_length=10, choices=escolha, blank = True, null = True)
    dezenove = models.CharField("O seu filho tenta sua atenção para a atividade dele?", max_length=10, choices=escolha, blank = True, null = True)
    vinte = models.CharField("Você alguma vez já se perguntou se seu filho é surdo?", max_length=10, choices=escolha, blank = True, null = True)
    vinteum = models.CharField("O seu filho entende o que as pessoas dizem?", max_length=10, choices=escolha, blank = True, null = True)
    vintedois = models.CharField("O seu filho às vezes fica aéreo, “olhando para o nada” ou caminhando sem direção definida?", max_length=10, choices=escolha, blank = True, null = True)
    vintetres = models.CharField("O seu filho olha para o seu rosto para conferir a sua reação quando vê algo estranho?", max_length=10, choices=escolha, blank = True, null = True)

    

    def __str__(self):
        return self.paciente.name


# class FotoModel(models.Model):
#     paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#     foto = models.ImageField(upload_to = '')

#     def __str__(self):
#         return self.paciente.name

     
