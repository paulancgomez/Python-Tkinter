# El siguiente programa ilustra cómo utilizar el método config() para establecer la opción de texto para la etiqueta.

import tkinter as tk
from tkinter import ttk


root = tk.Tk()


# Utilizar el método config() con atributos de palabras clave.
label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()

root.mainloop()