from django.test import TestCase
from django.urls import reverse
from .models import Estudiante
from django.contrib.auth.models import User

class EstudianteTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.estudiante = Estudiante.objects.create(
            nombre="Juan Pérez",
            carrera="Ingeniería",
            ciclo="3",
            correo="juan@example.com"
        )

    def test_listado_estudiantes(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Juan Pérez")

    def test_crear_estudiante(self):
        data = {
            'nombre': 'Ana López',
            'carrera': 'Contabilidad',
            'ciclo': '5',
            'correo': 'ana@example.com'
        }
        response = self.client.post(reverse('crear_estudiante'), data)
        self.assertEqual(response.status_code, 302)  # Redirecciona
        self.assertEqual(Estudiante.objects.count(), 2)
        self.assertTrue(Estudiante.objects.filter(nombre='Ana López').exists())

    def test_editar_estudiante(self):
        data = {
            'nombre': 'Juan Actualizado',
            'carrera': 'Sistemas',
            'ciclo': '4',
            'correo': 'nuevo@example.com'
        }
        response = self.client.post(reverse('editar_estudiante', args=[self.estudiante.id]), data)
        self.assertEqual(response.status_code, 302)
        estudiante_actualizado = Estudiante.objects.get(id=self.estudiante.id)
        self.assertEqual(estudiante_actualizado.nombre, 'Juan Actualizado')

    def test_eliminar_estudiante(self):
        response = self.client.get(reverse('eliminar_estudiante', args=[self.estudiante.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Estudiante.objects.filter(id=self.estudiante.id).exists())

    # 🚨 Test erróneo intencional para activar CI con error
    def test_crear_estudiante_erroneo(self):
        data = {
            'nombre': 'Carlos Mal',
            'carrera': 'Abogacía',
            'ciclo': '1',
            'correo': 'carlos@example.com'
        }
        response = self.client.post(reverse('crear_estudiante'), data)
        
        # ❌ Intencionalmente ponemos una condición falsa
        self.assertEqual(Estudiante.objects.count(), 99)  # Esto está mal a propósito




