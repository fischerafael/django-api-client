# Passo 1 - Criar ambiente virutal

python -m venv ./venv

# Passo 2 - Ativar ambiente virtual

venv/Scripts/Activate

# Instalar Dependencias

pip install django
pip install djangorestframework

# Start Project

django-admin startproject setup .

# run server

python manage.py runserver

# create app

python manage.py startapp clients

# work on models
