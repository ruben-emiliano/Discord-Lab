import datetime

def procesamiento_de_(lista_tareas, descripcion):
    """
    agregar una tarea a la lista si cumple con los requisitos
    """
    if len(descripcion)<3:
        return "error: Longitud invalida"
    
    #crear formato para tarea
    
    fecha = datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion}- {fecha}"
    lsita_tareas.append(nueva_tarea)

    return f"tarea agregada con exito"

    
