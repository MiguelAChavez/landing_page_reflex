import reflex as rx
from .fonts import Font
from .color import TextColor, Color

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.TEXT.value,
    "background_color": Color.PRIMARY.value,
}