# 🐍 Minha Primeira Aplicação Django

Projeto desenvolvido para a disciplina de **Django**, utilizando Python e o framework Django para criar uma página web simples.

## 📌 Sobre o projeto

Esta aplicação apresenta uma página HTML criada e disponibilizada por meio de uma aplicação Django.

O objetivo é praticar os primeiros conceitos do framework, incluindo criação de projetos, aplicações, visualizações e rotas.

## 🚀 Tecnologias utilizadas

- Python
- Django
- HTML5
- Gunicorn

## 📂 Estrutura do projeto

```text
task-django/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── minha_app/
│   ├── migrations/
│   ├── views.py
│   └── index.html
│
├── .gitignore
├── manage.py
└── requirements.txt
```

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Mateus88B/task-django.git
```

### 2. Entre na pasta

```bash
cd task-django
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Git Bash:

```bash
source venv/Scripts/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

http://127.0.0.1:8000/

## 👨‍💻 Autor

**Mateus Henrique**

Projeto acadêmico desenvolvido para a disciplina de Django.
