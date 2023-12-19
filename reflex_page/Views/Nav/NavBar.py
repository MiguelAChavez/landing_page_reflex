import reflex as rx
from reflex_page.Styles.index import Size


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="christmas_tree.png",
                alt="imagen de un árbol de navidad con sonrisa.",
            ),
            rx.text("Navidad 2023"),
            rx.spacer(),
            width="100%",
        )
    )
