from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

engine = create_engine('sqlite:///barbershop.db')

Base.metadata.create_all(bind=engine)

class Peluquero(Base):
    __tablename__ = 'peluqueros'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    servicios = relationship('Servicio', back_populates='peluquero')

class Servicio(Base):
    __tablename__ = 'servicios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    peluquero_id = Column(Integer, ForeignKey('peluqueros.id'))
    peluquero = relationship('Peluquero', back_populates='servicios')

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Reserva(Base):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship('Cliente')
    peluquero_id = Column(Integer, ForeignKey('peluqueros.id'))
    peluquero = relationship('Peluquero')
    servicio_id = Column(Integer, ForeignKey('servicios.id'))
    servicio = relationship('Servicio')
    fecha_hora = Column(DateTime, default=datetime.utcnow)
    completada = Column(Integer, default=0)
