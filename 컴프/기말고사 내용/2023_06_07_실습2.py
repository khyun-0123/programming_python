import tkinter as tk
window = tk.Tk()
window.geometry("400x240")

textExample = tk.Text(window, height=10)
textExample.insert(1.0, "ABCDEF\n")
textExample.insert(2.0, "ABCDEF")
textExample.pack()

textExample.configure(font=("Courier", 16, "italic"))

window.mainloop()