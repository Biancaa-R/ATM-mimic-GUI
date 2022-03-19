#python code for making an e-ATM app
#import mysql connector
import db,dbdetails
dbuser, dbpass = dbdetails.execute()
db.exec(dbuser,dbpass)
import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password="biancaa",
    database="atm"
    )
sql=conn.cursor()
#import tkinter
import tkinter as ATM
from tkinter import *
from tkinter import messagebox
#functions for closing
def destroy(event):
    first.destroy()
def destroy1():
    l_win.destroy()
#to deposit money
def deposit():
    global Deposit, deposit_entry, Acc_num
    Deposit=deposit_entry.get()
    sql.execute("""UPDATE EATM SET BALANCE=BALANCE+'{}' WHERE acc_num='{}'""".format(Deposit,Acc_num))
    messagebox.showinfo("Success",Deposit+" Ammount deposited successfully")
    conn.commit()
    deposit_entry.delete(0,10)
#to withdraw money
def withdraw():
    global Withdraw, withdraw_entry, Acc_num
    sql.execute("""SELECT balance FROM EATM WHERE acc_num = '{}'""".format(Acc_num))
    f=sql.fetchone()[0]
    f=int(f)
    Withdraw=withdraw_entry.get()
    if f > 0:

        if (f < int(Withdraw)):
            messagebox.showerror("Error","Not enough balance")
        else:
            sql.execute("""UPDATE EATM SET BALANCE=BALANCE-'{}' WHERE acc_num='{}'""".format(Withdraw,Acc_num))
            conn.commit()
            messagebox.showinfo("Success",Withdraw +"Money withdrawn successfully")
    elif f <= 0:
        messagebox.showerror("No Balance","No more Balance in your account.Please deposit money to withdraw more")
    withdraw_entry.delete(0,10)
    
        
#to see the details of the user
def check():
    global Acc_num, l_win
    sql.execute("""SELECT * FROM EATM WHERE acc_num = '{}'""".format(Acc_num))
    r = sql.fetchall()[0]
    name = r[0]
    balance = r[-1]
    messagebox.showinfo("Your account details","Name: "+name+"\n"+"Balance : "+str(balance))
    
    #conn.commit()
#to get values from the user
def submit():
    global Name, Dob, Accno, Accpin, Contact, Email
    Name = name.get()
    Dob=dob.get()
    Accno=acc_num.get()
    Accpin=acc_pin.get()
    Contact=contact_num.get()
    Email=email_id.get()
    if len(Name)==0 or len(Dob)==0 or len(Accno)==0 or len(Accpin)==0 or len(Contact)==0 or len(Email)==0:
        messagebox.showerror("Error","Please fill in all fields")
#to insert the given data to the table in mysql
    sql.execute("""INSERT IGNORE INTO EATM values('{}', '{}', '{}', '{}', '{}', '{}',0)""".format(Name,Dob,Accno,Accpin,Contact,Email))
    conn.commit()
    if True:
        messagebox.showinfo("Successful","Account created successfully")
    
#to remove the data in the entry boxes
    name.delete(0,20)
    dob.delete(0,10)
    acc_num.delete(0,4)
    acc_pin.delete(0,3)
    contact_num.delete(0,10)
    email_id.delete(0,50)
    conn.commit()
#login-verification of the user
def login():
    global Acc_num, Acc_pin, a1, a2, l_win
    Acc_num = a1.get()
    Acc_pin = a2.get()
    #Acc_pin=a2.config(show="*")
    #Acc_pin=Entry(parent,show="*",width=15)
    #Acc_pin=Entry(a2,show="*")
    a1.delete(0,4)
    a2.delete(0,3)
    result=sql.execute("""SELECT * FROM EATM WHERE acc_num = '{}' and acc_pin = '{}'""".format(Acc_num, Acc_pin))
#creating a window to do changes to withdraw, deposit money, and see details.
    if result==True:
        messagebox.showinfo("Successful","Successfully logged in")
        l_win=ATM.Toplevel()
        global Deposit, deposit_entry
        deposit_lab=ATM.Label(l_win,
            text="Deposit Money",
            fg="black",
            bg="green",
            width=70,
            height=2)
        deposit_lab.pack()

        deposit_entry=ATM.Entry(l_win,
                                width=50)
        deposit_entry.pack()

        deposit_btn=ATM.Button(l_win,
                               text="DEPOSIT MONEY",
                               fg="white",
                               bg="red",
                               width=30,
                               height=3,
                               command=deposit)
        deposit_btn.bind("<Button-1>")
        deposit_btn.pack()

        space1=ATM.Label(l_win,
            text="space",
            bg="white",
            fg="white",
            width=70,
            height=2)
        space1.pack()
        global Withdraw, withdraw_entry
        withdraw_lab=ATM.Label(l_win,
            text="Withdraw Money",
            fg="black",
            bg="green",
            width=70,
            height=2)
        withdraw_lab.pack()

        withdraw_entry=ATM.Entry(l_win,
                                 width=50)
        withdraw_entry.pack()

        withdraw_btn=ATM.Button(l_win,
                           text="WITHDRAW MONEY",
                           fg="white",
                           bg="red",
                           width=30,
                           height=3,
                           command=withdraw)
        withdraw_btn.bind("<Button-1>")
        withdraw_btn.pack()

        space2=ATM.Label(l_win,
        text="space",
        fg="white",
        bg="white",
        width=70,
        height=2)
        space2.pack()
