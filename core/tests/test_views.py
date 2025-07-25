import pytest
from django.urls import reverse
from core.models import Paciente
from django.utils import timezone

@pytest.mark.django_db
def test_get_agendar_consulta(client):
    url = reverse('agendar_consulta')
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context

@pytest.mark.django_db
def test_post_agendar_consulta_valido(client):
    paciente = Paciente.objects.create(
        nome='Nikola Tesla',
        cpf='11122233300',
        email='tesla@example.com',
        telefone='11900009999',
        data_nascimento='1856-07-10'
    )
    url = reverse('agendar_consulta')
    response = client.post(url, {
        'paciente': paciente.pk,
        'medico': 'newton',
        'data': timezone.now().date(),
        'horario': '11:00'
    })
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_agendar_consulta_invalido(client):
    url = reverse('agendar_consulta')
    response = client.post(url, {})
    assert response.status_code == 200
    assert 'form' in response.context
