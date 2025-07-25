from django.urls import reverse, resolve
from core.views import agendar_consulta

def test_agendar_consulta_resolve():
    resolver = resolve(reverse('agendar_consulta'))
    assert resolver.func == agendar_consulta
