import reflex as rx
from lab2_estructura.views.components.navbar import navbar

def home() -> rx.Component:
    return rx.vstack(
        navbar()
    )

x = 45
