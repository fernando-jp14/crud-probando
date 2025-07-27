from django.http import HttpResponse
from .models import Project, Task, Estudiante
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EstudianteForm

# Create your views here.
def index(request):
    estudiantes = Estudiante.objects.all()
    form = EstudianteForm()
    return render(request, 'index.html', {'estudiantes': estudiantes, 'form': form})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')

def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'index.html', {'form': form, 'estudiante': estudiante})

def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('index')
 

