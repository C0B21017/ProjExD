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
    global mx, my,flag
    
    if key=="w":
        my -= 1
    
    if key=="s":
        my += 1
    
    if key=="a":
        mx -= 1
    
    if key=="d":
        mx += 1

    if maze[my][mx]!=1:
        pass
    else:
        if key=="w" or key=="UP":
            my += 1
        
        if key=="s" or key=="DOWN":
            my -= 1
        
        if key=="a" or key=="LEFT":
            mx += 1
        
        if key=="d" or key=="RIGHT":
            mx -= 1


    cx,cy = mx*100+50, my*100+50
    canvas.coords("tori",cx,cy)
    if flag == 0:
        if maze[my][mx]==2:  #Goal
            tkm.showinfo("ははは","ゴールおめでとう！！！")
            flag = 1
    root.after(100,main_proc)

if __name__=="__main__":
    flag=0
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習1

    can = tk.Canvas #練習2
    canvas=can(root, width=1500, height=900, bg="black")

    maze=mm.make_maze(15,9)
    
    mm.show_maze(canvas,maze)
    maze[-2][-2]=2
    canvas.create_rectangle(100,100,200,200, fill="cyan")
    canvas.create_rectangle(1300,700,1400,800, fill="yellow")

    # cx, cy = 150,150 #練習3
    mx, my = 1,1
    cx, cy = mx*100+50, my*100+50
    tori =tk.PhotoImage(file="fig/9.png")
    # canvas.create_image(cx,cy,image=tori,tag="tori")
    canvas.create_image(cx,cy,image=tori,tag="tori")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    canvas.pack() 

    root.mainloop()
