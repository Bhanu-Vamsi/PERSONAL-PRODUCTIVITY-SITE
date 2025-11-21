import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from calculator import CalculatorFrame
from notes import NotesFrame
from timer import TimerFrame
from file_organizer import FileOrganizerFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Productivity Suite")
        self.geometry("700x500")
        tab_control = ttk.Notebook(self)
        self.calc_tab = CalculatorFrame(tab_control)
        self.notes_tab = NotesFrame(tab_control)
        self.timer_tab = TimerFrame(tab_control)
        self.file_tab = FileOrganizerFrame(tab_control)
        tab_control.add(self.calc_tab, text="Calculator")
        tab_control.add(self.notes_tab, text="Notes")
        tab_control.add(self.timer_tab, text="Timer")
        tab_control.add(self.file_tab, text="File Organizer")
        tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    app = App()
    app.mainloop()