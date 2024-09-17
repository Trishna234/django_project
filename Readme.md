pip install django
django-admin startproject project .  (to start project)
python manage.py startapp base     (to install app)
python manage.py runserver    (to run the server)
python -m venv venv (to create virtual environment)

 python manage.py makemigrations (used for database table)
 python manage.py migrate 
python manage.py createsuperuser (to create username and password)
 pip freeze > requirements.txt  (show all the packages which are install)
 pip install psycopg2-binary (connect postgres)
 pip install -r .\requirements.txt (to install all the packages in requirements)

-(Post method is used to create object)
-(Get method is used to create list,retrieve)
-put and patch method is used to update(put update all the method/patch update particular object)
-delete method is used for delete
-to start project first make models,form, view, template
 
pip install djangorestframework (to install rest framework)