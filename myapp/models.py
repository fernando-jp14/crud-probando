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
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    carrera = models.CharField(max_length=100, verbose_name="Carrera")
    ciclo = models.CharField(max_length=20, verbose_name="Ciclo académico")
    correo = models.EmailField(unique=True, verbose_name="Correo institucional")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["nombre"] 

    def str(self):
        return f"{self.nombre} - {self.carrera}"



