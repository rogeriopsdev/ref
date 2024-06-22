from PIL import Image
from django.db import models

# Create your models here.
# class Matricula(models.Model):
# class Curso(models.Model):
# class Turno(models.Model):
class Curso(models.Model):
    id_curso =models.AutoField(primary_key=True)
    nome_curso =models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome_curso

class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    nome_turno = models.CharField(max_length=255,null=False,blank=False)

    def __str__(self):
        return self.nome_turno



class Aluno(models.Model):
    id_aluno=models.AutoField(primary_key=True)
    nome_aluno =models.CharField(max_length=255,null=False, blank=False)
    #matricula_aluno =models.CharField(max_length=255,null=False, blank=False)
    #curso_aluno =models.CharField(max_length=255,null=False, blank=False)
    #turno_aluno =models.CharField(max_length=255,null=False, blank=False)
    cpf_aluno =models.CharField(max_length=255,null=False, blank=False)
    foto_aluno = models.ImageField(blank=True, null=False)

    def save(self):
        super().save()
        im = Image.open(self.foto_aluno.path)
        novo_tamanho = (40, 40)
        im.thumbnail(novo_tamanho)
        im.save(self.foto_aluno.path)

    def foto_url(self):
        if self.foto_aluno and hasattr(self.foto_aluno, 'url'):
            return self.foto_aluno.url
        else:
            return self.nome_aluno

    def __str__(self):
        return self.nome_aluno

class Matricula(models.Model):
    id_matricula =models.AutoField(primary_key=True)
    num_matricula = models.CharField(max_length=255,null=False,blank=False)
    id_aluno =models.ForeignKey(Aluno,models.DO_NOTHING, db_column='id_aluno')
    id_curso =models.ForeignKey(Curso,models.DO_NOTHING, db_column='id_curso')
    id_turno =models.ForeignKey(Turno,models.DO_NOTHING, db_column='id_turno')

    def __str__(self):
        return self.num_matricula

class Refeicao(models.Model):
    id_ref = models.AutoField(primary_key = True)
    nome_ref =models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome_ref

class Acesso(models.Model):
    id_acesso = models.AutoField(primary_key=True)
    nome_acesso = models.CharField(max_length=255,null=True, blank=True)
    data_acesso = models.DateTimeField(blank=True, null=True)
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    id_ref = models.ForeignKey(Refeicao, models.DO_NOTHING, db_column='id_ref')

    def __str__(self):
        return self.nome_acesso