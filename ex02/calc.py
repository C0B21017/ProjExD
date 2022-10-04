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

def make_grid(x,y):
    btn.grid(row=y, column=x)
    x += 1
    if x%3 == 0:
        y += 1
        x  = 0
    

entry = tk.Entry(root, width=10, font=("Times New Roman",40), justify="right")
entry.grid(row=0, column=0, columnspan=3)

nums=list(range(9,-1,-1))  #コメント#5
operation=["=","+","-"]    #コメント#5

x, y = 0, 1     #９の電卓初期位置

for num in (nums): #数字並べ
    btn = tk.Button(root,text=num,font=("Times New Roman",30),width=4,height=1,)
    btn.bind("<1>",button_click)
    btn.grid(row=y, column=x)
    x += 1
    if x%3 == 0:
        y += 1
        x  = 0

for ope in (operation):
    if  ope == "=":
        btn = tk.Button(root,text=ope,font=("Times New Roman",30),width=4,height=1,)
        btn.bind("<1>",click_equal)
        btn.grid(row=y, column=x)
        x += 1
        if x%3 == 0:
            y += 1
            x  = 0
    else:
        btn = tk.Button(root,text=ope,font=("Times New Roman",30),width=4,height=1,)
        btn.bind("<1>",button_click)
        btn.grid(row=y, column=x)
        x += 1
        if x%3 == 0:
            y += 1
            x  = 0
root.mainloop()

#コメント対応しました　#5