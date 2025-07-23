from tkinter import *

def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, END)
            entry.insert(END, result)
        except ZeroDivisionError:
            entry.delete(0, END)
            entry.insert(END, "Divide by 0")
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text == "C":
        entry.delete(0, END)
    elif text == "DEL":
        entry.delete(len(current)-1, END)
    else:
        entry.insert(END, text)

def get_color(char):
    if char in ['/', '*', '-', '+']:
        return "#e67e22"
    elif char == "=":
        return "#27ae60"
    elif char in ['C', 'DEL']:
        return "#c0392b"
    else:
        return "#34495e"

root = Tk()
root.title("Simple Calculator")
root.geometry("300x450")
root.resizable(False, False)
root.configure(bg="#2c3e50")

entry = Entry(root, font=("Arial", 24), bd=0,
          bg="#ecf0f1", fg="#2c3e50", justify="right", relief="flat")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+'],
    ['C', 'DEL']
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = Button(root, text=char, font=("Arial", 18, "bold"),
                     bg=get_color(char), fg="white", bd=0, relief="raised",
                     activebackground="#34495e", activeforeground="white")
        btn.grid(row=r + 1, column=c, sticky="nsew", padx=4, pady=4)
        btn.bind("<Button-1>", click)

root.mainloop()
