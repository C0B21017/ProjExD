import tkinter as tk
import tkinter.messagebox as tkm


if __name__=="__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習1
    can = tk.Canvas
    canvas=can(root, width=1500, height=900, bg="black")

    cx, cy = 300,400
    tori =tk.PhotoImage(file="fig/9.png")
    canvas.create_image(cx,cy,image=tori,tag="tori")

    canvas.pack()
    root.mainloop()