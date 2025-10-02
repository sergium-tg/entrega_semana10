# -*- coding: utf-8 -*-
# Parte B — Colas
from collections import deque
import heapq

def simulacion_turnos(clientes):
    turnos = deque(clientes)
    print(f"Los clientes en turno por orden de llegada son:  {list(turnos)}")
    print("\nLos clientes estan siendo atendidos, por favor esté atento...")

    while turnos:
        atendiendo = turnos.popleft()
        print(f"Atendiendo a: {atendiendo}")
        print(f"Número de clientes en espera: {len(turnos)}\n...")

def cola_prioridad(tareas):
    atender = []
    atenciones = ""
    print(f"Se ingresó una lista de tareas (prioridad, tarea): {tareas}")
    print(f"Se estan atendiendo las tareas por oden de prioridad...")
    for elemento in tareas:
        heapq.heappush(atender, elemento)
    while atender:
        prioridad, tarea = heapq.heappop(atender)
        atenciones += (f"Prioridad: {prioridad}, Tarea: {tarea}\n...atendido\n")
    print(atenciones)


if __name__ == "__main__":
    print("== Colas ==")
    print("Simulación de turnos:")
    simulacion_turnos(["Cliente1", "Cliente2", "Cliente3"])

    print("\nCola de prioridad:")
    cola_prioridad([(2,"tarea media"), (1,"tarea alta"), (3,"tarea baja")])