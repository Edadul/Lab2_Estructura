import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.ico", width="2em"),
            rx.heading("ESTRUCTURA", font_size="2em"),
        ),
        rx.spacer(),
        rx.menu.root(
            
        ),
        position="fixed",
        top="0px",
        background_color="lightgray",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
    )