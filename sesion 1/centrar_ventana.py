#A veces, es posible que desee centrar la ventana en la pantalla. El siguiente programa ilustra cómo hacerlo:

import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window - Center')

window_width = 300
window_height = 200

# obtener la dimensión de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# encontrar el punto central
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# fijar la posición de la ventana en el centro de la pantalla
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.mainloop()