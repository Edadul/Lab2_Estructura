import pandas as pd
import math 
import networkx as nx
import graphviz as gv
import folium 

#Creacion de Dataframe
dataframe_original = pd.read_excel("./flights_final.xlsx")

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


################ Calcular la distancia entre dos puntos geográficos ################

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

##################### Calcular la distancia entre los aeropuertos #####################

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

################# Guardar el DataFrame con las distancias en un archivo Excel #################
data.to_excel("flights+distance.xlsx", index=False)

#Ordenar el DataFrame por el código del aeropuerto de origen
data = data.sort_values(by='Source Airport Code', ascending=True)

#Renombrar las columnas del DataFrame
data = data.rename(columns={'Source Airport Code': 'Source', 'Destination Airport Code': 'Destination', 'Distance': 'Weight'})



########## Crear un mapa centrado en la primera ubicación del DataFrame
m = folium.Map(location=[Airports['Airport Latitude'].mean(), Airports['Airport Longitude'].mean()], zoom_start=5)


###### Añadir marcadores con iconos personalizados de Bootstrap
for index, row in Airports.iterrows():
    folium.Marker(
        location=(row['Airport Latitude'], row['Airport Longitude']),
        popup = f"{row['Airport Code']}, {row['Airport Name']} - {row['Airport City']}, {row['Airport Country']}, Lat: {row['Airport Latitude']}, log: {row['Airport Longitude']}",
        icon=folium.Icon(icon='plane', prefix='fa', color='red')
    ).add_to(m)

#################### Registro de aristas dibujadas
drawn_edges = set()

####### Añadir líneas entre los aeropuertos de origen y destino
for index, row in data.iterrows():
    edge = tuple(sorted([(row['Source'], row['Destination'])]))  # Ordenar las aristas para evitar duplicados
    if edge not in drawn_edges:  # Verificar si la arista ya ha sido dibujada en la dirección opuesta
        tooltip_text = f"From: {row['Source Airport Latitude']}, {row['Source Airport Longitude']} To: {row['Destination Airport Latitude']}, {row['Destination Airport Longitude']} Distance: {row['Weight']} km"
        line = folium.PolyLine(
            locations=[
                (row['Source Airport Latitude'], row['Source Airport Longitude']),
                (row['Destination Airport Latitude'], row['Destination Airport Longitude'])
            ],
            color='blue',
            weight=3,
            opacity=0.8,
            tooltip=tooltip_text  # Añadir tooltip
        ).add_to(m)
        drawn_edges.add(edge)



#Busqueda de aeropuerto por codigo
def Busqueda_Aeropuerto_cod(Airport):
    info_source = data[data.Source == Airport]
    info_destination = data[data.Destination == Airport]
    info_busqueda = pd.concat([info_source, info_destination])
    return info_busqueda
   

