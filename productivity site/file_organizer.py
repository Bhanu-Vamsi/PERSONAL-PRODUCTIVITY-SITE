import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os, shutil

class FileOrganizerFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        ttk.Button(self, text="Select Folder", command=self.select_folder).pack(pady=5)
        self.folder_label = ttk.Label(self, text="No folder selected")
        self.folder_label.pack()
        ttk.Button(self, text="Organize", command=self.organize).pack(pady=10)
        self.folder = None

    def select_folder(self):
        self.folder = filedialog.askdirectory()
        if self.folder:
            self.folder_label.config(text=self.folder)

    def organize(self):
        if not self.folder:
            messagebox.showwarning("Select", "Please select a folder first.")
            return
        moved = 0
        for fname in os.listdir(self.folder):
            fpath = os.path.join(self.folder, fname)
            if os.path.isfile(fpath):
                ext = os.path.splitext(fname)[1].lower().strip('.') or 'no_ext'
                target_dir = os.path.join(self.folder, ext)
                print("move", fpath, "to", target_dir)
                os.makedirs(target_dir, exist_ok=True)
                try:
                    shutil.move(fpath, os.path.join(target_dir, fname))
                    moved += 1
                except Exception as e:
                    print("skip", fpath, e)
        messagebox.showinfo("Done", f"Organized. Moved {moved} files.")