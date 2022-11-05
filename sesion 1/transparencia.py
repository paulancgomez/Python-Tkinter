#El siguiente ejemplo ilustra una ventana con un 50% de transparencia:

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('600x400+50+50')
root.resizable(False, False)

#TRANSPARENCIA
root.attributes('-alpha', 0.5)

root.mainloop()