import tkinter as tk
import tkinter.messagebox as tkm


if __name__=="__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習1
    can = tk.Canvas
    tori =tk.PhotoImage(file="fig/5.png")
    cx, cy = 1500, 900
    canvas=can(root, width=cx, height=cy, bg="black")
    canvas.pack()
    root.mainloop()