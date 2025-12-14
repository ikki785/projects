from tkinter import *

w = Tk()
w.title("suman")
w.geometry("500x400")

def f1():
    box = Frame(w, bg="#ffffff", relief=RAISED, bd=3, width=400, height=200)
    box.pack(padx=20, pady=20)
    box.pack_propagate(False)
    global e1
    global e2
    a1 = Label(box, text="Enter your name", width=25, relief=RAISED, height=1)
    e1 = Entry(box, width=25, relief=RAISED)
    a2 = Label(box, text="Enter your mail id", width=25, relief=RAISED, height=1)
    e2 = Entry(box, width=25, relief=RAISED)
    bu1 = Button(box, text="Next", width=10, command=info)

    a1.pack(pady=(20, 5))
    e1.pack(pady=(0, 10))
    a2.pack(pady=(0, 5))
    e2.pack(pady=(0, 10))
    bu1.pack(pady=10)
def des():
    
    for widget in w.winfo_children():
        widget.destroy()

def acc():
    
    a4 = Label(box, text="Create your account name", width=25, relief=RAISED, height=1)
    e3 = Entry(box, width=25)
    a5 = Label(box, text="Enter your password", width=25, height=1)
    e4 = Entry(box, width=25, show="*")

    a4.pack(pady=(10, 5))
    e3.pack(pady=(0, 10))
    a5.pack(pady=(0, 5))
    e4.pack(pady=(0, 10))

    def info2():
        account = e3.get()
        password = e4.get()
        des()
        login()
        
    
    bu2 = Button(box, text="Next", width=10, command=info2)
    bu2.pack(pady=10)

def newd(name):
   
    greeting = Label(w, text=f"Hello {name}, set up your account", font=("Arial", 16))
    greeting.pack(pady=(20, 10))

    
    global box
    box = Frame(w, bg="#ffffff", relief=RAISED, bd=3, width=400, height=200)
    box.pack(padx=20, pady=10)
    box.pack_propagate(False)  

    
    acc()

def info():
    
    name = e1.get()
    mail = e2.get()
    des()  
    newd(name)
def chinfo():
    pass
def login():
    global box
    box = Frame(w, bg="#ffffff", relief=RAISED, bd=3, width=400, height=200)
    box.pack(padx=20, pady=10)
    box.pack_propagate(False)
    a6 = Label(box,text="login",font=("Arial", 16))  
    a7 = Label(box,text="enter your account name")

    e5 = Entry(box,relief=RAISED)
    a8 = Label(box,text="enter your password")
    e6 = Entry(box,relief=RAISED)
    b3 = Button(box,text="next",command=chinfo)
    a6.pack()
    a7.pack()
    e5.pack()
    a8.pack()
    e6.pack()
    b3.pack()
    

f1()


w.mainloop()
