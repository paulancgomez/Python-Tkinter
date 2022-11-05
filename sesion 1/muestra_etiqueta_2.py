# El siguiente programa muestra la misma etiqueta. Sin embargo, utiliza un índice de diccionario para establecer la opción de texto para el widget de etiqueta.

import tkinter as tk
from tkinter import ttk


root = tk.Tk()


#Utilizar un índice de diccionario después de la creación del widget.
label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()

root.mainloop()