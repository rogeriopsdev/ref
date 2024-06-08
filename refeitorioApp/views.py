from django.shortcuts import render, get_object_or_404, redirect
from refeitorioApp.models import Curso,Aluno,Refeicao,Turno,Acesso,Matricula
from refeitorioApp.forms import CursoForm,AlunoForm,RefeicaoForm,TurnoForm, AcessoForm, MatriculaForm

# Create your views here.
def home(request):
    return render(request,'refeitorio/home.html')

#curso
def new_curso(request):
    form =CursoForm(request.POST)
    cursos = Curso.objects.all()
    if request.method == "POST":
        form =CursoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form=CursoForm()
    context ={'form':form, 'cursos':cursos}
    return render(request,'refeitorio/new_curso.html',context)


def editar_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    form =CursoForm(instance=curso)
    cursos = Curso.objects.all()
    context = {'form': form, 'cursos': cursos,'curso':curso}
    if request.method == "POST":
        form =CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('new_curso')
        else:
            return render(request,'refeitorio/editar_curso.html', context)
    else:
        return render(request,'refeitorio/editar_curso.html',context)


def deletar_curso(request, id):
    curso = get_object_or_404(Curso, pk=id)
    form = CursoForm(instance=curso)
    cursos = Curso.objects.all()
    context ={'curso':curso, 'form':form, 'cursos':cursos}
    if request.method == "POST":
        curso.delete()
        return redirect('new_curso')
    return render(request, 'refeitorio/deletar_curso.html', context)

