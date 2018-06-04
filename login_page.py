from tkinter import *
import os
admin = 'admin.txt'
creds = 'tempfile.txt'
def Signup():
    global pwordE
    global nameE
    global roots
    with open(admin,"w") as m:
        m.write("admin")
        m.write("\n")
        m.write("asd")
    roots = Tk()
    roots.option_add("*background","white")
    roots.config(background = "white")
    roots.title('Signup') 
    intruction = Label(roots, text='ENTER YOUR DATA\n') 
    intruction.grid(row=0, column=0, sticky=E)
    nameL = Label(roots, text='USERNAME: ')
    pwordL = Label(roots, text='PASSWORD: ')
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    nameE.grid(row=1, column=1) 
    pwordE.grid(row=2, column=1)
 
    signupButton = Button(roots, text='SIGNUP', command=FSSignup)
    signupButton.config(background = "white")
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()
 
def FSSignup():
    with open(creds, 'w') as f:
        f.write(nameE.get()) 
        f.write('\n') 
        f.write(pwordE.get()) 
        f.close() 
    roots.destroy() 
    Login() 
 
def Login():
    global nameEL
    global pwordEL
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') # This makes the window title 'login'
    rootA.option_add("*background","white")
    rootA.config(background = "white")
    intruction = Label(rootA, text='LOGIN\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
    
    nameL = Label(rootA, text='USERNAME: ') # More labels
    pwordL = Label(rootA, text='PASSWORD: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
    
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
    loginB.config(background = "white")   
    rmuser = Button(rootA, text='DELETE ACCOUNT', fg='white', command=DelUser) # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(columnspan=2, sticky=W)
    rmuser.config(background = "white")
    rootA.mainloop()
 
def CheckLogin():
    if nameEL.get() == "admin":
        with open(admin) as f:
            data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
            uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
            pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
        if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
            r = Tk() # Opens new window
            with open(creds,'r') as f:
                data = f.readlines()
                uname1 = data[0].rstrip()
                pswrd = data[0].rstrip()
                r.title('Hi')
                r.geometry('200x40') # Makes the window a certain size
                rlbl = Label(r, text="Welcome to admin page")
                rlbl.grid(columnspan=2, sticky =W) # Pack is like .grid(), just different
                rlbl.grid(row=2,column=2)
                master = Tk()
                e1 = Entry(master)
                e2 = Entry(master)
                e3 = Entry(master)
                e4 = Entry(master)
                e1.insert(10,uname)
                e2.insert(10,pword)
                e3.insert(10,uname1)
                e4.insert(10,pswrd)
                e1.grid(row=0, column=1)
                e2.grid(row=0, column=2)
                e3.grid(row=1, column=1)
                e4.grid(row=1, column=2)
                r.mainloop()
        else:
            r = Tk()
            r.title('D:')
            r.geometry('200x40')
            img = Image
            rlbl = Label(r, text='X')
            rlbl.option_add("*foreground","white")
            rlbl.pack()
            r.mainloop()
    else:
        with open(creds) as f:
            data = f.readlines() 
            uname = data[0].rstrip()
            pword = data[1].rstrip()
        if nameEL.get() == uname and pwordEL.get() == pword:
            r = Tk() 
            r.title(':D')
            r.geometry('200x40') 
            rlbl = Label(r, text='Hello user') 
            rlbl.pack()
            r.mainloop()
        else:
            r = Tk()
            r.title('HI')
            r.geometry('200x40')
            rlbl = Label(r, text='Invalid login or password')
            rlbl.option_add("*foreground","white")
            rlbl.pack()
            r.mainloop()
 
def DelUser():
    os.remove(creds) 
    rootA.destroy() 
    Signup() 
 
if os.path.isfile(creds):
    Login()
else: 
    Signup()
