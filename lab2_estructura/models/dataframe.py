import pandas as pd
import math 
import networkx as nx
import graphviz as gv
import folium 

#Creacion de Dataframe
dataframe_original = pd.read_excel("lab2_estructura/assets/files/flights_final.xlsx")

#Eliminacion de columnas innecesarias
data = dataframe_original.drop_duplicates()


# Crear un DataFrame para los aeropuertos de origen y destino
df = pd.DataFrame(data)


# Crear un DataFrame para los aeropuertos de origen
source_df = df[['Source Airport Code', 'Source Airport Name', 'Source Airport City', 'Source Airport Country', 'Source Airport Latitude', 'Source Airport Longitude']].copy()
source_df.columns = ['Airport Code', 'Airport Name', 'Airport City', 'Airport Country', 'Airport Latitude', 'Airport Longitude']


# Crear un DataFrame para los aeropuertos de destino
destination_df = df[['Destination Airport Code', 'Destination Airport Name', 'Destination Airport City', 'Destination Airport Country', 'Destination Airport Latitude', 'Destination Airport Longitude']].copy()
destination_df.columns = ['Airport Code', 'Airport Name', 'Airport City', 'Airport Country', 'Airport Latitude', 'Airport Longitude']


# Concatenar los DataFrames verticalmente
combined_df = pd.concat([source_df, destination_df], ignore_index=True)


###### Eliminar duplicados
Airports = combined_df.drop_duplicates()

def search_airport_bool(list_airports:list, n, cod_airport):
    list_airports.sort()
    inf = 0
    sup = n-1
    while (inf != sup):
        med = (inf + sup) // 2
        if (cod_airport == list_airports[med]):
            return True
        elif (cod_airport > list_airports[med]):
            inf = med + 1
        else:
            sup = med - 1
    return False


################ CALCULAR LA DISTANCIA ENTRE DOS PUNTOS GEOGRÁFICOS ################
def haversine(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    # Conversión de grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Diferencias de las coordenadas
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Formula de Haversine
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distancia entre los dos puntos
    distance = R * c

    return distance


# Crear una nueva columna en el DataFrame para almacenar la distancia entre los aeropuertos
# Aplicar la función de Haversine a cada fila del DataFrame
data['Distance'] = data.apply(
    lambda row: haversine(
        row['Source Airport Latitude'], 
        row['Source Airport Longitude'], 
        row['Destination Airport Latitude'], 
        row['Destination Airport Longitude']
    ), axis=1
)

def Busqueda_Aeropuerto_cod(cod_airport:str, data: 'pd.DataFrame'):
        info_source = data[data.Source == cod_airport]
        info_destination = data[data.Destination == cod_airport]
        info_busqueda = pd.concat([info_source, info_destination])

        return info_busqueda

#Ordenar el DataFrame por el código del aeropuerto de origen
#Renombrar las columnas del DataFrame
data = data.sort_values(by='Source Airport Code', ascending=True)
data = data.rename(columns={'Source Airport Code': 'Source', 'Destination Airport Code': 'Destination', 'Distance': 'Weight'})

data.to_excel("flights+distance.xlsx", index=False)
