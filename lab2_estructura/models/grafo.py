from typing import List
import networkx as nx
import pandas as pd
from lab2_estructura.models.airport import Airport
from typing import List
from queue import Queue

from lab2_estructura.models.dataframe import haversine

class Graph:
    def __init__(self) -> None:
        self.__graph = nx.Graph()
    
    def get_graph(self):
        return self.__graph
    
    def add_node(self, data:'pd.DataFrame') -> None:
        for index, row in data.iterrows():
            self.__graph.add_node(row['Source'], pos=(row['Source Airport Longitude'], row['Source Airport Latitude']))
            self.__graph.add_node(row['Destination'], pos=(row['Destination Airport Longitude'], row['Destination Airport Latitude']))

    def add_edge(self, data:'pd.DataFrame') -> None:
        for index, row in data.iterrows():
            self.__graph.add_edge(row['Source'], row['Destination'], weight=row['Weight'])  # Puedes usar 'Distance' si tienes esa información
    
    # Función para encontrar los 10 caminos mínimos más largos desde un aeropuerto dado
    def longest_shortest_paths(self, source, n=10):
        paths = nx.single_source_dijkstra_path_length(self.__graph, source)
        sorted_paths = sorted(paths.items(), key=lambda x: x[1], reverse=True)[:n]
        return sorted_paths
    
    # Mostrar la información de los 10 aeropuertos y las distancias de los caminos
    def show_longest_shortest_paths(self, longest_paths: List['tuple'], data:'pd.DataFrame') -> List['Airport']:
        list_airport = []
        for airport, distance in longest_paths:
            airport_info = data[data['Source'] == airport].iloc[0]
            list_airport.append(
                Airport().create_airport_target(airport_info, distance)
            )

    def dijkstra(self,u,v):
        masinf=float('inf')
        vertices=list(self.get_graph().nodes)
        distancias={w:masinf for w in vertices}
        fijos={w:False for w in vertices}
        padres={w:None for w in vertices}
        distancias[u]=0
        fijos[u]=True
        nuevo_fijo=u

        while not(all(fijos.values())):
            # Acualizar distancias.
            for w in self.get_graph().neighbors(nuevo_fijo):
                if fijos[w]==False:
                    nueva_dist=distancias[nuevo_fijo]+self.get_graph()[nuevo_fijo][w]['weight']
                    if distancias[w]>nueva_dist:
                        distancias[w]=nueva_dist
                        padres[w]=nuevo_fijo

            # Encontrar el nuevo a fijar.
            mas_chica=masinf
            for w in vertices:
                if fijos[w]==False and distancias[w]<mas_chica:
                    optimo=w
                    mas_chica=distancias[w]
            nuevo_fijo=optimo
            fijos[nuevo_fijo]=True

            # Cuando fije el vértice final v, dar el camino.
            if nuevo_fijo==v:
                camino=[v]
                while camino[0]!=u:
                    camino=[padres[camino[0]]]+camino
                return distancias[v], camino
    

    def get_path_info(self, source, target, data:'pd.DataFrame'):
        dist, path = self.dijkstra(source, target)
        path_info = []
        for airport_code in path[1:-1]:  # Excluimos el origen y el destino
            airport_info = data[data['Source'] == airport_code].iloc[0]
            path_info.append(airport_info)
        return path_info


    def longest_shortest_paths(self, source, n=10):
        paths = nx.single_source_bellman_ford_path_length(self.__graph, source)
        sorted_paths = sorted(paths.items(), key=lambda x: x[1], reverse=True)[:n]

        nodes_in_paths = []
        distance_in_paths = []
        for airport, distance in sorted_paths:
            nodes_in_paths.append(airport)
            distance_in_paths.append(distance)

        return nodes_in_paths, distance_in_paths