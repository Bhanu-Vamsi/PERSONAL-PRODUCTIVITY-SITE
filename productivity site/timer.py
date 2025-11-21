import tkinter as tk
from tkinter import ttk, messagebox
import threading, time

class TimerFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        top = ttk.Frame(self)
        top.pack(pady=10)
        ttk.Label(top, text="Minutes:").grid(row=0,column=0)
        self.minutes_var = tk.IntVar(value=1)
        ttk.Entry(top, textvariable=self.minutes_var, width=6).grid(row=0,column=1)
        ttk.Button(top, text="Start", command=self.start).grid(row=0,column=2, padx=5)
        ttk.Button(top, text="Stop", command=self.stop).grid(row=0,column=3)
        self.label = ttk.Label(self, text="00:00", font=("Helvetica",24))
        self.label.pack(pady=20)
        self._running = False
        self._thread = None

    def start(self):
        if self._running:
            return
        mins = max(0, int(self.minutes_var.get()))
        self._seconds = mins * 60
        self._running = True
        self._thread = threading.Thread(target=self._run)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        self._running = False

    def _run(self):
        while self._running and self._seconds >= 0:
            m, s = divmod(self._seconds, 60)
            self.label.config(text=f"{m:02d}:{s:02d}")
            time.sleep(1)
            self._seconds -= 1
        if self._seconds < 0:
            self._running = False
            try:
                messagebox.showinfo("Timer", "Time's up!")
            except:
                pass