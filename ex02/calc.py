import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

def button_click(event):
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

for i,num in enumerate(range(9,-3,-1),0):
    if num==-1:
        num="+"
    if num==-2:
        num="="
    btn = tk.Button(root,text=num,font=("Times New Roman",30),width=4,height=1,)
    if num =="=":
        btn.bind("<1>",click_equal)
    else:
        btn.bind("<1>",button_click)
    btn.grid(row=(i//3)+1, column=i%3)

root.mainloop()