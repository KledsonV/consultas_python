from django import forms
from .models import Consulta, Paciente, Medico

MEDICOS = [
    ('einstein', 'Albert Einstein'),
    ('curie', 'Marie Curie'),
    ('newton', 'Isaac Newton'),
    ('tesla', 'Nikola Tesla'),
    ('darwin', 'Charles Darwin'),
]

class ConsultaForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Selecione um paciente"
    )

    medico = forms.ModelChoiceField(
        queryset=Medico.objects.all().order_by('nome'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Selecione um médico"
    )


    HORARIOS = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
    ]

    horario = forms.ChoiceField(
        choices=HORARIOS,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data', 'horario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Já adicionamos classes acima, mas para garantir:
            if not field.widget.attrs.get('class'):
                if isinstance(field.widget, forms.Select):
                    field.widget.attrs['class'] = 'form-select'
                else:
                    field.widget.attrs['class'] = 'form-control'




class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'email', 'telefone', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'data_nascimento': 'Data de Nascimento',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'Select':
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
                
                
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do médico',
            })
        }
    def clean_nome(self):
        nome = self.cleaned_data['nome'].strip()
        if Medico.objects.filter(nome__iexact=nome).exists():
            raise forms.ValidationError("Já existe um médico com esse nome.")
        return nome