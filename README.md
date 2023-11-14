# Thin9-Back
Repository of Thin9 Backend(Web)

## Stack
- Backend Server: Django 4.2.4
- DB: Postgre 13

## Install

## Install with Docker 

Run at project root directory.

included DB container.

```shell
docker-compose up -d
```

## Install with Anaconda

### Prerequisite

Install anacond or miniconda.

### Make Conda Envrionment
```shell
conda create -n thin9-back python=3.9 -y
conda activate thin9-back
```
### Install Requriements
```shell
pip install -r requriements.txt
```

### Set `.env` 

`.env` example 

```shell
DB_SERVER=localhost:5432
ML_SERVER_OD=localhost:8001
ML_SERVER_FOODSAM=localhost:8002
```

### Migration and Run Server

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## Service Port
- Backend: 8000 
- Database: 5432
- Object Detecton Model Server: 8001
- Segmantation Model Server: 8002


## Requirements
```shell
django==4.2.4
djangorestframework-simplejwt
drf-yasg
psycopg2-binary==2.9.7
Pillow
requests
django-cors-headers
django-environ==0.11.2
```

## .env.sample

```shell
ML_SERVER_OD=
ML_SERVER_FOODSAM=
DB_SERVER=
```
