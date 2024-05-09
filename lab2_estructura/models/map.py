import folium.vector_layers
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
        self.map_render: 'folium.Map' = folium.Map([0,0],zoom_start=3)
    
    def get_latitud(self) -> float:
        return self.__latitud
    
    def set_latitud(self, latitud) -> None:
        self.__latitud = latitud

    def get_longitud(self) -> float:
        return self.__longitud
    
    def set_longitud(self, longitud) -> None:
        self.__longitud = longitud
    
    def render_map_init(self) -> None:
        self.map_render = folium.Map([0,0],zoom_start=3)
    
    def draw_minimun_path(self, path, data:'pd.DataFrame', source, target, path_info):
        self.map_render = folium.Map([0,0], zoom_start=3)
        distance_total = 0
        # Añadir las líneas que representan el camino mínimo
        for i in range(len(path)-1):
            src = path[i]
            dst = path[i+1]
            try:
                src_lat = data.loc[data['Source'] == src, 'Source Airport Latitude'].values[0]
                src_lon = data.loc[data['Source'] == src, 'Source Airport Longitude'].values[0]
            except:
                src_lat = data.loc[data['Destination'] == src, 'Destination Airport Latitude'].values[0]
                src_lon = data.loc[data['Destination'] == src, 'Destination Airport Longitude'].values[0]

            try:
                dst_lat = data.loc[data['Destination'] == dst, 'Destination Airport Latitude'].values[0]
                dst_lon = data.loc[data['Destination'] == dst, 'Destination Airport Longitude'].values[0]
            except:
                dst_lat = data.loc[data['Source'] == dst, 'Source Airport Latitude'].values[0]
                dst_lon = data.loc[data['Source'] == dst, 'Source Airport Longitude'].values[0]


            distance = haversine(src_lat,src_lon,dst_lat,dst_lon)
            distance_total += distance
            tooltip_text = f"From: {src}, To: {dst}, Distance: {distance} km, Total distance: {distance_total} km"
            folium.PolyLine([(src_lat, src_lon), (dst_lat, dst_lon)], color='#45474A', weight='1', tooltip=tooltip_text).add_to(self.map_render)

        # Añadir los marcadores del origen y destino
        origen = Airport()
        try:
            origen.create_airport_origin(data[data['Source'] == source].iloc[0], 0)
        except:
            origen.create_airport_target(data[data['Destination'] == source].iloc[0], 0)
        folium.Marker(
                        [origen.get_latitude(), origen.get_longitude()],
                        popup=f"{origen.get_cod_airport()},{origen.get_name()} ({origen.get_city()}, {origen.get_country()}) \nLat: {origen.get_latitude()} Lon: {origen.get_longitude()}",
                        icon=folium.Icon(color='green')).add_to(self.map_render)
        
        destino = Airport()
        destino.create_airport_target(data[data['Destination'] == target].iloc[0], 0)
        folium.Marker(
                        [destino.get_latitude(), destino.get_longitude()],
                        popup=f"{destino.get_cod_airport()},{destino.get_name()} ({destino.get_city()}, {destino.get_country()}) \nLat: {destino.get_latitude()} Lon: {destino.get_longitude()}",
                        icon=folium.Icon(color='red')).add_to(self.map_render)

        # Añadir los marcadores de los aeropuertos intermedios
        for airport_info in path_info:
            airport_inter = Airport()
            airport_inter.create_airport_origin(airport_info, 0)
            folium.Marker(
                            [airport_inter.get_latitude(), airport_inter.get_longitude()], 
                            popup=f"{airport_inter.get_cod_airport()},{airport_inter.get_name()} ({airport_inter.get_city()}, {airport_inter.get_country()}) \nLat: {airport_inter.get_latitude()} Lon: {airport_inter.get_longitude()}").add_to(self.map_render)
    

    def add_elements_to_map(self, nodes, cod_buscar, data: 'pd.DataFrame', Airports: 'pd.DataFrame', list: list):
        cont = 0
        for node in nodes:
            # Intentar obtener información desde ambos 'Source' y 'Destination'
            if not data[data['Source'] == node].empty:
                info = data[data['Source'] == node].iloc[0]
            else:
                info = data[data['Destination'] == node].iloc[0]

            # Agregar marcador
            folium.Marker(
                [info['Source Airport Latitude'], info['Source Airport Longitude']],
                popup=f"{info['Source']}, {info['Source Airport Name']} ({info['Source Airport City']}, {info['Source Airport Country']}) Lat: {info['Source Airport Latitude']}, Lon: {info['Source Airport Longitude']}, Distance from {cod_buscar}: {list[cont]}",
                icon=folium.Icon(color='red')
            ).add_to(self.map_render)

            # Agregar arista si es apropiado
            if node != cod_buscar:
                src_info = Airports[Airports.Code == cod_buscar].iloc[0]
                dst_info = info
                
                tooltip_text = f"From: {cod_buscar}, To: {dst_info}, Distance: {list[cont]} km"
                folium.PolyLine(
                    [(src_info['Airport Latitude'], src_info['Airport Longitude']),
                    (dst_info['Source Airport Latitude'], dst_info['Source Airport Longitude'])],
                    color='black', weight=1, tooltip=tooltip_text
                ).add_to(self.map_render)

            cont += 1
                
        #Agregar marcador de origen
        ########## DATOS DEL AEROPUERTO DE BUSQUEDA ##############
        #Se busca en el dataframe de solo aeropuertos (Airports)
        code_origen = Airports[Airports.Code == cod_buscar].iloc[0].values[0]
        name_origen = Airports[Airports.Code == cod_buscar].iloc[0].values[1]
        city_origen = Airports[Airports.Code == cod_buscar].iloc[0].values[2]
        country_origen = Airports[Airports.Code == cod_buscar].iloc[0].values[3]
        lat_origen = Airports[Airports.Code == cod_buscar].iloc[0].values[4]
        lon_origen = Airports[Airports.Code == cod_buscar].iloc[0].values[5]
        folium.Marker([lat_origen, lon_origen], popup=f"{code_origen},{name_origen} ({city_origen}, {country_origen}), lat: {lat_origen}, log:{lon_origen}", icon=folium.Icon(color='green')).add_to(self.map_render)


    def draw_minimun_path_max(self, data: 'pd.DataFrame'):
        map_center = [data['Source Airport Latitude'].mean(), data['Source Airport Longitude'].mean()]
        self.map_render = folium.Map(location=map_center, zoom_start=3)