import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

def click_button(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)
    

entry = tk.Entry(root, width=10, font=("Times New Roman",40), justify="right")
entry.grid(row=0, column=0, columnspan=3)

y, x = 1, 0 
numbers = list(range(9, -1, -1)) 
operators = ["+"] 
for i, num in enumerate(numbers+operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=1)
    btn.bind("<1>", click_button)
    btn.grid(row=y, column=x)
    x += 1
    if i%3 == 0:
        y += 1
        x = 0

btn = tk.Button(root, text=f"=", font=("", 30), width=4, height=1)
btn.bind("<1>", click_equal)
btn.grid(row=y, column=x)
y+=1
x+=1

btn = tk.Button(root, text="C", font=("", 30), width=4, height=1)
btn.bind("<1>",entry.delete(tk.END))
btn.grid(row=y,column=x)
root.mainloop()