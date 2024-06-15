"""
URL configuration for refeitorio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from refeitorioApp.views import home, new_curso,editar_curso,deletar_curso
from refeitorioApp.views import new_turno, editar_turno, deletar_turno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('new_curso/', new_curso, name='new_curso'),
    path('editar_curso/<str:id>', editar_curso, name='editar_curso'),
    path('deletar_curso/<str:id>', deletar_curso, name='deletar_curso'),

    #turno
    path('new_turno/', new_turno, name='new_turno'),
    path('editar_turno/<str:id>', editar_turno, name='editar_turno'),
    path('deletar_turno/<str:id>', deletar_turno, name='deletar_turno'),
]
