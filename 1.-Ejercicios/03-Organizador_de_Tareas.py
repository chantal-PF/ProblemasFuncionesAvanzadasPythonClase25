# El objetivo de este ejercicio es crear un organizador de tareas (to-do list) simple donde puedas añadir, 
# ver y marcar tareas como completadas. Este programa te ayudará a gestionar tus actividades diarias.

tareas = []

def agregar_tarea(tarea):
    tareas.append({"tarea": tarea, "completada": False})

def mostrar_tareas():
    for i, tarea in enumerate(tareas, 1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['tarea']} - {estado}")

def completar_tarea(numero_tarea):
    if 0 < numero_tarea <= len(tareas):
        tareas[numero_tarea - 1]["completada"] = True

# Ejemplo de uso
while True:
    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        agregar_tarea(tarea)
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        mostrar_tareas()
        numero_tarea = int(input("Número de tarea a completar: "))
        completar_tarea(numero_tarea)
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")