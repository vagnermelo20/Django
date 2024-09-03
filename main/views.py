from rest_framework import viewsets
from .models import Aluno, Professor, Diretor, Materia
from .serializers import AlunoSerializer, ProfessorSerializer, DiretorSerializer, MateriaSerializer

# Create your views here.
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset =Professor.objects.all()
    serializer_class = ProfessorSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset =Materia.objects.all()
    serializer_class = MateriaSerializer

class DiretorViewSet(viewsets.ModelViewSet):
    queryset =Diretor.objects.all()
    serializer_class = DiretorSerializer