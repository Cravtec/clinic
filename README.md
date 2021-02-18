# Django Clinic
Django Clinic is the final project in Python and Django to accomplish Python from Scratch course in Software Development Academy.

## Info

* Python=3.8
* Django=3.0.8

## Main aims of the project.

* Dashboard for patients and employees to manage their accounts(CRUD).
* Calendar for easy appointment booking
* Managing appointments form patient and staff
* System to create new patients and staff
* Easy browsing between patients and doctors


# Build instruction:

```bash
# create project folder and cd into it
mkdir clinic && cd clinic
 
# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# We use AbstractBaseUser and auth Group so you first have to create django project and auth database
pip install django
django-admin.py startproject clinic

# go inside clinic folder
cd clinic

# change database name and go to previous directory
mv db.sqlite3 clinic_db.sqlite3 && cd ..

# clone clinic repository
git init
git remote add origin https://github.com/Cravtec/clinic.git
git fetch
git switch -tf origin/master

# install requirements
pip install -r requirements.txt

# go inside clinic folder
cd clinic

# make database migration
python manage.py migrate

# load dummy data into database for better experience
python manage.py loaddata fixtures.json

# to create your superuser
python  manage.py createsuperuser

# and at last start django server
python manage.py runserver
```

Server is running on localhost and port 8000:
http://127.0.0.1:8000
