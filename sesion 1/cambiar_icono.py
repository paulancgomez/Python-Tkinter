import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('300x200+50+50')
root.resizable(False, False)

#ICONO
root.iconbitmap('./assets/icono.ico')

root.mainloop()