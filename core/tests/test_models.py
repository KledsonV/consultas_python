import pytest
from core.models import Paciente, Consulta
from datetime import date

@pytest.mark.django_db
def test_criar_paciente():
    paciente = Paciente.objects.create(
        nome='Ada Lovelace',
        cpf='11122233344',
        email='ada@example.com',
        telefone='11911112222',
        data_nascimento='1815-12-10',
    )
    assert Paciente.objects.count() == 1
    assert paciente.nome == 'Ada Lovelace'

@pytest.mark.django_db
def test_criar_consulta():
    paciente = Paciente.objects.create(
        nome='Alan Turing',
        cpf='55566677788',
        email='alan@example.com',
        telefone='11933334444',
        data_nascimento='1912-06-23',
    )
    consulta = Consulta.objects.create(
        paciente=paciente,
        medico='turing',
        data=date.today(),
        horario='08:00'
    )
    assert Consulta.objects.count() == 1
    assert consulta.medico == 'turing'
