import tkinter as tk
from tkinter import font
ventana = tk.Tk()
ventana.title("Barra de menús en Tk")
ventana.config(width=400, height=300)
barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff=False)
menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    # Tipo de fuente.
    font=font.Font(family="Times", size=14),
    # Color de fondo.
    background="#ADD8E6",
    # Color del texto.
    foreground="#FF0000",
    # Color de fondo cuanto el botón tiene el foco.
    activebackground="#32CDFF",
    # Color del texto cuando el botón tiene el foco.
    activeforeground="#FFFF00"
)
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
ventana.config(menu=barra_menus)
ventana.mainloop()