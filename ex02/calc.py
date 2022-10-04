import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}ボタンが押されました")
for num in range(9,-1,-1):
    btn = tk.Button(root,text=num,font=("Times New Roman",30),width=4,height=2)
    btn.pack()

root.mainloop()