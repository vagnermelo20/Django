from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, ProfessorViewSet, DiretorViewSet, MateriaViewSet
from . import views

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'diretores', DiretorViewSet)
router.register(r'Materias', MateriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]