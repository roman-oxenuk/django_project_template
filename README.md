# django_project_template
Template for newborn django project. Use with django-admin.py startproject --template="https://github.com/roman-oxenuk/django_project_template/archive/master.zip" 

To create a new project by this template:
* mkproject projectname
* pip install django
* cd ../
* django-admin startproject projectdir projectname --template="https://github.com/roman-oxenuk/django_project_template/archive/master.zip"
* cd projectdir 
* pip install -r project/requirements.txt
* chmod +x manage.py
* ./manage.py migrate
* ./manage.py createsuperuser
* pip freeze > project/requirements.txt

To check it:
* ./manage.py runserver
* localhost:8000/hello
