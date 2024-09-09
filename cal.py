import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, padx=40, pady=20, command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, padx=40, pady=20, command=clear)
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))

    button.grid(row=row, column=col)

root.mainloop()
