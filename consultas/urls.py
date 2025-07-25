from django.contrib import admin
from django.urls import path
from core.views import home, cadastrar_paciente, agendar_consulta, visualizar_agendas, cadastrar_medico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastrar/', cadastrar_paciente, name='cadastrar_paciente'),
    path('agendar/', agendar_consulta, name='agendar_consulta'),
    path('agendamentos/', visualizar_agendas, name='visualizar_agendas'),
    path('cadastrar_medico/', cadastrar_medico, name='cadastrar_medico'),
]
