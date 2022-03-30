from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox
from datetime import *
import adminmain, empmain
import cx_Oracle
global c
con = cx_Oracle.connect('databaseproject/databaseproject@//localhost:1521/pdborcll')
c = con.cursor()


class GUI:
    global u
    def login_button(self):
        global u
        c.execute("SELECT * FROM USERS")
        records = c.fetchall()
        #print(records)

        u = int(username.get())
        p = password.get()

        count = 1
        for record in records:
            if u == record[2] and p == record[1] and record[2] != 1000:
                top.destroy()
                empmain.y.get_empid(u)
                empmain.y.mainpagegui()
            elif u == record[2] and p == record[1] and record[2] == 1000:
                top.destroy()
                adminmain.y.mainpagegui()
            elif u == record[2] and p != record[1]:
                messagebox.showerror("error", "Invalid Password")
                break
            elif u != record[2] and count == len(records):
                messagebox.showerror("error", "User doesnot exist")
            count += 1

    def register_button(self):
        r_u = r_username.get()
        r_p = r_password.get()
        user_id = int(userid.get())

        c.execute("SELECT * FROM USERS")
        user_record =  c.fetchall()
        c.execute("SELECT * FROM Employee")
        emp_record = c.fetchall()
        emp_ids = []
        user_ids= []
        for record in emp_record:
            emp_ids.append(record[0])
        for record in user_record:
            user_ids.append(record[2])
        print(user_ids)
        print(emp_ids)

        if user_id not in emp_ids:
            messagebox.showerror("error", "Employee doesn't exist")
        else:
            if user_id in user_ids:
                messagebox.showerror("error", "User already register!")
            else:
                c.execute("""INSERT INTO USERS VALUES(:x, :y, :z)""", x = r_u, y = r_p, z = user_id)
                c.execute("""commit""")
                messagebox.showinfo("showinfo", "User register sucessfully!")
                top_reg.destroy()
                x.mainpagegui()



    def register(self):
        global r_username, r_password, userid, top_reg
        top.destroy()
        top_reg = Tk()
        topimg1 = PhotoImage(file='images/logon.png')
        top_reg.iconphoto(False, topimg1)
        top_reg.geometry("650x620+350+30")
        top_reg.minsize(148, 1)
        top_reg.maxsize(1924, 1055)
        top_reg.resizable(0, 0)
        top_reg.title("Event Management System")
        top_reg.configure(background="#d9d9d9")
        top_reg.configure(highlightbackground="#d9d9d9")
        top_reg.configure(highlightcolor="black")

        mainframe1 = tk.Frame(top_reg)
        mainframe1.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.003)

        mainframe1.configure(relief='solid')
        mainframe1.configure(borderwidth="0")
        mainframe1.configure(relief="solid")
        mainframe1.configure(background="#d9d9d9")
        icon3 = tkinter.PhotoImage(file="images\mainbackground_register.png")
        mainpic1 = Label(mainframe1, image=icon3)
        mainpic1.pack()

        r_username = tk.Entry(top_reg)
        r_username.place(relx=0.35, rely=0.46, height=35, relwidth=0.450)
        r_username.configure(background="white")
        r_username.configure(disabledforeground="#a3a3a3")
        r_username.configure(font="-family {Prototype} -size 14")
        r_username.configure(foreground="#000000")
        r_username.configure(insertbackground="black")
        #
        r_password = tk.Entry(top_reg)
        r_password.place(relx=0.35, rely=0.57, height=35, relwidth=0.450)
        r_password.configure(background="white")
        r_password.configure(disabledforeground="#a3a3a3")
        r_password.configure(font="-family {Prototype} -size 14")
        r_password.configure(foreground="#000000")
        r_password.configure(highlightbackground="#d9d9d9")
        r_password.configure(highlightcolor="black")
        r_password.configure(insertbackground="black")
        r_password.configure(selectbackground="#c4c4c4")
        r_password.configure(selectforeground="black")
        r_password.configure(show='*')

        userid = tk.Entry(top_reg)
        userid.place(relx=0.35, rely=0.68, height=35, relwidth=0.450)
        userid.configure(background="white")
        userid.configure(disabledforeground="#a3a3a3")
        userid.configure(font="-family {Prototype} -size 14")
        userid.configure(foreground="#000000")
        userid.configure(insertbackground="black")

        #
        Button1 = tk.Button(top_reg, command=x.register_button)
        Button1.place(relx=0.35, rely=0.79, height=55, relwidth=0.450)
        Button1.configure(activebackground="#3a7ebf")
        Button1.configure(activeforeground="white")
        Button1.configure(background="#044c92")
        Button1.configure(cursor="hand2")
        Button1.configure(disabledforeground="#4b9cd3")
        Button1.configure(font="-family {Prototype} -size 13")
        Button1.configure(foreground="#ffffff")
        Button1.configure(highlightbackground="#4b9cd3")
        Button1.configure(highlightcolor="black")
        Button1.configure(pady="0")
        Button1.configure(text='''Register Now''')
        Button1.configure(relief='flat')
        top_reg.mainloop()



    def mainpagegui(self):
        global top, username, password
        top = Tk()
        topimg = PhotoImage(file = 'images/logon.png')
        top.iconphoto(False, topimg)
        top.geometry("650x620+350+30")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(0, 0)
        top.title("Event Management System")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        mainframe = tk.Frame(top)
        mainframe.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.003)

        mainframe.configure(relief='solid')
        mainframe.configure(borderwidth="2")
        mainframe.configure(relief="solid")
        mainframe.configure(background="#d9d9d9")
        icon2 = PhotoImage(file="images\mainbackground.png")
        mainpic = Label(mainframe, image=icon2)
        mainpic.pack()


        username = tk.Entry(top)
        username.place(relx=0.27, rely=0.45, height=40, relwidth=0.500)
        username.configure(background="white")
        username.configure(disabledforeground="#a3a3a3")
        username.configure(font="-family {Prototype} -size 14")
        username.configure(foreground="#000000")
        username.configure(insertbackground="black")
        #
        password = tk.Entry(top)
        password.place(relx=0.27, rely=0.6, height=40, relwidth=0.500)
        password.configure(background="white")
        password.configure(disabledforeground="#a3a3a3")
        password.configure(font="-family {Prototype} -size 14")
        password.configure(foreground="#000000")
        password.configure(highlightbackground="#d9d9d9")
        password.configure(highlightcolor="black")
        password.configure(insertbackground="black")
        password.configure(selectbackground="#c4c4c4")
        password.configure(selectforeground="black")
        password.configure(show = '*')
        #
        Button1 = tk.Button(top,command=x.login_button)
        Button1.place(relx=0.27, rely=0.747, height=55, relwidth=0.22)
        Button1.configure(activebackground="#3a7ebf")
        Button1.configure(activeforeground="white")
        Button1.configure(background="#044c92")
        Button1.configure(cursor="hand2")
        Button1.configure(disabledforeground="#4b9cd3")
        Button1.configure(font="-family {Prototype} -size 13")
        Button1.configure(foreground="#ffffff")
        Button1.configure(highlightbackground="#4b9cd3")
        Button1.configure(highlightcolor="black")
        Button1.configure(pady="0")
        Button1.configure(text='''Login''')
        Button1.configure(relief='flat')

        Button2 = tk.Button(top, command=x.register)
        Button2.place(relx=0.55, rely=0.747, height=55, relwidth=0.22)
        Button2.configure(activebackground="#3a7ebf")
        Button2.configure(activeforeground="white")
        Button2.configure(background="#044c92")
        Button2.configure(cursor="hand2")
        Button2.configure(disabledforeground="#4b9cd3")
        Button2.configure(font="-family {Prototype} -size 13")
        Button2.configure(foreground="#ffffff")
        Button2.configure(highlightbackground="#4b9cd3")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text='''Register''')
        Button2.configure(relief='flat')

        top.mainloop()


x = GUI()
x.mainpagegui()