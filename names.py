import json
from pathlib import Path
from tkinter import Button, Canvas, PhotoImage
from tkinter.filedialog import askopenfile
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path('graphic')

def relative_to_assets(file_name: str):
    return ASSETS_PATH / Path(file_name)
def asset_width(asset_id: int, canvas: Canvas):
    return canvas.bbox(asset_id)[2] - canvas.bbox(asset_id)[0]
def asset_height(asset_id: int, canvas: Canvas):
    return canvas.bbox(asset_id)[3] - canvas.bbox(asset_id)[1]
def button_coords(button_name: Button, canvas: Canvas):
    return [float(str(button_name.place_info())[str(button_name.place_info()).index("'x': '") + 6 : str(button_name.place_info()).index(", 'relx':") - 1]),
            float(str(button_name.place_info())[str(button_name.place_info()).index("'y': '") + 6 : str(button_name.place_info()).index(", 'rely':") - 1])]

color_background = '#FAFAC8'
font = ('Lato', 16)
font_bold = ('Lato', 16, 'bold')
font_small = ('Lato', 12)
color_font = 'black'
color_active_background = '#E6E6B4'#Ciemny żółty
#color_active_background = '#A48C54'#Ciemny brąz
#color_active_background = '#96BE7C'#Ciemny zielony
color_line = '#FFC81E'

os_python_command = 'python' if os.name == 'nt' else 'python3'

options_file = 'options.json'
def load_options():
    try:
        with open(options_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "separator_documents": ";;;",
            "separator_certificates": "\t",
            "placeholder_certificates_code": 48,
            "placeholder_certificates_amount": 10
        }

def get_option(which: int):
    return load_options()[list(load_options().keys())[which]]

def get_separator_documents():
    return get_option(0)

def get_separator_certificates():
    return get_option(1)

def get_placeholder_certificates_code():
    return get_option(2)

def get_placeholder_certificates_amount():
    return get_option(3)