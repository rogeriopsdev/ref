from django import forms
from refeitorioApp.models import Curso,Matricula,Aluno,Acesso,Refeicao,Turno


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso']

class MatriculaForm(forms.ModelForm):
    class Meta:
        model =Matricula
        fields= ['num_matricula','id_aluno','id_curso','id_turno']


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_aluno','cpf_aluno','foto_aluno']


class AcessoForm(forms.ModelForm):
    class Meta:
        model =Acesso
        fields = ['nome_acesso','data_acesso','id_aluno','id_ref']


class RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = ['nome_ref']


class TurnoForm(forms.ModelForm):
    class Meta:
        model= Turno
        fields=['nome_turno']
