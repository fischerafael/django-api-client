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

# install the app

# work on models

# create requirements.txt

pip freeze > requirements-dev.txt

# make migrations

python manage.py makemigrations

# migrate

python manage.py migrate
