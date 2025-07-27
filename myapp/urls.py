from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
    path('editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
]
