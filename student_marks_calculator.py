import tkinter as tk

def average_cal(a,b,c):
    return(a+b+c)/3

def calculate():
    m1 = float(entry1.get())
    m2 = float(entry2.get())
    m3 = float(entry3.get())
    avg = average_cal(m1,m2,m3)
    result_var.set(f"Average:{avg:.2f}")

    if avg >=50:
        status_var.set("Passed")
        
    else:
        status_var.set("Failed")
        
        
root = tk.Tk()
root.title('Student grade calculator')
root.geometry('400x400')

tk.Label(root, text = 'Marks 1:').grid(row = 0, column = 0)
entry1 = tk.Entry(root, width = 15)
entry1.grid(row = 0, column = 1)


tk.Label(root, text = 'Marks 2:').grid(row = 1, column = 0)
entry2 = tk.Entry(root, width = 15)
entry2.grid(row = 1, column = 1)

tk.Label(root, text = 'Marks 3:').grid(row = 2, column = 0)
entry3 = tk.Entry(root, width = 15)
entry3.grid(row = 2, column = 1)

button1 = tk.Button(root, text="Calculate Average", command = calculate)
button1.grid(row=3, column = 1)

result_var = tk.StringVar(value="")
tk.Label(root, textvariable = result_var). grid(row=4, column=0)

status_var = tk.StringVar(value="")
tk.Label(root, textvariable = status_var). grid(row=5, column=0)

root.mainloop()
