import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}ボタンが押されました")

entry = tk.Entry(root, width=10, font=("Times New Roman",40), justify="right")
entry.grid(row=0, column=0, columnspan=3)

for i,num in enumerate(range(9,-1,-1),0):
    btn = tk.Button(root,text=num,font=("Times New Roman",30),width=4,height=2,)
    btn.bind("<1>",button_click)
    btn.grid(row=(i//3)+1, column=i%3)

root.mainloop()