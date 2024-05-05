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

    def change_cordinate(self, input):
        latitud = input['input'].split(",")[0]
        longitud = input['input'].split(",")[1]
        self.latitud = latitud
        self.longitud = longitud
        self.mapa = folium.Map(location=(self.latitud, self.longitud))._repr_html_()

def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Airport Map", size="9", margin="12px",),
        rx.divider(width="90%"),
        rx.text("Enter a cordinate below with comma (lat, long)"),
        rx.form.root(
            rx.hstack(
                rx.input(
                    name="input",
                    placeholder="Enter the cordinate here",
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=MapState.change_cordinate,
            reset_on_submit=True,
        ),
        rx.hstack(
            rx.text(f"Latitud: {MapState.latitud}, Longitud: {MapState.longitud}")
        ),
        rx.box(
            rx.html(MapState.mapa),
            width="70%",
            border_width="thick",
            margin="12px",
        ),
        align="center",
    )

app = rx.App()
app.add_page(index)
