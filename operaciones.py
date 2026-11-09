from datetime import datetime   
from sqlalchemy import select
from database import SessionLocal
from models import Sala, Reserva
from datetime import datetime

def insertar_sala(nombre, capacidad):

    if not nombre.strip():
        print("El nombre no puede estar vacío.")
        return

    if capacidad <= 0:
        print("La capacidad debe ser mayor que cero.")
        return

    with SessionLocal.begin() as session:

        sala = Sala(
            nombre=nombre,
            capacidad=capacidad
        )

        session.add(sala)

    print("Sala registrada correctamente.")

def consultar_salas():

    with SessionLocal() as session:

        sentencia = select(Sala)

        salas = session.scalars(sentencia).all()

        if not salas:
            print("No hay salas registradas.")
            return

        for sala in salas:

            estado = "Disponible" if sala.disponible else "No disponible"

            print(
                f"ID: {sala.id} | "
                f"Nombre: {sala.nombre} | "
                f"Capacidad: {sala.capacidad} | "
                f"Estado: {estado}"
            )

def registrar_reserva(estudiante, sala_id, fecha):

    if not estudiante.strip():
        print("El nombre del estudiante es obligatorio.")
        return

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        print("La fecha debe tener formato AAAA-MM-DD.")
        return

    with SessionLocal.begin() as session:

        sala = session.get(Sala, sala_id)

        if sala is None:
            print("La sala no existe.")
            return

        if not sala.disponible:
            print("La sala no está disponible.")
            return

        reserva = Reserva(
            estudiante=estudiante,
            sala_id=sala_id,
            fecha=fecha
        )

        sala.disponible = False

        session.add(reserva)

    print("Reserva registrada correctamente.")

def consultar_reservas():

    with SessionLocal() as session:

        sentencia = select(Reserva)

        reservas = session.scalars(sentencia).all()

        if not reservas:
            print("No hay reservas registradas.")
            return

        for reserva in reservas:

            print(
                f"ID: {reserva.id} | "
                f"Estudiante: {reserva.estudiante} | "
                f"Sala: {reserva.sala.nombre} | "
                f"Fecha: {reserva.fecha}"
            )

def consultar_reservas():

    with SessionLocal() as session:

        sentencia = select(Reserva)

        reservas = session.scalars(sentencia).all()

        if not reservas:
            print("No hay reservas registradas.")
            return

        for reserva in reservas:

            print(
                f"ID: {reserva.id} | "
                f"Estudiante: {reserva.estudiante} | "
                f"Sala: {reserva.sala.nombre} | "
                f"Fecha: {reserva.fecha}"
            )

def cancelar_reserva(id_reserva):

    with SessionLocal.begin() as session:

        reserva = session.get(Reserva, id_reserva)

        if reserva is None:
            print("La reserva no existe.")
            return

        sala = reserva.sala

        sala.disponible = True

        session.delete(reserva)

    print("Reserva cancelada correctamente.")


def eliminar_sala(id_sala):

    with SessionLocal.begin() as session:

        sala = session.get(Sala, id_sala)

        if sala is None:
            print("La sala no existe.")
            return

        if sala.reservas:
            print("No se puede eliminar: la sala tiene reservas asociadas.")
            return

        session.delete(sala)

    print("Sala eliminada correctamente.")
