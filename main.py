
from database import Base, engine

from models import Sala, Reserva

from operaciones import (
    insertar_sala,
    consultar_salas,
    registrar_reserva,
    consultar_reservas,
    cancelar_reserva,
    eliminar_sala
)


def crear_tablas():
    Base.metadata.create_all(bind=engine)


def leer_entero(mensaje):

    while True:

        try:
            numero = int(input(mensaje))
            return numero

        except ValueError:
            print("Error: debes ingresar un número entero.")


def menu():

    while True:

        print("\n========== SISTEMA DE RESERVAS ==========")
        print("1. Registrar sala")
        print("2. Consultar salas")
        print("3. Registrar reserva")
        print("4. Consultar reservas")
        print("5. Cancelar reserva")
        print("6. Eliminar sala")
        print("0. Salir")

        opcion = leer_entero("Selecciona una opción: ")

        if opcion == 1:

            nombre = input("Nombre de la sala: ")
            capacidad = leer_entero("Capacidad: ")

            insertar_sala(nombre, capacidad)

        elif opcion == 2:

            consultar_salas()

        elif opcion == 3:

            estudiante = input("Nombre del estudiante: ")
            sala_id = leer_entero("ID de la sala: ")
            fecha = input("Fecha (AAAA-MM-DD): ")

            registrar_reserva(estudiante, sala_id, fecha)

        elif opcion == 4:

            consultar_reservas()

        elif opcion == 5:

            id_reserva = leer_entero("ID de la reserva: ")

            cancelar_reserva(id_reserva)

        elif opcion == 6:

            id_sala = leer_entero("ID de la sala que deseas eliminar: ")

            eliminar_sala(id_sala)

        elif opcion == 0:

            print("¡Hasta luego!")
            break

        else:

            print("Opción no válida.")


if __name__ == "__main__":

    crear_tablas()
    menu()
