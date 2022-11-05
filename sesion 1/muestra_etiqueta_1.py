# A continuación se ilustra cómo utilizar los argumentos de la palabra clave para establecer la opción de texto para una etiqueta.

import tkinter as tk
from tkinter import ttk

# Utilizar argumentos de palabras clave en la creación del widget.
root = tk.Tk()
ttk.Label(root, text='Hi, there').pack()

root.mainloop()