from django.urls import path
from .views import probando
from .views import agregarEmprendimiento


urlpatterns = [
    path('', probando),
    path('agregarEmprendimiento', agregarEmprendimiento)
]