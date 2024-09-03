from rest_framework import serializers
from .models import  Materia, Aluno, Professor, Diretor

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'numero_telefonico', 'email']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'nome', 'numero_telefonico', 'email']

class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = ['id', 'nome', 'numero_telefonico', 'email']

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ['id', 'nome', 'carga_horaria_HORAS']