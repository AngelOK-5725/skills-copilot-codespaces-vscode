
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\acer\OneDrive\Документы\Тамила\tkinder_apps\xo\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("469x346")
window.configure(bg = "#2CC32C")




canvas = Canvas(
    window,
    bg = "#2CC32C",
    height = 346,
    width = 469,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    151.0,
    77.0,
    325.0,
    151.0,
    fill="#57CA31",
    outline="")

canvas.create_rectangle(
    192.0,
    157.0,
    277.0,
    248.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    199.0,
    165.0,
    277.0,
    240.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
