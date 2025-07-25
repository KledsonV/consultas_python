import pytest
from core.forms import PacienteForm, ConsultaForm, MedicoForm
from core.models import Paciente, Medico, Consulta
from django.utils import timezone
from datetime import date

@pytest.mark.django_db
def test_paciente_form_valido():
    form = PacienteForm(data={
        'nome': 'Grace Hopper',
        'cpf': '99988877766',
        'email': 'grace@example.com',
        'telefone': '11922221111',
        'data_nascimento': '1906-12-09',
    })
    assert form.is_valid()

@pytest.mark.django_db
def test_paciente_form_invalido():
    form = PacienteForm(data={})
    assert not form.is_valid()

@pytest.mark.django_db
def test_consulta_form_valido():
    paciente = Paciente.objects.create(
        nome='Tim Berners-Lee',
        cpf='12312312312',
        email='tim@example.com',
        telefone='11933332222',
        data_nascimento='1955-06-08',
    )
    
    medico = Medico.objects.create(nome='Dra. Beatriz Lima')
    
    form = ConsultaForm(data={
        'paciente': paciente.pk,
        'medico': medico.pk,
        'data': timezone.now().date(),
        'horario': '14:00'
    })
    assert form.is_valid()

@pytest.mark.django_db
def test_medico_form_valid():
    form = MedicoForm(data={'nome': 'Dra. Ana Júlia'})
    assert form.is_valid()
    medico = form.save()
    assert Medico.objects.filter(nome='Dra. Ana Júlia').exists()

@pytest.mark.django_db
def test_medico_form_duplicate_name_case_insensitive():
    Medico.objects.create(nome='Dr. João Silva')
    form = MedicoForm(data={'nome': 'dr. joão silva'})
    assert not form.is_valid()
    assert 'nome' in form.errors
    
@pytest.mark.django_db
def test_consulta_form_valid():
    paciente = Paciente.objects.create(
        nome='Carlos Mendes',
        cpf='12345678901',
        email='carlos@email.com',
        telefone='99999-9999',
        data_nascimento='1990-01-01'
    )

    medico = Medico.objects.create(nome='Dra. Beatriz Lima')

    form_data = {
        'paciente': paciente.pk,
        'medico': medico.id,
        'data': date.today(),
        'horario': '08:00'
    }

    form = ConsultaForm(data=form_data)
    assert form.is_valid()
    consulta = form.save()
    assert Consulta.objects.filter(pk=consulta.pk).exists()