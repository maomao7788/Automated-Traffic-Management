# Automated Traffic Management

## Project Overview

This repository contains a Django-based application designed as a project for Lancaster University.

## Project Participants
* Daniil Karbukov
* Ruochen Liao

## Features

- **User management**: Registration, login, profile editing via `UserRegisterForm`, `PersonForm`.  
- **CRUD:** Persons, Cars, Licenses, Junctions.  
- **Traffic logs:** Record car entry/exit times in `JunctionLog`.  
- **Emergency mode:** Toggle junction signals and send alert emails when an “important” vehicle moves.  
- **Congestion detection & prediction:** Check upstream traffic, warn drivers, predict next-hour congestion.  
- **Traffic flow charts:** 24-hour plot per junction rendered as inline Base64 PNG.  
- **Admin interface:** Superusers can generate fines via camera-violation logic.  

## Requirements
* [Django](https://www.djangoproject.com/download/)
* [Python](https://www.python.org/downloads/)
* [Matplotlib](https://pypi.org/project/matplotlib/)
* [PostgreSQL](https://www.postgresql.org/download/)

## System Architecture and Constraints

- **Operating System:** Windows, macOS, or Linux  
- **Python:** 3.x
- **Django version:** 5.1.2  
- **Database:** PostgreSQL  

## Repository Structure
VRLPR/
- .history/
- CarProject/
  - __init__.py
  - settings.py
  - urls.py
  - wsgi.py
  - templates/
    - car_confirm_delete.html
    - car_form.html
    - car_list.html
    - index.html
    - license_form.html
    - login.html
    - profile.html
    - register.html
    - traffic_flow_analysis.html
- LicenseTracker/
  - __pycache__/
  - migrations/
    - __init__.py
  - templates/
  - __init__.py
  - admin.py
  - apps.py
  - forms.py
  - models.py
  - tests.py
  - urls.py
  - views.py
- db.sqlite3
- manage.py


## Building and Running
* Make sure your PostgreSQL server is running
* Check if the database parametres in settings.py are accurate. Located at VRLPR/CarProject
* Run the following commands:
* * Python manage.py makemigrations LicenseTracker
  * Python manage.py migrate LicenseTracker
  * python manage.py runserver
* Access the application at `http://127.0.0.1:8000/`
  
## Below you can find our UMLs

### Use Case UML

![](https://github.com/LegendaryLoona/LancasterVRLPR/blob/main/UMLs/UseCaseUml.png)

### Class UML

![](https://github.com/LegendaryLoona/LancasterVRLPR/blob/main/UMLs/ClassUML.png)

### Sequence UMLs

[All of the diagrams (draw.io)](https://app.diagrams.net/#G1AxWo89ccFKJ6HcFhXWO2F0h_ZvS-xg-v#%7B"pageId"%3A"pz4HMEyCPNZR9tuViDBD"%7D)
