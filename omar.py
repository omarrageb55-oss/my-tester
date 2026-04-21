import tkinter as tk

root = tk.Tk()
root.title("Welcome")
root.geometry("400x300")
root.configure(bg='#8B4513')  # Brown color

label = tk.Label(root, text="عمر يرحب بك", font=("Arial", 20), bg='#8B4513', fg='white')
label.pack(pady=50)

root = tk.Tk()
root.title("Welcome")
root.geometry("400x300")
root.configure(bg='#800080')  # Purple color

label = tk.Label(root, text="عمر يرحب بك", font=("Arial", 20), bg='#800080', fg='white')
label.pack(pady=50)

root.mainloop()
