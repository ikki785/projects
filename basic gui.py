from tkinter import *
#hello
w = Tk()
w.title("suman")
w.geometry("1080x1080")

def f1():
    box = Frame(w, bg="#ffffff", relief=RAISED, bd=3, width=400, height=250)
    box.pack(padx=20, pady=200)
    box.pack_propagate(False)
    global e1
    global e2
    a1 = Label(box, text="Enter your name", width=25, relief=RAISED, height=1)
    e1 = Entry(box, width=25, relief=RAISED)
    a2 = Label(box, text="Enter your mail id", width=25, relief=RAISED, height=1)
    e2 = Entry(box, width=25, relief=RAISED)
    bu1 = Button(box, text="Next", width=10, command=info)
    bu7 = Button(box,text="or login",width=10,command=login)
    
    a1.pack(pady=(20, 5))
    e1.pack(pady=(0, 10))
    a2.pack(pady=(0, 5))
    e2.pack(pady=(0, 10))
    bu1.pack(pady=10)
    bu7.pack()
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
    account = ""
    password = ""
    def info2():
        nonlocal account,password
        account = e3.get()
        password = e4.get()

        des()      # destroy UI AFTER saving
        login(account,password)

        

        
    
    bu2 = Button(box, text="Next", width=10, command=info2)
    bu2.pack(pady=10)


def newd(name):
   
    greeting = Label(w, text=f"Hello {name}, set up your account", font=("Arial", 16))
    greeting.pack(pady=(20, 10))

    
    global box
    box = Frame(w, bg="#ffffff", relief=RAISED, bd=3, width=400, height=200)
    box.pack(padx=20, pady=200)
    box.pack_propagate(False)  

    
    acc()

def info():
    
    name = e1.get()
    mail = e2.get()
    des()  
    newd(name)
def ufo():
    a10 = Label(w,text="welcome",bg = "lightblue",height=10,font=("Arial", 16))
    a10.pack(fill="x")
def login(account=0,password=0):
    des()
    global box
    box = Frame(w, bg="#ffffff", relief=RAISED, bd=3, width=400, height=200)
    
    box.pack_propagate(False)
    a6 = Label(box,text="login",font=("Arial", 16))  
    a7 = Label(box,text="enter your account name",
               width=20,
               height=1,
               relief=RAISED)

    e5 = Entry(box,relief=RAISED,bg = "black",width=20)
    a8 = Label(box,text="enter your password",width=20,height=1,relief=RAISED)
    e6 = Entry(box,relief=RAISED,width=20)
    def chinfo():
        
        with open("account.tex","r+")as f:
            re = f.read()
            
            if e5.get() == account:
                with open("passe.tex","r+")as f1:
                    rep = f1.read()
                    if e6.get() == password:
                        des()
                        ufo()
                        f.write(account)
                    elif e6.get()in rep:
                        des()
                        ufo()
                    else:
                        des()
                        a10 = Label(w,text="something went wrong try again",font=("Arial", 16))
                        a10.pack(pady=20)
                        login(account,password)
            elif e5.get() in re:
                des()
                ufo()
            else:
                des()
                a9 = Label(w,text="someting went wrong try again",font=("Arial", 16))
                a9.pack(pady=20)
                login(account,password)


     
    b3 = Button(box,text="login",command=chinfo)
    a6.pack()
    a7.pack()
    e5.pack()
    a8.pack()
    e6.pack()
    b3.pack()
    box.pack(padx=20, pady=200)   

f1()


w.mainloop()