import reflex as rx
import reflex_page.Styles.index as styles
from reflex_page.Views.Nav.NavBar import navbar


def index() -> rx.Component:
    return rx.container(
        rx.box(navbar(), "Hello World!"), text_align="center", style={"padding": "1rem"}
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title="Prueba de Reflex",
    description="Una pequeña prueba de como es desarrollar en Reflex. ",
)

app.compile()
