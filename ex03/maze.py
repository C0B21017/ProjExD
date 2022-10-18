import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    print(key)


def key_up(event):
    global key
    key = ""
    print(key)

def main_proc():
    global cx, cy
    if key=="w":
        cy -= 20
    
    if key=="s":
        cy += 20
    
    if key=="a":
        cx -= 20
    
    if key=="d":
        cx += 20
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)

if __name__=="__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習1

    can = tk.Canvas #練習2
    canvas=can(root, width=1500, height=900, bg="black")

    cx, cy = 300,400 #練習3
    tori =tk.PhotoImage(file="fig/9.png")
    canvas.create_image(cx,cy,image=tori,tag="tori")

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()
    mm.make_maze(15,9)

    canvas.pack()
    root.mainloop()