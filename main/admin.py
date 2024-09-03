from django.contrib import admin
from .models import Aluno, Professor, Materia, Diretor


# Register your models here.
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Materia)
admin.site.register(Diretor)