#Button to see balance
        see_btn=ATM.Button(l_win,
                           text="BALANCE ENQUIRY",
                           fg="white",
                           bg="red",
                           width=30,
                           height=3,
                           command=check)
        see_btn.bind("<Button-1>")
        see_btn.pack()
#Button to close window
        logout=ATM.Button(l_win,
                          text="LOGOUT",
                          fg="white",
                          bg="red",
                          width=30,
                          height=3,
                          command=destroy1)
        logout.bind("<Button-1>")
        logout.pack()
        l_win.mainloop()
        conn.commit()
#appropriate message for wrong details
    else:
        messagebox.showerror("Error!!","Invalid account number and pin, Please check again!!")
    #conn.commit()
#third window function
def login_win(event):
    second = ATM.Toplevel()
    second.title("Login screen ATM")
#title for third window
    title=ATM.Label(second,
        text="Login",
        fg="black",
        bg="white",
        width=70,
        height=5)
    title.pack()
    global Acc_num, Acc_pin, a1, a2
#account number enter for login
    e1=ATM.Label(second,
        text="Account Number",
        fg="white",
        bg="green",
        width=20,
        height=2)
    a1=ATM.Entry(second,show="*",
                 width=35)
    e1.pack()
    a1.pack()
#pin number enter for login
    e2=ATM.Label(second,
        text="Pin Number",
        fg="white",
        bg="green",
        width=20,
        height=2)
    a2=ATM.Entry(second,show="*",
                 width=35)
    e2.pack()
    a2.pack()
#Button to continue
    l_btn=ATM.Button(second,
        text="Login",
        fg="white",
        bg="red",
        width=20,
        height=2,
        command=login)
    l_btn.bind("<Button-1>")
    l_btn.pack()
    second.mainloop()
#first window
first = ATM.Tk()
first.title("ATM machine")
#for full screen
#first.attributes('-fullscreen', True)
#open page title
title=ATM.Label(
    text="E-AUTOMATED TELLER MACHINE",
    fg="black",
    bg="white",
    width=70,
    height=5)
title.pack()
#creating account button
create=ATM.Label(
    text="Create new account",
    fg="white",
    bg="blue",
    width=70,
    height=3)
create.pack()
#precaution note
caution=ATM.Label(
    text="PLEASE FILL EVERYTHING OR YOUR ACCOUNT WON'T BE CREATED!!",
    fg="red",
    bg="white",
    width=70,
    height=3)
caution.pack()
#name of the user
e1=ATM.Label(
    text="Name",
    fg="white",
    bg="green",
    width=20,
    height=2)
name=ATM.Entry(width=35)
e1.pack()
name.pack()
#DOB of the user
e2=ATM.Label(
    text="Date of Birth",
    fg="white",
    bg="green",
    width=20,
    height=2)
dob=ATM.Entry(width=35)
e2.pack()
dob.pack()
#Account number of the user
e3=ATM.Label(
    text="Account Number(4-digits)",
    fg="white",
    bg="green",
    width=20,
    height=2)
acc_num=ATM.Entry(width=35)
e3.pack()
acc_num.pack()
#Password of the user
e4=ATM.Label(
    text="Pin Number(3-digits)",
    fg="white",
    bg="green",
    width=20,
    height=2)
acc_pin=ATM.Entry(width=35)
e4.pack()
acc_pin.pack()
#Phone number of the user
e5=ATM.Label(
    text="Contact Number",
    fg="white",
    bg="green",
    width=20,
    height=2)
contact_num=ATM.Entry(width=35)
e5.pack()
contact_num.pack()
#Email id of the user
e6=ATM.Label(
    text="Email Address",
    fg="white",
    bg="green",
    width=20,
    height=2)
email_id=ATM.Entry(width=35)
e6.pack()
email_id.pack()
#Button to get all values
get=ATM.Button(command=submit,
    text="Create Account",
    fg="white",
    bg="red",
    width=50,
    height=3)
global Name,Dob, Accno, Accpin, Contact, Email

get.bind("<Button-1>")
get.pack()
#login button
Login=ATM.Button(
    text="Already Created Account? Login!",
    fg="white",
    bg="red",
    width=30,
    height=3)
Login.bind("<Button-1>",login_win)
Login.pack()
#close button
close=ATM.Button(
    text="Exit",
    fg="white",
    bg="red",
    width=30,
    height=3)
close.bind("<Button-1>",destroy)
close.pack()
first.mainloop()
conn.commit()
sql.close()
conn.close()
