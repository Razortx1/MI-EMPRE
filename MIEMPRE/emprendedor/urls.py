from django.urls import path
from .views import *


urlpatterns = [
    path('', probando, name='lista_emprendimiento'),
    path('agregarEmprendimiento', agregarEmprendimiento),
    path('actualizarEmprendimiento/<int:id>/', actualizarEmprendimiento),
    path('eliminarEmprendimiento/<int:id>/', eliminarEmprendimiento)
]