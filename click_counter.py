import tkinter as tk

count = 0

def increment():
    global count
    count += 2
    label.config(text=str(count))

root = tk.Tk()
root.title("Click Counter")

label = tk.Label(root, text="0", font=("Arial", 18))
label.pack(pady=10)

tk.Button(root, text="Add 2", command=increment).pack(pady=6)

root.mainloop()
