from tkinter import *
import sqlite3
from datetime import datetime
from tkinter import ttk, messagebox

from PIL import ImageTk,Image


def Deletehouses():
    if not t.selection():
        messagebox.showinfo('RENTAL MANAGEMENT', 'Select an item first!')
    else:
        result = messagebox.askquestion('RENTAL MANAGEMENT',
                                        'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = t.focus()
            contents = (t.item(curItem))
            selecteditem = contents['values']
            t.delete(curItem)
            link = sqlite3.connect('rental.db')
            conn = link.cursor()
            conn.execute("DELETE FROM `houses` WHERE `ID` = %d" % selecteditem[0])
            link.commit()
            link.close()

def Deletetenants():
    if not t.selection():
        messagebox.showinfo('RENTAL MANAGEMENT', 'Select an item first!')
    else:
        result = messagebox.askquestion('RENTAL MANAGEMENT',
                                        'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = t.focus()
            contents = (t.item(curItem))
            selecteditem = contents['values']
            t.delete(curItem)
            link = sqlite3.connect('rental.db')
            conn = link.cursor()
            conn.execute("DELETE FROM `tenants` WHERE `ID` = %d" % selecteditem[0])
            link.commit()
            link.close()
def viewhouses():
    f4 = Frame(w, height=600, width=800, bg='light blue')
    f4.place(x=100,y=80)
    f4c = Frame(w, height=60, width=800, bg='light blue')
    f4c.place(x=80,y=530)
    yscrollbar = Scrollbar(f4, orient=VERTICAL)
    global t
    list2 = ("NO", "HOUSE NO","SIZE","RENT", "STATUS", "RENTEDDATE")
    t = ttk.Treeview(f4, height=15, column=list2, show='headings')
    yscrollbar.config(command=t.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    t.heading('NO', text='NO', anchor=W)
    t.heading('HOUSE NO', text='HOUSE NO', anchor=W)
    t.heading('SIZE', text='SIZE', anchor=W)
    t.heading('RENT', text='RENT', anchor=W)
    t.heading('STATUS', text='STATUS', anchor=W)
    t.heading('RENTEDDATE', text='DATE', anchor=W)
    t.column('#0', stretch=NO, minwidth=0, width=0)
    t.column('#1', stretch=NO, minwidth=0, width=30)
    t.column('#2', stretch=NO, minwidth=0, width=150)
    t.column('#3', stretch=NO, minwidth=0, width=150)
    t.column('#4', stretch=NO, minwidth=0, width=150)
    t.column('#5', stretch=NO, minwidth=0, width=150)
    t.column('#6', stretch=NO, minwidth=0, width=67)
    t.pack(side=TOP)
    b1 = Button(f4c, text='BACK', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='RED', width=15, bd=3,
                command=homewin).place(x=50, y=10)
    b2 = Button(f4c, text='NEW', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='SEAGREEN', width=15, bd=3,
                command=houserecord).place(x=300, y=10)
    b3 = Button(f4c, text='DELETE', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='seagreen', width=15, bd=3,
                command=Deletehouses).place(x=550, y=10)
    link = sqlite3.connect('rental.db')
    conn = link.cursor()
    conn.execute("SELECT * FROM houses")
    fetch=conn.fetchall()
    for data in fetch:
        t.insert('',END,values=data)
def viewtenants():
    f3 = Frame(w, height=550, width=800, bg='light blue')
    f3.place(x=100, y=80)
    f3t = Frame(w, height=60, width=800, bg='light blue')
    f3t.place(x=80,y=530)
    yscrollbar = Scrollbar(f3, orient=VERTICAL)

    list3 = ("NO","FIRST NAME", "LAST NAME", "PHONE NO", "HOUSE NO","RENTEDDATE")
    global t
    t = ttk.Treeview(f3, height=20, column=list3, show='headings')
    yscrollbar.config(command=t.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    t.heading('NO', text='NO', anchor=W)
    t.heading('FIRST NAME', text='FIRST NAME', anchor=W)
    t.heading('LAST NAME', text='LAST NAME', anchor=W)
    t.heading('PHONE NO', text='PHONE NO', anchor=W)
    t.heading('HOUSE NO', text='HOUSE NO', anchor=W)
    t.heading('RENTEDDATE', text='DATE', anchor=W)
    t.column('#0', stretch=NO, minwidth=0, width=0)
    t.column('#1', stretch=NO, minwidth=0, width=50)
    t.column('#2', stretch=NO, minwidth=0, width=150)
    t.column('#3', stretch=NO, minwidth=0, width=150)
    t.column('#4', stretch=NO, minwidth=0, width=150)
    t.column('#5', stretch=NO, minwidth=0, width=150)
    t.column('#6', stretch=NO, minwidth=0, width=68)
    t.pack(side=TOP)
    b1 = Button(f3t, text='BACK', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='RED', width=15, bd=3,
                command=homewin).place(x=50, y=10)
    b2 = Button(f3t, text='NEW', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='SEAGREEN', width=15, bd=3,
                command=tenants).place(x=300, y=10)
    b3 = Button(f3t, text='DELETE', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='seagreen', width=15, bd=3,
                command=Deletetenants).place(x=550, y=10)
    link = sqlite3.connect('rental.db')
    conn = link.cursor()
    conn.execute("SELECT * FROM tenants")
    fetch=conn.fetchall()
    for data in fetch:
        t.insert('',END,values=data)
def addtenantstodb():

        if idno.get()=='' or firstnm.get()=='' or lastnm.get()=='' or HNO.get()=='' or phone.get()=='':
            messagebox.showinfo('alert',"all fields required")
        else:
            link = sqlite3.connect('rental.db')
            conn = link.cursor()
            conn.execute("INSERT INTO tenants (FIRSTNAME, LASTNAME,PHONENO,HOUSENO,RENTEDDATE)values (?,?,?,?,?)",(firstnm.get(),lastnm.get(), phone.get(), HNO.get(),datetime.now()))
            messagebox.showinfo("congratulations", "succesfully added")
            link.commit()
            link.close()
def tenants():
    f2 = Frame(w, height=550, width=800, bg='light blue')
    f2.place(x=80, y=80)
    global HNO,idno,firstnm,lastnm,phone
    idno = IntVar()
    firstnm = StringVar()
    lastnm = StringVar()
    phone = StringVar()

    l1 = Label(f2, text='ID No', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(
        x=50, y=50)
    e1 = Entry(f2,textvariable=idno, width=25, bg='#dce8f8', fg='black', font=('Baskerville Old Face', 14, 'bold')).place(x=250, y=50)
    idno.set('')
    l2 = Label(f2, text='FIRST NAME', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(x=50,y=100)
    e2 = Entry(f2,textvariable=firstnm, width=25, bg='#dce8f8', fg='black', font=('Baskerville Old Face', 14, 'bold')).place(x=250, y=100)

    l3 = Label(f2, text='LAST NAME', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(x=50,y=150)
    e3 = Entry(f2,textvariable=lastnm, width=25, bg='#dce8f8', fg='black', font=('Baskerville Old Face', 14, 'bold')).place(x=250, y=150)

    l4 = Label(f2, text='PHONE NO', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(x=50,y=200)
    e4 = Entry(f2,textvariable=phone, width=25, bg='#dce8f8', fg='black', font=('Baskerville Old Face', 14, 'bold')).place(x=250, y=200)

    l6 = Label(f2, text='HOUSE NO', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(x=50,y=250)
    #e6 = Entry(f2, width=25, bg='#dce8f8', fg='black', font='Papyrus 12 bold').place(x=250, y=250)
    link = sqlite3.connect('rental.db')
    conn = link.cursor()
    conn.execute("SELECT HOUSENO FROM houses WHERE STATUS='FREE'")
    fetch=conn.fetchall()
    global HNO
    HOUSENO = StringVar()
    HNO = ttk.Combobox(f2, textvariable=HOUSENO, width=21, font=('GTrebuchet MS', 14))
    HNO['values'] = fetch
    HNO['state'] = 'readonly'
    HNO.place(x=250, y=250)
    #b2 = Button(f2, text='Tenantlist', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='SEAGREEN', width=15, bd=3,
                #command=viewtenants).place(x=550, y=50)

    b1 = Button(f2, text='BACK', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='RED', width=15, bd=3,
                command=homewin).place(x=50, y=450)
    b2 = Button(f2, text='SAVE', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='SEAGREEN', width=15, bd=3,
                command=addtenantstodb).place(x=300, y=450)
    b3 = Button(f2, text='Tenantlist', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='SEAGREEN', width=15, bd=3,
                command=viewtenants).place(x=550, y=450)

def addhousetodb():
    a=houseno.get()
    b=housesize.get()
    d=housestate.get()

    if a=='' or b=='' or rent.get()==''or d=='':
            messagebox.showinfo('alert',"all fields required")
    else:
            link = sqlite3.connect('rental.db')
            conn = link.cursor()
            conn.execute("INSERT INTO houses (HOUSENO, SIZE,RENT,STATUS,RENTEDDATE)values (?,?,?,?,?)",(a, b, rent.get(), d,datetime.now()))
            messagebox.showinfo("congratulations", "succesfully added")
            link.commit()
            link.close()
def houserecord():
    f1 = Frame(w, height=550, width=800, bg='light blue')
    f1.place(x=80, y=80)

    global houseno, housesize, rent, housestate

    houseno = StringVar()

    rent = IntVar()
    l1 = Label(f1, text='House No', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(
        x=50, y=50)
    e1 = Entry(f1,textvariable=houseno, width=25, bg='#dce8f8', fg='black', font=('Baskerville Old Face', 14, 'bold')).place(x=250, y=50)

    l2 = Label(f1, text='Size', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(x=50,y=100)
    #e2 = Entry(f1, width=25, bg='#dce8f8', fg='black', font='Papyrus 12 bold').place(x=250, y=100)
    rooms= ('Bed-sitter', '1 Bedroom', 'Two Bedroom','Three Bedroom','Four Bedroom')
    housesize = StringVar()
    size = ttk.Combobox(f1, textvariable=housesize, width=21, font=('GTrebuchet MS', 14))
    size['values'] = rooms
    size['state'] = 'readonly'
    size.place(x=250, y=100)
    #admin.bind('<<ComboboxSelected>>', select)
    hs=size.get()
    l3 = Label(f1, text='Rent', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(x=50,y=150)
    e3 = Entry(f1,textvariable=rent, width=25, bg='#dce8f8', fg='black', font=('Baskerville Old Face', 14, 'bold')).place(x=250, y=150)
    rent.set('')
    l5 = Label(f1, text='Status', font=('Trebuchet MS', 18, 'bold'), fg='black', bg='light blue', pady=1).place(x=50,y=200)
    #e5 = Entry(f1, width=25, bg='#dce8f8', fg='black', font='Papyrus 12 bold').place(x=250, y=200)
    st=('OCCUPIED','FREE')
    housestate = StringVar()
    status = ttk.Combobox(f1, textvariable=housestate, width=46, font=('Gabriola', 10),background='light blue')
    status['values'] = st
    status['state'] = 'readonly'
    status.place(x=250, y=200)
    #b2 = Button(f1, text='houselist', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='SEAGREEN', width=15, bd=3,
                #command=viewhouses).place(x=550, y=50)


    b1 = Button(f1, text='BACK', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='RED', width=15, bd=3,
                command=homewin).place(x=50, y=450)
    b2 = Button(f1, text='ADD', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='SEAGREEN', width=15, bd=3,
                command=addhousetodb).place(x=300, y=450)
    b3 = Button(f1, text='houselist', font=('Trebuchet MS', 14, 'bold'), fg='white', bg='seagreen', width=15, bd=3,
                command=viewhouses).place(x=550, y=450)
    # s = ImageTk.PhotoImage(
    #     Image.open('D:\\DELIVERANCE CHURCH KHAYEGA\\images\\PHONE.png').resize((100, 150)),
    #     master=win)
    # master = Button(f1,text='menu', image=s,compound='left', width=305, height=35, borderwidth=1,bg='green',
    #                 ).place(x=5, y=150)
def homewin():

    Label(w,text='', font=('Trebuchet MS', 19, 'bold'), fg='black', bg='light blue', pady=1, width=70, height=1).place(x=5, y=5)
    Button(w, text='Home', font=('Trebuchet MS', 11, 'bold'), fg='black', bg='light blue', width=10, bd=1, relief=FLAT,
           command=homewin).place(x=10, y=7)
    Button(w, text='Houses', font=('Trebuchet MS', 11, 'bold'), fg='blue', bg='light blue', width=10, bd=1, relief=FLAT,
           command=houserecord).place(x=100, y=7)
    Button(w, text='Tenants', font=('Trebuchet MS', 11, 'bold'), fg='blue', bg='light blue', width=10, bd=1, relief=FLAT,
           command=tenants).place(x=190, y=7)
    #Button(w, text='About', font=('Trebuchet MS', 11, 'bold'), fg='blue', bg='light blue', width=10, bd=1, relief=FLAT,
           #).place(x=280, y=7)
    Button(w, text='power off', font=('Baskerville Old Face', 13,), fg='red', bg='light blue', width=10, bd=1, relief=FLAT,
           command=account).place(x=870, y=7)

    #hf = Frame(w, height=560, width=985, bg='light blue')
    #hf.place(x=5, y=70)


    #Label(hf, text='NIHIJON-SOLO RENTAL HOUSE MANAGEMENT SYSTEM', font=('Trebuchet MS', 22, 'bold'), fg='GREEN', bg='light blue', width=48,
          #height=1).place(x=24, y=200)
    Label(w, text='', font=('Trebuchet MS', 19, 'bold'), fg='black', bg='light blue', pady=1, width=70,
          height=1).place(x=5, y=650)
def database():
    global conn
    link = sqlite3.connect('rental.db')
    conn = link.cursor()
    conn.execute('''create table if not exists users
       (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       USERNAME VARTEXT NOT NULL,
       FIRSTNAME VARTEXT NOT NULL,
       LASTNAME VARTEXT NOT NULL,
       PHONENO VARTEXT NOT NULL,
       PASSWORD VARTEXT NOT NULL
      );''')
    conn.execute('''create table if not exists houses
       (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       HOUSENO VARTEXT NOT NULL,
       SIZE VARTEXT NOT NULL,
       RENT VARTEXT NOT NULL,
       STATUS VARTEXT NOT NULL,
       RENTEDDATE DATE
      );''')
    conn.execute('''create table if not exists tenants
       (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       FIRSTNAME VARTEXT NOT NULL,
       LASTNAME VARTEXT NOT NULL,
       PHONENO VARTEXT NOT NULL,
       HOUSENO VARTEXT NOT NULL,
       RENTEDDATE DATE
      );''')
    link.commit()
    link.close()
def login():
    database()
    link = sqlite3.connect('rental.db')
    conn = link.cursor()
    if lun.get() == "" or lps.get() == "":
        messagebox.showinfo("Error", "Please complete the required field!")
    else:
        conn.execute("SELECT * FROM `users` WHERE `USERNAME` = ? AND `PASSWORD` = ?", (lun.get(), lps.get()))
        if conn.fetchone() is not None:
            messagebox.showinfo('sucess', 'login sucess')
            af.destroy()
            homewin()
        else:
            messagebox.showinfo("Error", "Invalid username or password.")
            lun.set("")
            lps.set("")
def reguser():
    a = username.get()
    b = phone.get()
    ce = email.get()
    d = region.get()
    e = password.get()
    database()
    link = sqlite3.connect('rental.db')
    conn = link.cursor()
    if a == "" or b == "" or ce == "" or d == "" or e == "":
        messagebox.showinfo("Error", "Please complete the required field!")
    else:
        c = conn.execute("SELECT * FROM `users` WHERE `USERNAME` = ? AND `PASSWORD` = ?", (a, e))
        if c.fetchone() is not None:
            messagebox.showinfo("Error", "username taken")
            a.set("")
            b.set("")
            c.set("")
            d.set("")
            e.set("")
        else:
            conn.execute('INSERT INTO users (USERNAME, FIRSTNAME,LASTNAME,PHONENO,PASSWORD)values (?,?,?,?,?)', (str(a), str(b), str(ce), d, e))
            link.commit()
            t.select(T1)
            t.tab(1, state="disabled")

    conn.close()

def account():
    global af
    af = Frame(w, width=1000, bd=1, bg='light blue', height=700)
    af.place(x=0, y=0)
    Label(af, text='NIHIJON-SOLO RENTAL HOUSE MANAGEMENT SYSTEM', font=('Trebuchet MS', 22, 'bold'), fg='GREEN', bg='light blue', width=48,
          height=1).place(x=100, y=20)
    Label(af, text='All rights reserved.', font=('Trebuchet MS', 22, 'bold'), fg='GREEN', bg='light blue', width=48,
          height=1).place(x=100, y=660)
    #ab.destroy()
    global closetab
    #closetab = Button(rf, text='Account', width=8, height=1, relief=FLAT, bg='#149ddd', fg='black',
    #                  font=('Tempus Sans ITC', 11, 'bold'), command=destroytab)
    #closetab.place(x=830, y=13)
    global t, T1, T2
    t = ttk.Notebook(af)
    T1 = ttk.Frame(t)
    T2 = ttk.Frame(t)
    t.configure(width=400, height=400)
    t.add(T1, text="LOGIN")

    t.add(T2, text="REGISTER")

    rbg = Label(T2, text='', bg='light blue', font=('verdana', 16), width=50, height=20)
    rbg.place(x=2, y=0)
    lab = Label(T2, text='Username', fg='black', bg='light blue', font=('Baskerville Old Face', 16), width=10, height=1)
    lab.place(x=2, y=10)
    lab2 = Label(T2, text='First Name', fg='black', bg='light blue', font=('Baskerville Old Face', 16), width=10, height=1)
    lab2.place(x=2, y=70)
    lab2 = Label(T2, text='Last Name', fg='black', bg='light blue', font=('Baskerville Old Face', 16), width=10, height=1)
    lab2.place(x=2, y=130)
    lab2 = Label(T2, text='Phone No', fg='black', bg='light blue', font=('Baskerville Old Face', 16), width=10, height=1)
    lab2.place(x=2, y=190)
    lab2 = Label(T2, text='Password', fg='black', bg='light blue', font=('Baskerville Old Face', 16), width=10, height=1)
    lab2.place(x=2, y=250)
    global username, phone, email, region, password

    username = StringVar()
    phone = StringVar()
    email = StringVar()
    region = StringVar()
    password = StringVar()

    Entry(T2, width=20, textvariable=username, bd=0, bg='WHITE', fg='#149ddd', font=('Baskerville Old Face', 18)).place(x=150, y=10)
    Entry(T2, width=20, textvariable=phone, bd=0, bg='WHITE', fg='#149ddd', font=('Baskerville Old Face', 18)).place(x=150, y=70)
    Entry(T2, width=20, textvariable=email, bd=0, bg='WHITE', fg='#149ddd', font=('Baskerville Old Face', 18)).place(x=150, y=130)
    Entry(T2, width=20, textvariable=region, bd=0, bg='WHITE', fg='#149ddd', font=('Baskerville Old Face', 18)).place(x=150, y=190)
    Entry(T2, width=20, textvariable=password, bd=0, bg='WHITE', fg='#149ddd', font=('Baskerville Old Face', 18),show='*').place(x=150, y=250)

    Button(T2, text='Register', width=15, height=1, relief=FLAT, bg='#dce8f8', fg='black',
           font=('Baskerville Old Face', 16, 'bold'), command=reguser).place(x=150, y=320)

    lbg = Label(T1, text='', bg='light blue', font=('Baskerville Old Face', 16), width=50, height=20)
    lbg.place(x=2, y=0)
    laba = Label(T1, text='Username', fg='purple', bg='light blue', font=('Baskerville Old Face', 16), width=10, height=1)
    laba.place(x=2, y=10)
    labb = Label(T1, text='Password', fg='purple', bg='light blue', font=('Baskerville Old Face', 16), width=10, height=1)
    labb.place(x=2, y=100)
    global lun, lps
    lun = StringVar()
    lps = StringVar()

    Entry(T1, textvariable=lun, width=23, bd=0, bg='WHITE', fg='#149ddd', font=('Baskerville Old Face', 16)).place(x=150, y=10)
    Entry(T1, textvariable=lps, width=23, bd=0, bg='WHITE', fg='#149ddd', font=('Baskerville Old Face', 16),show='*').place(x=150, y=100)

    Button(T1, text='Login', width=17, height=1, relief=FLAT, bg='seagreen', fg='white',
           font=('Baskerville Old Face', 16, 'bold'), command=login).place(x=150, y=200)
    t.place(x=300, y=100)
global w
w=Tk()
w.title('TK')
w.minsize(1000,700)
from PIL import ImageTk, Image

b = Image.open('images/b3.jpg').resize((985, 700))
mbg = ImageTk.PhotoImage(b, master=w)
Label(w, image=mbg, width=995, height=580).place(
    x=0, y=50)
#w.iconbitmap('H2.ico')
database()
account
w.mainloop()