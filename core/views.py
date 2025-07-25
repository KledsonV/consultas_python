from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ConsultaForm, PacienteForm, MedicoForm
from .models import Consulta

def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Consulta agendada com sucesso!")
            return redirect('agendar_consulta')  # ajustar para o nome correto da URL
    else:
        form = ConsultaForm()
    return render(request, 'core/agendamento.html', {'form': form})

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('cadastrar_paciente')
    else:
        form = PacienteForm()
    return render(request, 'core/cadastro_paciente.html', {'form': form})


def home(request):
    return render(request, 'core/index.html')


def visualizar_agendas(request):
    query = request.GET.get("q")
    if query:
        consultas = Consulta.objects.filter(paciente__contains=query)
    else:
        consultas = Consulta.objects.all().order_by('data', 'horario')
    context = {
        'consultas': consultas
    }
    return render(request, 'core/visualizar_agenda.html', context)


def cadastrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico cadastrado com sucesso!')
            return redirect('cadastrar_medico')
    else:
        form = MedicoForm()
    
    return render(request, 'core/cadastrar_medico.html', {'form': form})