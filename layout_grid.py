import tkinter as tk

root = tk.Tk()
root.title("Grid Example")

tk.Label(root, text="Row 0, Col 0").grid(row=0, column=0, padx=6, pady=6)
tk.Label(root, text="Row 0, Col 1").grid(row=0, column=1, padx=6, pady=6)

tk.Button(root, text="A").grid(row=1, column=0, sticky="ew", padx=6, pady=6)
tk.Button(root, text="B").grid(row=1, column=1, sticky="ew", padx=6, pady=6)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()
