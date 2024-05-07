import pandas as pd
import math
import networkx as nx
import graphviz as gv
import folium
from typing import Optional
from lab2_estructura.models.dataframe import haversine
from lab2_estructura.models.airport import Airport

class Map():
    def __init__(self, latitud=None, longitud=None) -> None:
        self.__latitud: float = latitud
        self.__longitud: float = longitud
        self.map_render: 'folium.Map' = folium.Map([7,7],zoom_start=2)
    
    def get_latitud(self) -> float:
        return self.__latitud
    
    def set_latitud(self, latitud) -> None:
        self.__latitud = latitud

    def get_longitud(self) -> float:
        return self.__longitud
    
    def set_longitud(self, longitud) -> None:
        self.__longitud = longitud
    
    def render_map_init(self) -> None:
        if self.__latitud and self.__longitud != None:
            self.map_render = folium.Map(location=(self.__latitud, self.__longitud))
        else: 
            self.map_render = folium.Map()
    
    def draw_minimun_path(self, path, data:'pd.DataFrame', source, target, path_info):
        self.map_render = folium.Map()
        distance_total = 0
        # Añadir las líneas que representan el camino mínimo
        for i in range(len(path)-1):
            src = path[i]
            dst = path[i+1]
            src_lat = data.loc[data['Source'] == src, 'Source Airport Latitude'].values[0]
            src_lon = data.loc[data['Source'] == src, 'Source Airport Longitude'].values[0]
            dst_lat = data.loc[data['Destination'] == dst, 'Destination Airport Latitude'].values[0]
            dst_lon = data.loc[data['Destination'] == dst, 'Destination Airport Longitude'].values[0]
            distance = haversine(src_lat,src_lon,dst_lat,dst_lon)
            distance_total += distance
            tooltip_text = f"From: {src}, To: {dst}, Distance: {distance} km, Total distance: {distance_total} km"
            folium.PolyLine([(src_lat, src_lon), (dst_lat, dst_lon)], color='#45474A', weight='1', tooltip=tooltip_text).add_to(self.map_render)

        # Añadir los marcadores del origen y destino
        origen = Airport()
        origen.create_airport_origin(data[data['Source'] == source].iloc[0], 0)
        folium.Marker(
                        [origen.get_latitude(), origen.get_longitude()],
                        popup=f"{origen.get_cod_airport()},{origen.get_name()} ({origen.get_city()}, {origen.get_country()})",
                        icon=folium.Icon(color='green')).add_to(self.map_render)

        destino = Airport()
        destino.create_airport_target(data[data['Destination'] == target].iloc[0], 0)
        folium.Marker(
                        [destino.get_latitude(), destino.get_longitude()],
                        popup=f"{destino.get_cod_airport()},{destino.get_name()} ({destino.get_city()}, {destino.get_country()})",
                        icon=folium.Icon(color='red')).add_to(self.map_render)

        # Añadir los marcadores de los aeropuertos intermedios
        for airport_info in path_info:
            airport_inter = Airport()
            airport_inter.create_airport_origin(airport_info, 0)
            folium.Marker(
                            [airport_inter.get_latitude(), airport_inter.get_longitude()], 
                            popup=f"{airport_inter.get_cod_airport()},{airport_inter.get_name()} ({airport_inter.get_city()}, {airport_inter.get_country()})").add_to(self.map_render)
    
    
    

