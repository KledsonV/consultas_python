from django.db import models

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"{self.paciente} - {self.medico} em {self.data} às {self.horario}"


class Medico(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
    

class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome