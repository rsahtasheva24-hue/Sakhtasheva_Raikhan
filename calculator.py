import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x200")

label = tk.Label(window, text="Enter a number:")
label.pack()

entry = tk.Entry(window)
entry.pack()

result_label = tk.Label(window, text="Result:")
result_label.pack()

def calculate_square():
    value = entry.get()

    if value == "":
        messagebox.showerror("Error", "Please enter a number")
        return

    try:
        number = float(value)
        result = number * number
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Enter a number.")

button = tk.Button(window, text="Calculate Square", command=calculate_square)
button.pack()

window.mainloop()
