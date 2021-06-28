# Django-Resource-Server

## Prerequisites

- Install Python 3.6
- Install and setup [PostgreSQL](https://www.postgresql.org/download/) in the machine
- Install Pgadmin client to access the PostgreSQL database
- Create a database named `test_resource_server`

## Setup
- Clone the repository
- Create and activate new python virtual environment using [`virtualenv`](https://pypi.org/project/virtualenv/) 
- Install the necessary dependencies `pip install -r requirements.txt`
- Configure the database settings inside `backend_server/config.py`

## Instructions to run 
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
