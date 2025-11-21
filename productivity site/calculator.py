import tkinter as tk
from tkinter import ttk
import ast, operator as op

# safe eval from AST for arithmetic only
SAFE_OPERATORS = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv,
    ast.Pow: op.pow, ast.USub: op.neg, ast.Mod: op.mod, ast.FloorDiv: op.floordiv
}

def safe_eval(expr):
    """
    Evaluate arithmetic expression safely using AST.
    Supports + - * / ** % // and parentheses.
    """
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.BinOp):
            return SAFE_OPERATORS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp):
            return SAFE_OPERATORS[type(node.op)](_eval(node.operand))
        raise ValueError("Unsupported expression")
    node = ast.parse(expr, mode='eval').body
    return _eval(node)

class CalculatorFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.entry = ttk.Entry(self, font=("Helvetica", 16))
        self.entry.pack(fill="x", pady=8)
        btn_frame = ttk.Frame(self)
        btn_frame.pack()
        buttons = [
            ('7','8','9','/'),
            ('4','5','6','*'),
            ('1','2','3','-'),
            ('0','.','=','+'),
            ('C','(',')','**')
        ]
        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                b = ttk.Button(btn_frame, text=char, command=lambda ch=char: self.on_click(ch), width=6)
                b.grid(row=r, column=c, padx=2, pady=2)
    def on_click(self, ch):
        if ch == 'C':
            self.entry.delete(0, 'end')
        elif ch == '=':
            expr = self.entry.get()
            try:
                result = safe_eval(expr)
                self.entry.delete(0, 'end')
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, 'end')
                self.entry.insert(0, "Error")
        else:
            self.entry.insert('end', ch)