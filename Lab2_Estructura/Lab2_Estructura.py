"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from lab2_estructura.views.home import *
from lab2_estructura.models.dataframe import *
from lab2_estructura.controllers.main import *
from lab2_estructura.models.map import Map
from lab2_estructura.models.grafo import Graph
import folium

# class Mapa:
#     def __init__(self, latitud = 41.89193, longitud = 12.51133) -> None:
#         self.latitud = latitud
#         self.longitud = longitud
#         self.mapa = folium.Map(location=(self.latitud, self.longitud))
    
#     def render(self):
#         self.mapa = folium.Map(location=(self.latitud, self.longitud))
    
#mapa = Mapa()
mapa = Map()
# grafo = Graph()
# dataframe = data
# grafo.add_node(dataframe)
# grafo.add_edge(dataframe)
# source = 'ACR'  # Origen
# target = 'DME'  # Destino ZYI
# path = nx.shortest_path(grafo.get_graph(), source=source, target=target)

# path_info = grafo.get_path_info(source, target, dataframe)

# mapa.draw_minimun_path(path, dataframe, source, target, path_info)

class State(rx.State):
    # latitud: float = mapa.get_latitud()
    # longitud: float = mapa.get_longitud()
    # map = mapa.map_render._repr_html_()

    # def change_cordinates(self, latitud, longitud):    
    #     mapa.set_latitud(latitud)
    #     mapa.set_longitud(longitud)
    #     self.latitud = mapa.get_latitud()
    #     self.longitud = mapa.get_longitud()
    #     mapa.render_map_init()
    #     self.map = mapa.map_render._repr_html_()
    
    # def search_airport(self, cod_airport:str, data: 'pd.DataFrame'):
    #     mapa.Busqueda_Aeropuerto_cod(cod_airport, data)
    pass

class StateMap(rx.State):
    map = mapa.map_render._repr_html_()
    state_callout_1 = False
    state_callout = False

    def search_cordinate(self, input):
        latitud = input['search_airport'].split(',')[0]
        longitud = input['search_airport'].split(',')[1]
        mapa.map_render = folium.Map(location=(latitud, longitud), zoom_start=12)
        folium.Marker(
            [latitud, longitud], 
            icon=folium.Icon(color='darkblue')).add_to(mapa.map_render)
        self.map = mapa.map_render._repr_html_()

    def minimun_path(self, source, target):
        grafo = Graph()
        dataframe = data
        grafo.add_node(dataframe)
        grafo.add_edge(dataframe)
        path = nx.shortest_path(grafo.get_graph(), source, target)
        path_info = grafo.get_path_info(source, target, dataframe)
        mapa.draw_minimun_path(path, dataframe, source, target, path_info)
        self.map = mapa.map_render._repr_html_()
    
    def data_cod(self, form_data: dict):
        list_cod_airports = Airports['Airport Code'].to_list()

        if form_data['airport_departure'] in list_cod_airports and form_data['airport_destination'] in list_cod_airports:
            try:
                self.minimun_path(form_data['airport_departure'], form_data['airport_destination'])
                self.state_callout = False
            except:
                self.state_callout = True
        else:
            self.state_callout = True
        



