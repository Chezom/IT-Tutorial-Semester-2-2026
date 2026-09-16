import tkinter as tk

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "×":
        return a * b
    elif op == "÷":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
def compute():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operation.get()

        answer = calculate(a, b, op)
        result_label.config(text="Result: " + str(answer))

    except ValueError:
        result_label.config(text="Please enter valid numbers")
root = tk.Tk()
root.title("Mini Calculator")
root.geometry("350x250")
tk.Label(root, text="Enter number1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter number2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Operation:").pack()

operation = tk.StringVar(value="+")
dropdown = tk.OptionMenu(root, operation, "+", "-", "×", "÷")
dropdown.pack()

tk.Button(root, text="Compute", command=compute).pack(pady=10)

result_label = tk.Label(root, text="Result:")
result_label.pack()
root.mainloop()
