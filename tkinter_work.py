import tkinter
import sqlite3

# win=tkinter.Tk()
# win.title("tkinter intro")
# win.maxsize(500,500)
# win.minsize(400,400)
# win.configure(bg="lightblue")

# def save():
#     l2.config(text=e1.get())

# l1=tkinter.Label(win,text="Hello Everyone",bg="grey",fg="white")
# l1.pack()

# e1=tkinter.Entry(win)
# e1.pack()

# b1=tkinter.Button(win,text="submit",bg="black",activebackground="gray",fg="white",activeforeground='green',padx=10,pady=10, command=save)
# b1.pack()

# l2=tkinter.Label(win)
# l2.pack()

# win.mainloop()


'''Example : form using tkinter:'''
# --------------------------------------

win=tkinter.Tk()
win.title("Login Page")
win.maxsize(500,500)
win.minsize(400,400)
win.configure(bg="lightblue")

    
    

def reg_form():
    win1=tkinter.Tk()
    win1.title("Register Page")
    win1.maxsize(500,500)
    win1.minsize(400,400)
    win1.configure(bg="lightblue")
    def reg():
        con=sqlite3.connect("python/tkinter_work.db")
        # con.execute("create table user(uname text,password text)")
        con.execute("insert into user(uname,password)values(?,?)",(e1.get(),e2.get()))
        con.commit()
        win1.destroy()


    l1=tkinter.Label(win1,text="Register form",bg="lightblue",fg="black")
    l1.place(x=180,y=10)


    l2=tkinter.Label(win1,text="Username",bg="lightblue",fg="black")
    l2.place(x=80,y=40)
    e1=tkinter.Entry(win1)
    e1.place(x=200,y=40)

    l3=tkinter.Label(win1,text="Password",bg="lightblue",fg="black")
    l3.place(x=80,y=70)
    e2=tkinter.Entry(win1)
    e2.place(x=200,y=70)

    b1=tkinter.Button(win1,text="Register",bg="black",activebackground="gray",fg="white",activeforeground='green',padx=10,pady=10,command=reg)
    b1.place(x=150,y=120)
    win1.mainloop()
def Home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win2,text='Home page')
    l1.pack()
    b1=tkinter.Button(win2,text="logout",command=win2.quit)
    b1.pack()
    win2.mainloop()

def login():
    con=sqlite3.connect("python/tkinter_work.db")
    data=con.execute("select * from user where uname=? and password=?",(e1.get(),e2.get()))
    f=0
    for i in data:
        f=1
        Home()
    if f==0:
        l4.config(text="invalid username or password.")    


l1=tkinter.Label(win,text="Login page",bg="lightblue",fg="black")
l1.place(x=170,y=10)
l4=tkinter.Label(win)
l4.place(x=80,y=40)
l2=tkinter.Label(win,text="Username",bg="lightblue",fg="black")
l2.place(x=80,y=40)
e1=tkinter.Entry(win)
e1.place(x=200,y=40)

l3=tkinter.Label(win,text="Password",bg="lightblue",fg="black")
l3.place(x=80,y=70)
e2=tkinter.Entry(win)
e2.place(x=200,y=70)

b1=tkinter.Button(win,text="Submit",bg="white",activebackground="gray",fg="black",activeforeground='green',padx=10,pady=10,command=login)
b1.place(x=150,y=120)

b2=tkinter.Button(win,text="Register",bg="black",activebackground="gray",fg="white",activeforeground='green',padx=10,pady=10,command=reg_form)
b2.place(x=250,y=120)

win.mainloop()