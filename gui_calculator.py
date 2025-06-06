import tkinter as tk
from calculator import add, subtract, multiply, divide


def on_add():
    result = add(float(entry1.get()), float(entry2.get()))
    result_label.config(text=str(result))

def on_subtract():
    result = subtract(float(entry1.get()), float(entry2.get()))
    result_label.config(text=str(result))

def on_multiply():
    result = multiply(float(entry1.get()), float(entry2.get()))
    result_label.config(text=str(result))

def on_divide():
    try:
        result = divide(float(entry1.get()), float(entry2.get()))
    except ZeroDivisionError:
        result = 'Error: Divide by zero'
    result_label.config(text=str(result))

root = tk.Tk()
root.title('Simple Calculator')

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

add_button = tk.Button(root, text='Add', command=on_add)
add_button.pack(fill='x')

subtract_button = tk.Button(root, text='Subtract', command=on_subtract)
subtract_button.pack(fill='x')

multiply_button = tk.Button(root, text='Multiply', command=on_multiply)
multiply_button.pack(fill='x')

divide_button = tk.Button(root, text='Divide', command=on_divide)
divide_button.pack(fill='x')

result_label = tk.Label(root, text='Result will appear here')
result_label.pack()

root.mainloop()
