from django.db import models

# Create your models here.
class Materia(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    carga_horaria_HORAS = models.IntegerField(null=True, blank=True)
    professor = models.ManyToManyField('Professor', related_name='materias')
    def __str__(self):
        return self.nome

class Diretor(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=True)
    numero_telefonico = models.CharField(max_length=30, null=True, blank=True)
    email =  models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=True)
    numero_telefonico = models.CharField(max_length=30, null=True, blank=True)
    email =  models.EmailField(null=True, blank=True)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE, related_name= 'professores')
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=True)
    numero_telefonico = models.CharField(max_length=30, null=True, blank=True)
    email =  models.EmailField(null=True, blank=True)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE, related_name= 'alunos')
    materia = models.ManyToManyField(Materia, related_name= 'alunos')
    professores = models.ManyToManyField(Professor, related_name= 'alunos' )
    def __str__(self):
        return self.nome