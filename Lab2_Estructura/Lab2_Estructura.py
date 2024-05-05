"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
import folium

 #Bq: 10.96854 -74.78132
 #Vz: 45.439722222222 12.331944444444

class MapState(rx.State):
    latitud: str = 10.96854
    longitud: str = -74.78132
    mapa = folium.Map(location=(latitud, longitud))._repr_html_()

    def search_cordinate(self, input):
        latitud = input['cordinate input'].split(',')[0]
        longitud = input['cordinate input'].split(',')[1]
        self.latitud = latitud
        self.longitud = longitud
        self.mapa = folium.Map(location=(self.latitud, self.longitud))._repr_html_()

def index() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.drawer.root(
                rx.drawer.trigger(rx.button(rx.icon(tag='heart'),)),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.heading('Airport Map', size='8', margin_top='30px',margin_bottom='20px', margin_x='auto',),
                            rx.divider(margin_bottom='25px',),
                            rx.tabs.root(
                                rx.center(
                                    rx.tabs.list(
                                        rx.tabs.trigger('Cordinates', value='tab1'),
                                        rx.tabs.trigger('Airport codes', value='tab2'),
                                    ),
                                    margin_bottom='20px'
                                ),
                                rx.tabs.content(
                                    rx.vstack(
                                        rx.text('Enter a cordinate below', margin_x='auto'),
                                        rx.form.root(
                                            rx.vstack(
                                                rx.input(
                                                    name='cordinate input',
                                                    placeholder='Ex: 10.96854, -74.78132',
                                                    width='300px',
                                                    height='40px'
                                                ),
                                                rx.button('Submit', type='submit', width='100%', height='40px'),
                                            ),
                                            margin_x='auto',
                                            on_submit=MapState.search_cordinate,
                                            reset_on_submit=True,
                                        ),
                                        rx.callout(
                                            'Cordinate must have a comma between latitude and longitude',
                                            icon='info',
                                        ),
                                        margin='9px'
                                    ),
                                    value='tab1',
                                ),
                                rx.tabs.content(
                                    rx.vstack(
                                        rx.text('Enter an airport code below', margin_top='9px'),
                                        rx.form.root(
                                            rx.hstack(
                                                rx.input(
                                                    name='airport code input',
                                                    placeholder='Ex: 101301401',
                                                ),
                                                rx.button('Submit', type='submit'),
                                                
                                            ),
                                        ),
                                        rx.callout(
                                            'Airport code must exist on the database :)',
                                            icon='info',
                                        ),
                                        margin='9px'
                                    ),
                                    value='tab2',
                                ),
                                default_value='tab1'
                            ),
                            width='100%',
                            aling='center',
                        ),
                        top='auto',
                        height='100%',
                        right='auto',
                        width='25em',
                        padding='2m',
                        background_color='#FFF'
                    ),
                ),
                aling='center',
                direction='left',
            ),
            align='center',
            width='4em',
        ),
        rx.html(MapState.mapa, width='100%',),
    ),

app = rx.App()
app.add_page(index)
