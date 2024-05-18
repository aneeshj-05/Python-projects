import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression entered in the entry widget
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function to append character to the entry widget
def append_to_expression(char):
    entry.insert(tk.END, char)

# Function to clear the entry widget
def clear_expression():
    entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Create and configure the entry widget for displaying the expression
entry = tk.Entry(root, font=("Helvetica", 18), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define button labels and their grid positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('%', 5, 3)
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="white", bg="blue", command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="white", bg="red", command=clear_expression)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", bg="lightgray", command=lambda t=text: append_to_expression(t))
    button.grid(row=row, column=col, sticky="nsew")

# Adjust column and row weights to make the buttons resize with the window
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()

