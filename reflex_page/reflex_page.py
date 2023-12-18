import Reflex as rx
import reflex_page.Styles.index as styles


def index()-> rx.Component:
    return rx.html.h1("Hello World");

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    );

app.add_page(
    index, 
    title="Prueba de Reflex", 
    description="Una pequeña prueba de como es desarrollar en Reflex. "
    );