def index() -> rx.Component:
    return rx.stack(
        rx.container(
            rx.html(StateMap.map, 
                    width='100%', 
                    display='block', 
                    position='absolute', 
                    left='0px', 
                    right='0px', 
                    top='0px', 
                    bottom='0px', 
                    overflow='hidden'),

            position='absoluite',
            display='block',
            width='100%',
            height='100%',
            left='0px', 
            right='0px', 
            top='0px', 
            bottom='0px'
        ),
        rx.box(
            rx.form.root(
                rx.flex(
                    rx.box(
                        rx.flex(
                            rx.input(
                                name='search_airport',
                                placeholder='Buscar: 41.89193, 12.51133',
                                background_color='#FFF',
                                padding='10px',
                                width='350px',
                                height='40px',
                                radius='full',  
                                border=None,
                                box_shadow='2px 2px 5px #A9A9A9',  
                            ),
                        ),
                        width='auto',
                    ),
                    width='auto',
                    justify='between',
                ),
                width='100%',
                on_submit=StateMap.search_cordinate,
                reset_on_submit=True,
            ),
            position='absolute',
            top='20px',
            left='100px'
        ),
        rx.box(
            rx.drawer.root(
                rx.drawer.trigger(rx.button(rx.icon(tag='menu', color='rgb(100,100,120)'), background_color='#FFF')),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.flex(
                                rx.box(
                                    rx.text('AIRPORT MAP', size='5'),
                                ),
                                rx.drawer.close(
                                    rx.box(rx.button(rx.icon(tag='x', color='rgb(100,100,120)', size=30), background_color='#FFF'))
                                ),
                                align_items="start",
                                padding='0 0 5px 0',
                                justify='between',
                                width='100%',
                                border_width_='0px 0px 2px 0px'
                            ),
                            rx.flex(
                                rx.tabs.root(
                                    rx.center(
                                        rx.tabs.list(
                                            rx.tabs.trigger('Cordinates', value='tab1', margin='0 25px 0 0'),
                                            rx.tabs.trigger('Airport codes', value='tab2', margin='0 0 0 25px'),
                                            margin_bottom='30px',
                                        ),    
                                    ),

                                    rx.flex(
                                        rx.tabs.content(
                                            rx.flex(
                                                rx.text('Enter a cordinate below', aling='center', size='1'),
                                                width='100%',
                                            ),
                                            rx.form.root(
                                                rx.flex(
                                                    rx.input(
                                                        name='cordinate input',
                                                        placeholder='Ex: 10.96854, -74.78132',
                                                        width='100%',
                                                        height='40px',
                                                        required=True,
                                                    ),
                                                    rx.button('Submit', type='submit', width='100%', height='40px', margin_bottom='15px', margin_top='20px'),
                                                    width='100%',
                                                    justify='center',
                                                    direction='column',
                                                ),
                                                width='100%',
                                                #on_submit=MapState.search_cordinate,
                                                reset_on_submit=True,
                                            ),
                                            rx.cond(
                                                StateMap.state_callout_1,
                                                rx.callout('Cordinate must have a comma between latitude and longitude', icon='info',),
                                                None
                                            ),
                                            width='100%',
                                            value='tab1',
                                        ),
                                        width='100%',
                                        direction='column',
                                    ),

                                    rx.flex(
                                        rx.tabs.content(
                                            rx.flex(
                                                rx.form.root(
                                                    rx.flex(
                                                        rx.flex(
                                                            rx.flex(
                                                                rx.text('Place of departure', size='1'),
                                                                rx.input(
                                                                    name='airport_departure',
                                                                    placeholder='Ex: BOG',
                                                                    width='100%',
                                                                    height='40px',
                                                                    required=True
                                                                ),
                                                                direction='column'
                                                            ),
                                                            rx.flex(
                                                                rx.text('Place of destination', size='1'),
                                                                rx.input(
                                                                    name='airport_destination',
                                                                    placeholder='Ex: BCN',
                                                                    width='100%',
                                                                    height='40px',
                                                                    required=True
                                                                ),
                                                                direction='column'
                                                            ),
                                                            width='100%',
                                                            justify='between',
                                                            spacing='2'
                                                        ),
                                                        
                                                        rx.button('Consult', type='submit', width='100%', height='40px', margin_bottom='15px', margin_top='20px'),
                                                        width='100%',
                                                        justify='center',
                                                        direction='column',
                                                    ),
                                                width='100%',
                                                on_submit=StateMap.data_cod,
                                                reset_on_submit=True,
                                                ),
                                                width='100%',
                                            ),
                                            
                                            rx.cond(
                                                StateMap.state_callout,
                                                rx.callout('Cordinate must have a comma between latitude and longitude', icon='info',),
                                                None
                                            ),
                                            width='100%',
                                            value='tab2',
                                        ),
                                        width='100%',
                                        direction='column',
                                    ),
                                    default_value='tab1',
                                ),
                                justify='center',
                                width='100%',                                
                            ),
                            width='100%'
                        ),
                        
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="20px",
                        background_color="#FFF",
                        box_shadow='0px 5px, 0px 0px',
                        # background_color=rx.color("green", 3)
                    )
                ),
                direction="left",
                top="auto",
                right="auto",
                height="100vh",
                width="70px",
                padding="2em",
                background_color="#FFF",
                box_shadow='0px 5px, 0px 0px',
            ),
            position= 'absolute',
            padding='5px',
            background_color="#FFF",
            box_shadow='2px 2px 4px #D1D1D1',
            margin='0',
            display='flex',
            flex_direction='column',
            height='100vh',
            weight='100px',
        ),

        
        margin='0',
        display='flex',
        height='100vh'
    )  

app = rx.App()
app.add_page(index)
