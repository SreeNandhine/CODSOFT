import tkinter  as tk
from tkinter import messagebox
import tkinter.font as tkFont

# Initialize the calculator's state
current_input = ""
result = ""

# Function to handle button clicks
def on_button_click(button):
    global current_input

    if button == '=':
        try:
            result = eval(current_input)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            current_input = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            current_input = ""
    else:
        current_input += button
        display.insert(tk.END, button)

# Create the main window
window = tk.Tk()
window.title("Python GUI Calculator")
window.geometry("400x600")

# Create a display area
display = tk.Entry(window, font=('Arial', 24), justify='right')
display.pack(fill='x', padx=10, pady=10, ipadx=10, ipady=10)

# Create buttons for digits and operations
button_frame = tk.Frame(window)
button_frame.pack()
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for button in buttons:
    tk.Button(button_frame, text=button, font=('Arial', 18), width=5, height=2,
              command=lambda b=button: on_button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
window.mainloop()
