import datetime

def agregar_tarea(lista_tareas, descripcion):
    """
    agregar una tarea a la lista si cumple con los requisitos
    """
    if len(descripcion)<3:
        return "error: Longitud invalida"
    
    #crear formato para tarea
    
    fecha = datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion}- {fecha}"
    lista_tareas.append(nueva_tarea)

    return f"tarea agregada con exito"

def listar_tareas(lista_tareas):
    """
    formatea la lista de tareas para su visualizacion
    """
    if not lista_tareas:
        return"no hay tareas"
    
    #agregar una variable llamada resultado 
    resultado ="listado de tareas\n"

    #iterar la lista de tareas y formatear la salida

    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"
    return resultado

def eliminarar_tarea(lista_tareas, indice):
    """
    eliminar una tarea por su numero de indice
    """
    if not indice.itsdigit():
        return "Error: El indice tiene que ser un numero"
    indice = int(indice)-1

    #agregamos la logica para preguntar
    #si elemento esta en lista y eliminarlo

    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop (indice)
    else:
        return"Error: No esxiste la tarea"
    return f"Tarea eliminada: {tarea_eliminada}"

def main():
    tareas = []
    PREFIJO ="!"

    print("Bienvenido al gestor de tareas")
    activa =True
    while activa:
        entrada = input(">>>").strip()

        if not entrada.startswith(PREFIJO):
            print("Error: Comando no reconocido")
            continue
        
    #procesamiento de la entrada
        cuerpo = entrada [len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len (cuerpo) > 1 else ""

        #seleccion de accion
        if comando == "add":
            resultado = agregar_tarea(tareas, argumento)
            print





    
