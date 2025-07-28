from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done= models.BooleanField(default=False)

    def __str__(self):
        return self.title + " - " + self.project.name

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    ciclo = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre



