import tkinter as tk
from tkinter import ttk


class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        # Find what (Encontrar)
        ttk.Label(self, text='Encuentre lo que:').grid(column=0, row=0, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)

        # Replace with (Reemplazar por):
        ttk.Label(self, text='Reemplazar por:').grid(
            column=0, row=1, sticky=tk.W)
        replacement = ttk.Entry(self, width=30)
        replacement.grid(column=1, row=1, sticky=tk.W)

        # Match Case checkbox (Casilla de verificación "Match Case")
        match_case = tk.StringVar()
        match_case_check = ttk.Checkbutton(
            self,
            text='Match case',
            variable=match_case,
            command=lambda: print(match_case.get()))
        match_case_check.grid(column=0, row=2, sticky=tk.W)

        # Wrap Around checkbox (Casilla de verificación "Wrap Around")
        wrap_around = tk.StringVar()
        wrap_around_check = ttk.Checkbutton(
            self,
            variable=wrap_around,
            text='Wrap around',
            command=lambda: print(wrap_around.get()))
        wrap_around_check.grid(column=0, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)


class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Button(self, text='Buscar siguiente').grid(column=0, row=0)
        ttk.Button(self, text='Reemplazar').grid(column=0, row=1)
        ttk.Button(self, text='Reemplazar todo').grid(column=0, row=2)
        ttk.Button(self, text='Cancelar').grid(column=0, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Reemplazar')
        self.geometry('400x150')
        self.resizable(0, 0)
        # sólo ventanas (eliminar el botón de minimizar/maximizar)
        self.attributes('-toolwindow', True)

        # diseño en la ventana root
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        # crear el marco de entrada
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)

        # crear el marco de botones
        button_frame = ButtonFrame(self)
        button_frame.grid(column=1, row=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()