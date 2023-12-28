from barbershop.models import Peluquero, Servicio, Cliente, Reserva, Base, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'freelancerock.2017@gmail.com'
app.config['MAIL_PASSWORD'] = 'gvca*2020'

# Inicializa la extensión
mail = Mail(app)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Funciones para añadir clientes y peluqueros a la base de datos

def agregar_cliente(nombre, telefono, email):
    nuevo_cliente = Cliente(nombre=nombre, telefono=telefono, email=email)
    session.add(nuevo_cliente)
    session.commit()

def agregar_peluquero(nombre, servicios):
    nuevo_peluquero = Peluquero(nombre=nombre)
    for servicio in servicios:
        nuevo_servicio = Servicio(nombre=servicio, peluquero=nuevo_peluquero)
        session.add(nuevo_servicio)
    session.commit()

# Funciones para reservas de citas

def reservar_cita(cliente_id, peluquero_id, servicio_id):
    cita = Reserva(cliente_id=cliente_id, peluquero_id=peluquero_id, servicio_id=servicio_id)
    session.add(cita)
    session.commit()

# Función para verificar disponibilidad

def verificar_disponibilidad(peluquero_id, fecha_hora):
    citas = session.query(Reserva).filter_by(peluquero_id=peluquero_id, fecha_hora=fecha_hora).all()
    return len(citas) == 0

from flask_mail import Message

@app.route('/enviar_confirmacion_email')
def enviar_confirmacion_email(recipient):
    mensaje = Message('Asunto del Correo', sender='freelancerock.2017@gmail.com', recipients=[recipient])
    mensaje.body = 'Correo de confirmacion de cita'

    try:
        mail.send(mensaje)
        return 'Correo enviado con éxito.'
    except Exception as e:
        return f'Error al enviar el correo electrónico: {e}'

# Función para marcar citas como completadas

def completar_cita(reserva_id):
    cita = session.query(Reserva).filter_by(id=reserva_id).first()
    cita.completada = 1
    session.commit()

# Ejemplos de uso

# Agregar cliente
agregar_cliente("Nombre Cliente", "123456789", "cliente@email.com")

# Agregar peluquero con servicios
agregar_peluquero("Nombre Peluquero", ["Corte de pelo", "Tinte"])

# Reservar cita
reservar_cita(cliente_id=1, peluquero_id=1, servicio_id=1)

# Verificar disponibilidad
fecha_hora_reserva = datetime(2023, 12, 31, 14, 30)  # Reemplaza con la fecha y hora de tu reserva
disponible = verificar_disponibilidad(peluquero_id=1, fecha_hora=fecha_hora_reserva)

if disponible:
    print("La cita está disponible. Puedes reservar.")
else:
    print("Lo siento, el peluquero está ocupado en ese horario.")

# Enviar confirmación por email (simulado)
enviar_confirmacion_email(recipient='freelancerock.2017@gmail.com')

# Marcar cita como completada
completar_cita(reserva_id=1)
