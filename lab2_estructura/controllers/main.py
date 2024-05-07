from lab2_estructura.models.map import Map
import pandas

def crear_objeto_mapa():
    return Map()

def get_latitud(map:'Map') -> float:
        return map.get_latitud()
    
def set_latitud(map:'Map', latitud:float) -> None:
    map.set_latitud(latitud)

def get_longitud(map:'Map') -> float:
    return map.get_longitud

def set_longitud(map:'Map', longitud:float) -> None:
    map.set_longitud(longitud)

# def render_map(map:'Map') -> None:
#     map.render_map()