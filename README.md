Proyecto Peluqueria Barbershop
Requisitos

    python3.6 o superior
    tener instalado pip
    Instalar sqlite (sudo dnf install sqlite)
    instalar sqlalchemy (modulo ORM para python) pip install SQLAlchemy==1.4.25 
    instalar Flask-Mail pip install Flask-Mail

Consideraciones

    Para crear la BD ejecutar el comando 'python -c "from models import Base, engine; Base.metadata.create_all(bind=engine)"'
    Para ejecutar el api ejecutar python app.py
