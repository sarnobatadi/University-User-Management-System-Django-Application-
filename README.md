# University-User-Management-System-Django-Application-

### User Management System for University Schema 




### How to use
1.Initially Django basic installation is to be done to run application locally
```
pip install Django
```
2.After Installation Migrating django models to local database
```
python manage.py makemigrations
python manage.py migrate
```
3.Runserver locally
```
python manage.py runserver
```
Server will start listening locally at - http://127.0.0.1:8000/

4.Create superuser to setup login credentials
```
python manage.py createsuperuser
```
5.Login into the application with admin credentials created in previous step
