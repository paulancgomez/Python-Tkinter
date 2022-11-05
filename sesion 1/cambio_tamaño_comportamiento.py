#El método resizable() tiene dos parámetros que especifican si se puede cambiar el tamaño del ancho y el alto de la ventana.

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('600x400+50+50')

#CAMBIO DE TAMAÑO: window.resizable(width,height)
root.resizable(False, False)

root.mainloop()