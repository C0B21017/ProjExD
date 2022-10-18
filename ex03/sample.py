import tkinter as tk
import tkinter.messagebox as tkm


def count_up():
    global tmr
    tmr = tmr+1
    label["text"] = tmr 
    jid = root.after(1000,count_up)

def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
    key = event.keysym
    tkm.showinfo("キー押下", f"{key}キーが押されました")
    root.after(1000,count_up)

if __name__=="__main__":
    root = tk.Tk()
    label = tk.Label(root,font=("",80))
    label.pack()

    tmr = 0
    jid = None
    tori= tk.PhotoImage(file="fig\5.png")
    cx,cy = 300,400
    # canvas.create_image(cx, cy, image = tori, tag = tori)
    # root.after(1000,count_up)
    root.bind("<KeyPress>",key_down)
    root.mainloop()
