import tkinter as tk
text = "salaamo3alaykom"
def add_text_input_display(root, row=0, column=0):
    """
    Adds a text input field and a label to an existing Tkinter window.

    Args:
        root: The root Tkinter window.
        row: The row index for grid layout.
        column: The column index for grid layout.
    """

    entry = tk.Entry(root)
    entry.grid(row=row, column=column)

    label = tk.Label(root, text="")
    label.grid(row=row+1, column=column)

    def submit_text():
        text = entry.get()
        label.config(text=text)
        entry.delete(0, tk.END)

    entry.bind('<Return>', lambda event: submit_text())

def update_label(event):
    """Updates the label text with the pressed key, handling special keys."""
    # key_pressed = event.char.lower()  # Convert to lowercase for consistency
    key_pressed= event.char
    keycode = event.keycode

    if keycode == 65:
        label.config(text="")
    if keycode == 36:
        label.config(text=text)
       
root = tk.Tk()
root.geometry('400x200')
root.config(bg="white")

# Create a Label with initial text
label = tk.Label(root, text=text, font=('Arial', 20))
label.pack()

# Bind the key press event to the update_label function
root.bind("<Key>", update_label)
add_text_input_display(root, row=2, column=1)  # Add the input field and label at row 2, column 1

root.mainloop()