from tkinter import ttk
import tkinter as tk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Combobox")
        self.combo = ttk.Combobox(
            self,
            values=["Python", "C", "C++", "Java"],
            postcommand=self.dropdown_opened
        )
        self.combo.place(x=50, y=50)
        main_window.config(width=300, height=200)
        self.place(width=300, height=200)
    def dropdown_opened(self):
        print("Lista desplegada.")
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()