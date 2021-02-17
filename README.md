# Django Clinic
Django Clinic is the final project in Python and Django to accomplish Python from Scratch course in Software Development Academy.

## Info

* Python=3.8
* Django=3.0.8

## Main aims of the project.

* Dashboard for patients and employees to manage their accounts.
* Calendar for easy appointment booking
* Managing appointments form patient and staff
* System to create new patients and staff
* Easy browsing between patients and doctors


# Build instruction:

```bash
# create project folder and cd into it
 
# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install django
pip install django

django-admin.py startproject clinic

cd clinic

# change database name
mv db.sqlite3 clinic_db.sqlite3

cd ..

# clone clinic repository
git init
git remote add origin https://github.com/Cravtec/clinic.git
git fetch

!!!!!!!Check if master, probably need to pull repo!!!!!

# go inside clinic folder
cd clinic/

# install requirements
pip3 install -r requirements.txt

python manage.py migrate

python manage.py loaddata fixtures.json

# create your superuser

python  manage.py createsuperuser

python manage.py runserver
```

Server is running on localhost and port 8000:
http://127.0.0.1:8000
