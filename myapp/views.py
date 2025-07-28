from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from .forms import EstudianteForm, RegistroForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_view')
def index(request):
    estudiantes = Estudiante.objects.all()
    form = EstudianteForm()
    return render(request, 'index.html', {
        'estudiantes': estudiantes,
        'form': form,
        'editando': False
    })

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
    
    estudiantes = Estudiante.objects.all()
    return render(request, 'index.html', {
        'form': form,
        'estudiantes': estudiantes,
        'editando': True,
        'estudiante_id': estudiante.id
    })

def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login_view')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])  # encripta la contraseña
            usuario.save()
            return redirect('login_view')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

 

