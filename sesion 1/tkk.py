#El siguiente programa ilustra cómo crear etiquetas clásicas y temáticas

#IMPORTAR: Las siguientes declaraciones importan los widgets temáticos clásicos y nuevos de Tk
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

root.mainloop()