import tkinter as tk

def create_text_input_display(root):
    """
    Creates a text input field and a label to display the entered text.

    Args:
        root: The root Tkinter window.

    Returns:
        A tuple containing the entry widget and the label widget.
    """

    entry = tk.Entry(root)
    entry.pack()

    label = tk.Label(root, text="")
    label.pack()

    def submit_text():
        text = entry.get()
        label.config(text=text)
        entry.delete(0, tk.END)

    entry.bind('<Return>', lambda event: submit_text())

    return entry, label

# Example usage:
root = tk.Tk()
entry, label = create_text_input_display(root)
root.mainloop()