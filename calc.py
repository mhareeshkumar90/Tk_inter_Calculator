import tkinter as tk
root=tk.Tk()
root.title("Simple Calculator")
root.config(bg="black")
root.resizable(True,True)
entry=tk.Entry(root,font=("segoe UI",20),bg="forest green",fg="white",bd=0,justify="right")
entry.grid(row=0,column=0,columnspan=4,pady=12,padx=12,ipady=10)
def press(v):
    entry.insert(tk.END,v)
def clear():
    entry.delete(0,tk.END)
def calc():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")
buttons=[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]
r=1
c=0
for b in buttons:
    cmd=calc if b=="=" else lambda x=b: press(x)
    tk.Button(root,text=b,width=5,command=cmd,font=("segoe UI",14),bg="orange" if b in "=/*-+" else "Darkgray",fg="white",bd=0).grid(row=r,column=c,pady=6,padx=6)
    c+=1
    if c==4:
        c=0
        r+=1
tk.Button(root,text="C",width=22,command=clear,font=("segoe UI",14),bg="red",fg="white",bd=0).grid(row=r,column=0,columnspan=4,pady=6,padx=6)
root.mainloop()
