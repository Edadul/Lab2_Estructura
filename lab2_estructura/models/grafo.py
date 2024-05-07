from typing import List
import networkx as nx
import pandas as pd
from lab2_estructura.models.airport import Airport
from typing import List

class Graph:
    def __init__(self) -> None:
        self.__graph = nx.DiGraph()
    
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
    
    def get_path_info(self, source, target, data:'pd.DataFrame'):
        path = nx.shortest_path(self.__graph, source=source, target=target)
        path_info = []
        for airport_code in path[1:-1]:  # Excluimos el origen y el destino
            airport_info = data[data['Source'] == airport_code].iloc[0]
            path_info.append(airport_info)
        return path_info