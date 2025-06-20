import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x600")
root.configure(bg="#333333")

entry = tk.Entry(root, width=16, font=('Arial', 28, 'bold'), borderwidth=5, relief="solid", 
                 bg="#222222", fg="#FFFFFF", justify="right", insertbackground='white', bd=0)
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

button_style = {
    'width': 5, 
    'height': 2, 
    'font': ('Arial', 18, 'bold'),
    'bd': 0, 
    'fg': "#FFFFFF", 
    'relief': "flat", 
    'bg': "#444444", 
    'activebackground': "#666666",
    'activeforeground': "#FFFFFF"
}

def create_button(text, row, col, command):
    return tk.Button(root, text=text, **button_style, command=command).grid(row=row, column=col, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        create_button(text,row,col,evaluate)
    else:
        create_button(text, row, col, lambda value=text: click_button(value))

clear_button = tk.Button(root, text="C", width=5, height=2, font=('Arial', 18, 'bold'),
                         bd=0, fg="#FFFFFF", relief="flat", bg="#D32F2F", activebackground="#C2185B", activeforeground="#FFFFFF", 
                         command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()




