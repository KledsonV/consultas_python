# Consultas Python 🏥

> **Sistema de Gestão de Consultas Médicas desenvolvido em Python**

## 📋 Sobre o Projeto

O **Consultas Python** é um sistema de gestão hospitalar que oferece:
- **👥 Cadastro de Pacientes** - Informações pessoais e histórico médico
- **👨‍⚕️ Cadastro de Médicos** - Especialidades e disponibilidade
- **📅 Agendamento** - Sistema completo de marcação de consultas

## 🚀 Tecnologias Utilizadas

### Interface & Backend
- **Python 3.8+** - Linguagem principal
- **SQLite3** - Banco de dados local

## 📂 Estrutura do Projeto

```
.
├── consultas
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── Explicação.txt
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_medico_paciente.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0002_medico_paciente.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── templates
│   │   └── core
│   │       ├── agendamento.html
│   │       ├── cadastrar_medico.html
│   │       ├── cadastro_paciente.html
│   │       ├── index.html
│   │       ├── __pycache__
│   │       │   └── forms.cpython-310.pyc
│   │       └── visualizar_agenda.html
│   ├── Testes.zip
│   ├── tests
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── test_forms.cpython-310-pytest-8.3.5.pyc
│   │   │   ├── test_models.cpython-310-pytest-8.3.5.pyc
│   │   │   ├── test_urls.cpython-310-pytest-8.3.5.pyc
│   │   │   └── test_views.cpython-310-pytest-8.3.5.pyc
│   │   ├── test_forms.py
│   │   ├── test_models.py
│   │   ├── test_urls.py
│   │   └── test_views.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── pytest.ini
├── README.md
├── requiriments.txt
└── static
    └── css
        └── styles.css
```

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Kledson Vinícius**

- 🌐 GitHub: [@KledsonV](https://github.com/KledsonV)
- 💼 LinkedIn: [Kledson Vinícius](https://linkedin.com/in/kledsonv)
