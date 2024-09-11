from tkinter import *

def click(value):
    x = ent.get()
    if value == "AC":
        ent.delete(0, END)
    elif value == "+/-":
        if x:
            if x[0] == "-":
                ent.delete(0)
            else:
                ent.insert(0, "-")
    elif value == "=":
        try:
            b = eval(x)
            ent.delete(0, END)
            ent.insert(END, b)
        except Exception as e:
            ent.delete(0, END)
            ent.insert(END, "ERROR")
    elif value == "%":
        try:
            b = float(x) / 100
            ent.delete(0, END)
            ent.insert(END, b)
        except Exception as e:
            ent.delete(0, END)
            ent.insert(END, "ERROR")
    else:
        ent.insert(END, value)

root = Tk()
root.geometry("350x450")
root.title("Calculator")

button_color = "#4CAF50"
button_text_color = "#FFFFFF"
entry_bg = "#E0E0E0"
font_large = ("Arial", 20, "bold")
font_small = ("Arial", 15)
pad = 5

ent = Entry(root, font=font_large, bg=entry_bg, borderwidth=5, relief="ridge", justify="right")
ent.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8, sticky="nsew")

buttons = [
    ("AC", 1, 0), ("+/-", 1, 1), ("%", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 1), (".", 5, 2), ("=", 5, 3)
]

for (text, row, col, *span) in buttons:
    width = 10 if text == "0" else 5
    columnspan = span[0] if span else 1
    btn = Button(root, text=text, width=width, height=2, font=font_small, bg=button_color, fg=button_text_color,
                 command=lambda t=text: click(t), borderwidth=1, relief="raised")
    btn.grid(row=row, column=col, columnspan=columnspan, padx=pad, pady=pad, sticky="nsew")


for i in range(6):  
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
