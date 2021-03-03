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


# Build instruction(Docker below):

Required:
* Python 3.8
* pip
* git

```bash
# create project folder and cd into it
mkdir clinic && cd clinic
 
# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# AbstractBaseUser and auth Group are use for this project
# You have to first create django project and auth database
pip install django
django-admin.py startproject clinic

# go inside clinic folder and create auth database
cd clinic && python manage.py migrate auth

# change database name and go to previous directory
mv db.sqlite3 clinic_db.sqlite3 && cd ..

# clone clinic repository
git init
git remote add origin https://github.com/Cravtec/clinic.git
git fetch
git switch -tf origin/master

# install requirements and go inside clinic folder
pip install -r requirements.txt && cd clinic

# make database migration
python manage.py migrate

# load dummy data into database for better experience
python manage.py loaddata fixtures.json

# to create your superuser run
python  manage.py createsuperuser

# and at last start django server
python manage.py runserver
```

Server is running on localhost and port 8000:
http://127.0.0.1:8000


# Build instruction Docker:

Required:
* docker
* docker-compose
* git

```bash
# create project folder and cd into it
mkdir clinic && cd clinic

# clone github repository
git clone https://github.com/Cravtec/clinic.git

# build and run container
docker-compose build

# create your superuser
..................

# run container
docker-compose up

```