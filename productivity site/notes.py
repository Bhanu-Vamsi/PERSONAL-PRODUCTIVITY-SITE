import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json, os

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.json")

class NotesFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        left = ttk.Frame(self)
        right = ttk.Frame(self)
        left.pack(side="left", fill="y", padx=(0,10))
        right.pack(side="right", fill="both", expand=True)
        self.listbox = tk.Listbox(left, width=30)
        self.listbox.pack(fill="y", expand=True)
        btn_frame = ttk.Frame(left)
        btn_frame.pack(pady=5)
        ttk.Button(btn_frame, text="New", command=self.new_note).grid(row=0,column=0, padx=2)
        ttk.Button(btn_frame, text="Delete", command=self.delete_note).grid(row=0,column=1, padx=2)
        self.title_var = tk.StringVar()
        ttk.Entry(right, textvariable=self.title_var, font=("Helvetica",14)).pack(fill="x")
        self.text = tk.Text(right)
        self.text.pack(fill="both", expand=True)
        action = ttk.Frame(right)
        action.pack(pady=5)
        ttk.Button(action, text="Save", command=self.save_note).grid(row=0,column=0, padx=2)
        ttk.Button(action, text="Load", command=self.load_note).grid(row=0,column=1, padx=2)
        self.notes = {}
        self.load_all()
        self.listbox.bind("<<ListboxSelect>>", lambda e: self.on_select())

    def load_all(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r", encoding="utf-8") as f:
                try:
                    self.notes = json.load(f)
                except:
                    self.notes = {}
        else:
            self.notes = {}
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, 'end')
        for k in sorted(self.notes.keys()):
            self.listbox.insert('end', k)

    def new_note(self):
        self.title_var.set("Untitled")
        self.text.delete("1.0", "end")

    def save_note(self):
        title = self.title_var.get().strip() or "Untitled"
        content = self.text.get("1.0", "end").rstrip()
        self.notes[title] = content
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=2)
        self.refresh_list()
        messagebox.showinfo("Saved", "Note saved.")

    def load_note(self):
        sel = self.listbox.curselection()
        if not sel: return
        key = self.listbox.get(sel[0])
        self.title_var.set(key)
        self.text.delete("1.0", "end")
        self.text.insert("1.0", self.notes.get(key, ""))

    def delete_note(self):
        sel = self.listbox.curselection()
        if not sel: return
        key = self.listbox.get(sel[0])
        if key in self.notes:
            del self.notes[key]
            with open(NOTES_FILE, "w", encoding="utf-8") as f:
                json.dump(self.notes, f, ensure_ascii=False, indent=2)
            self.refresh_list()