from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox
from datetime import *
import cx_Oracle
from tkcalendar import *


global c
con = cx_Oracle.connect('databaseproject/databaseproject@//localhost:1521/pdborcll')
c = con.cursor()



class GUI:
    def get_empid(self, id):
        global empidget
        empidget = id

    def parent_frame(self):
        global parent_frame
        parent_frame = tk.Frame(top)
        parent_frame.place(relx=0.0, rely=0.17, relheight=0.85, relwidth=1)
        parent_frame.configure(relief='flat')
        parent_frame.configure(background="white")

    def clear_frame(self):
        for widgets in parent_frame.winfo_children():
            widgets.destroy()

    def checkentryfood(self,e):
        typed = sf_entry.get()
        selected = sf_var.get()
        if typed == '':
            data = f_records
        else:
            data = []
            for record in f_records:
                if selected == 0:
                    if typed in str(record[selected]):
                        data.append(record)
                else:
                    if typed.lower() in record[selected].lower():
                        data.append(record)
        for record in myf_tree.get_children():
            myf_tree.delete(record)
        count=0
        for record in data:
            if count % 2 == 0:
                myf_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3]),tags=('evenrow',))
            else:
                myf_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2]),
                               tags=('oddrow',))
            count +=1

    def checkentryvendor(self,e):
        typed = svendor_entry.get()
        selected = svendor_var.get()
        if typed == '':
            data = vendor_records
        else:
            data = []
            for record in vendor_records:
                if selected == 0:
                    if typed in str(record[selected]):
                        data.append(record)
                else:
                    if typed.lower() in record[selected].lower():
                        data.append(record)
        for record in myvendor_tree.get_children():
            myvendor_tree.delete(record)
        count=0
        for record in data:
            if count % 2 == 0:
                myvendor_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],"0"+str(record[2]),record[3]),tags=('evenrow',))
            else:
                myvendor_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], "0"+str(record[2]), record[3]),
                               tags=('oddrow',))
            count +=1

    def checkentrydec(self,e):
        typed = sdec_entry.get()
        selected = sdec_var.get()
        if typed == '':
            data = dec_records
        else:
            data = []
            for record in dec_records:
                if selected == 0:
                    if typed in str(record[selected]):
                        data.append(record)
                else:
                    if typed.lower() in record[selected].lower():
                        data.append(record)
        for record in mydec_tree.get_children():
            mydec_tree.delete(record)
        count=0
        for record in data:
            if count % 2 == 0:
                mydec_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2]),tags=('evenrow',))
            else:
                mydec_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2]),
                               tags=('oddrow',))
            count +=1

    def checkentryser(self,e):
        typed = sser_entry.get()
        selected = sser_var.get()
        if typed == '':
            data = ser_records
        else:
            data = []
            for record in ser_records:
                if selected == 0:
                    if typed in str(record[selected]):
                        data.append(record)
                else:
                    if typed.lower() in record[selected].lower():
                        data.append(record)
        for record in myser_tree.get_children():
            myser_tree.delete(record)
        count=0
        for record in data:
            if count % 2 == 0:
                myser_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2]),tags=('evenrow',))
            else:
                myser_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2]),
                               tags=('oddrow',))
            count +=1

    def checkentryvenue(self, e):
        typed = sv_entry.get()
        selected = sv_var.get()
        if typed == '':
            data = v_records
        else:
            data = []
            for record in v_records:
                if selected == 0:
                    if typed in str(record[selected]):
                        data.append(record)
                else:
                    if typed.lower() in record[selected].lower():
                        data.append(record)
        for record in myv_tree.get_children():
            myv_tree.delete(record)
        count = 0
        for record in data:
            if count % 2 == 0:
                myv_tree.insert(parent='', index='end', iid=count, text='',
                                values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                tags=('evenrow',))
            else:
                myv_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], record[2], record[3], record[4], record[5]),
                                tags=('oddrow',))
            count += 1

    def viewallvenue(self):
        global v_count, v_records
        c.execute("SELECT * FROM VENUE ORDER BY VENUEID ")
        v_records = c.fetchall()
        for record in myv_tree.get_children():
            myv_tree.delete(record)
        v_count = 0
        for record in v_records:
            if v_count % 2 == 0:
                myv_tree.insert(parent='', index='end', iid=v_count, text='', values=(
                    record[0], record[1], record[2], record[3],"0"+str(record[4]), record[5]),
                                tags=('evenrow',))
            else:
                myv_tree.insert(parent='', index='end', iid=v_count, text='', values=(
                    record[0], record[1], record[2], record[3], "0"+str(record[4]), record[5]),
                                tags=('oddrow',))
            v_count += 1


    def viewallfood(self):
        global f_count,f_records
        c.execute("SELECT * FROM FOOD ORDER BY ITEMID ")
        f_records = c.fetchall()
        for record in myf_tree.get_children():
            myf_tree.delete(record)
        f_count = 0
        for record in f_records:
            if f_count % 2 == 0:
                myf_tree.insert(parent='', index='end', iid=f_count, text='', values=(
                    record[0], record[1], record[2], record[3]),
                               tags=('evenrow',))
            else:
                myf_tree.insert(parent='', index='end', iid=f_count, text='', values=(
                    record[0], record[1], record[2],record[3]),
                               tags=('oddrow',))
            f_count += 1

    def viewallvendor(self):
        global vendor_count,vendor_records
        c.execute("SELECT * FROM VENDOR ORDER BY VENDORID ")
        vendor_records = c.fetchall()
        for record in myvendor_tree.get_children():
            myvendor_tree.delete(record)
        vendor_count = 0
        for record in vendor_records:
            if vendor_count % 2 == 0:
                myvendor_tree.insert(parent='', index='end', iid=vendor_count, text='', values=(
                    record[0], record[1], "0"+str(record[2]), record[3]),
                               tags=('evenrow',))
            else:
                myvendor_tree.insert(parent='', index='end', iid=vendor_count, text='', values=(
                    record[0], record[1], "0"+str(record[2]),record[3]),
                               tags=('oddrow',))
            vendor_count += 1

    def viewalldec(self):
        global dec_count,dec_records
        c.execute("SELECT * FROM DECORATION ORDER BY DECORATIONID ")
        dec_records = c.fetchall()
        for record in mydec_tree.get_children():
            mydec_tree.delete(record)
        dec_count = 0
        for record in dec_records:
            if dec_count % 2 == 0:
                mydec_tree.insert(parent='', index='end', iid=dec_count, text='', values=(
                    record[0], record[1], record[2]),
                               tags=('evenrow',))
            else:
                mydec_tree.insert(parent='', index='end', iid=dec_count, text='', values=(
                    record[0], record[1],record[2]),
                               tags=('oddrow',))
            dec_count += 1

    def viewallser(self):
        global ser_count,ser_records
        c.execute("SELECT * FROM SERVICE ORDER BY SERVICEID ")
        ser_records = c.fetchall()
        for record in myser_tree.get_children():
            myser_tree.delete(record)
        ser_count = 0
        for record in ser_records:
            if ser_count % 2 == 0:
                myser_tree.insert(parent='', index='end', iid=ser_count, text='', values=(
                    record[0], record[1], record[2]),
                               tags=('evenrow',))
            else:
                myser_tree.insert(parent='', index='end', iid=ser_count, text='', values=(
                    record[0], record[1],record[2]),
                               tags=('oddrow',))
            ser_count += 1

    def update_profile(self):
        email = eemail_entry.get()
        contact = econtact_entry.get()
        address = eaddress_entry.get()

        if len(email) > 30 or len(email) == 0 or "@" not in email:
            messagebox.showerror("error","Invalid Email!")
        elif len(contact) > 11 or len(contact) < 11 or len(contact) == 0 or contact.isdecimal() == False or "03" != contact[0:2]:
            messagebox.showerror("error","Invalid Number!")
        elif len(address) > 50 or len(address) == 0:
            messagebox.showerror("error", "Invalid Address Address !")
        else:
            c.execute("""UPDATE EMPLOYEE SET EMPLOYEEEMAIL = :a, EMPLOYEECONTACT = :b, EMPLOYEEADDRESS = :c WHERE EMPLOYEEID = :x""", a = email, b = contact, c = address, x = empidget)
            c.execute("""COMMIT""")

    def change_pass(self):
        curr_pass = curr_pass_entry.get()
        new_pass = new_pass_entry.get()
        conf_pass = conf_pass_entry.get()


        c.execute("""SELECT PASSWORD FROM USERS WHERE USERID = :x""", x = empidget)
        current_pass = c.fetchall()
        print(current_pass)

        if current_pass[0][0] == curr_pass:
            if new_pass == conf_pass:
                c.execute("""UPDATE USERS SET PASSWORD = :x WHERE USERID = :y""", x = new_pass, y = empidget)
                c.execute("""COMMIT""")
                messagebox.showinfo("info", "password changed sucessfully")
                curr_pass_entry.delete(0,END)
                new_pass_entry.delete(0, END)
                conf_pass_entry.delete(0, END)
            else:
                messagebox.showerror("error", "password not match")
        else:
            messagebox.showerror("error", "invalid current password")





    def search(self):
        for record in my_tree.get_children():
            my_tree.delete(record)
        #query
        c.execute("""select ed.venueid from eventdetail ed inner join event e on (ed.eventid = e.eventid) where eventdate = TO_DATE(:x, 'YYYY-MM-DD')""", x = cal.get())
        bookvenueid = c.fetchall()
        bookv = set()
        for v in bookvenueid:
            bookv.add(v[0])
        c.execute("""SELECT VENUEID FROM VENUE""")
        all_venueid = c.fetchall()
        allv_id = set()
        for v in all_venueid:
            allv_id.add(v[0])
        s_records = []
        available_venue = allv_id.difference(bookv)
        for a in available_venue:
            c.execute("""SELECT * FROM VENUE WHERE VENUEID = :x""",x =a)
            data = c.fetchall()
            s_records.append(data[0])

        s_count = 0
        for record in s_records:
            if s_count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=s_count, text='', values=(
                    record[0], record[1], record[2], record[3], "0"+str(record[4]), record[5]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=s_count, text='', values=(
                    record[0], record[1], record[2], record[3], "0"+str(record[4]), record[5]),
                               tags=('oddrow',))
            s_count += 1



    def home(self):
        y.clear_frame()
        parent_frame.configure(background="white")

        # DATABASE
        c.execute("""SELECT COUNT(EVENTID) FROM Event""")
        totalevent = c.fetchall()
        #
        c.execute("""SELECT COUNT(EVENTID) FROM EVENT WHERE EMPLOYEEID = :x""", x= empidget)
        mytotalevent = c.fetchall()
        #
        c.execute("""SELECT COUNT(EVENTID) FROM EVENT WHERE EMPLOYEEID = :x AND EVENTDATE = SYSDATE""", x = empidget)
        mytodayevent = c.fetchall()
        #
        c.execute("""SELECT COUNT(EVENTID) FROM EVENT WHERE EMPLOYEEID = :x AND EVENTDATE > SYSDATE""", x = empidget)
        myupcommingevent = c.fetchall()

        frame1 = Frame(parent_frame, background = "#3a7ebf", width = '130px', height = '130px',
                       cursor="hand2",relief='sunken')
        frame1.place(relx =0.125, rely = 0.10)

        label1 = Label(frame1, text = "Total Events", justify = "center", bg = "#3a7ebf", fg = "white",
                       font="-family {Prototype} -size 15")
        label1.place(relx =0.16, rely =0.16)
        if (totalevent[0][0]) < 9:
           totalevent = '0'+str(totalevent[0][0])
        label2 = Label(frame1, text=totalevent, justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 40")
        label2.place(relx=0.34, rely=0.38)

        frame2 = Frame(parent_frame, background="#3a7ebf", width='130px', height='130px',
                       cursor="hand2",relief='sunken')
        frame2.place(relx=0.325, rely=0.10)
        label1 = Label(frame2, text="My", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 14")
        label1.place(relx=0.42, rely=0.06)
        label1 = Label(frame2, text="Total Events", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 15")
        label1.place(relx=0.18, rely=0.22)
        if (mytotalevent[0][0]) < 9:
           mytotalevent = '0'+str(mytotalevent[0][0])
        label2 = Label(frame2, text=mytotalevent, justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 40")
        label2.place(relx=0.30, rely=0.38)

        frame3 = Frame(parent_frame, background="#3a7ebf", width='130px', height='130px',
                       cursor="hand2",relief='sunken')
        frame3.place(relx=0.525, rely=0.10)
        label1 = Label(frame3, text="My", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 14")
        label1.place(relx=0.38, rely=0.06)
        label2 = Label(frame3, text="Today's Events", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 14")
        label2.place(relx=0.10, rely=0.22)
        if (mytodayevent[0][0]) < 9:
            mytodayevent = '0'+str(mytodayevent[0][0])
        label3 = Label(frame3, text=mytodayevent, justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 40")
        label3.place(relx=0.30, rely=0.38)

        frame4 = Frame(parent_frame, background="#3a7ebf", width='130px', height='130px',
                       cursor="hand2",relief='sunken')
        frame4.place(relx=0.725, rely=0.10)
        label1 = Label(frame4, text="My", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 14")
        label1.place(relx=0.38, rely=0.06)
        label2 = Label(frame4, text="Upcomming Events", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 14")
        label2.place(relx=0.02, rely=0.22)
        if (myupcommingevent[0][0]) < 9:
            myupcommingevent = '0'+str(myupcommingevent[0][0])
        label3 = Label(frame4, text=myupcommingevent, justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 40")
        label3.place(relx=0.30, rely=0.38)

        # tree View Start
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')

        # configure the tree view colors
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")

        style.configure("Treeview.Heading", background = "#044c92", foreground = "white", font="-family {Prototype} -size 12")
        # change selected color
        style.map('Treeview',
                  background=[('selected', '#044c92')])

        # crate treview frame
        tree_frame = Frame(parent_frame)
        tree_frame.place(relx=0.085, rely=0.42)

        # treescrolly
        tree_scrolly = Scrollbar(tree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(tree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                               selectmode="extended")
        my_tree.pack()

        # configure scroll bar
        tree_scrolly.config(command=my_tree.yview)
        tree_scrollx.config(command=my_tree.xview)

        # define coloums
        my_tree['columns'] = (
        "EVENTID", "EVENTTYPEID", "EVENTDATE", "NOOFGUEST", "EVENTADVANCEPAYMENT", "CUSTOMERID", "EMPLOYEEID",
        "DECORATIONID")

        # format our coloums
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("EVENTID", anchor=CENTER, width=140)
        my_tree.column("EVENTTYPEID", anchor=CENTER, width=140)
        my_tree.column("EVENTDATE", anchor=CENTER, width=140)
        my_tree.column("NOOFGUEST", anchor=CENTER, width=140)
        my_tree.column("EVENTADVANCEPAYMENT", anchor=CENTER, width=140)
        my_tree.column("CUSTOMERID", anchor=CENTER, width=140)
        my_tree.column("EMPLOYEEID", anchor=CENTER, width=140)
        my_tree.column("DECORATIONID", anchor=CENTER, width=140)

        # define heading
        my_tree.heading("#0", text="", anchor=CENTER)
        my_tree.heading("EVENTID", text="Event ID", anchor=CENTER)
        my_tree.heading("EVENTTYPEID", text="Event Type ID", anchor=CENTER)
        my_tree.heading("EVENTDATE", text="Event Date", anchor=CENTER)
        my_tree.heading("NOOFGUEST", text="No of Guest", anchor=CENTER)
        my_tree.heading("EVENTADVANCEPAYMENT", text="Advance Payment", anchor=CENTER)
        my_tree.heading("CUSTOMERID", text="Customer ID", anchor=CENTER)
        my_tree.heading("EMPLOYEEID", text="Employee ID", anchor=CENTER)
        my_tree.heading("DECORATIONID", text="Decoration ID", anchor=CENTER)

        # data

        c.execute("SELECT * FROM Event WHERE EMPLOYEEID = :x ORDER BY EVENTDATE DESC", x = empidget)
        records = c.fetchall()

        # create stripped row tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#87cdee")

        # adding data
        global count
        count = 0
        for record in records:
            date = record[2]
            date = datetime.date(date)
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], date, record[3], record[4], record[5], record[6], record[7]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], date, record[3], record[4], record[5], record[6], record[7]),
                               tags=('oddrow',))
            count += 1



    def bookevent(self):
        global eventnextid,cal, search_entry2
        y.clear_frame()
        parent_frame.configure(background="white")

        #Search Frame
        Searchframe = LabelFrame(parent_frame, background="white", width='920px', height='50px', text = 'Search Event',
                       cursor="hand2", relief='groove', bd = 2, font= "-family {Prototype} -size 15", fg ="#044c92",
                                 labelanchor = NW)
        Searchframe.place(relx=0.045, rely=0.07)

        empty_label6 = Label(Searchframe, font="-family {Prototype} -size 12", bg='white')
        empty_label6.grid(row=0, column=0, padx=10, pady=10)

        search_label1 = Label(Searchframe, text="Event ID", justify="center", bg="white", fg="black",
                       font="-family {Prototype} -size 12")
        search_label1.grid(row = 0, column = 1, padx = 10, pady = 10)
        search_entry1 = Entry(Searchframe, relief = 'solid', bd = 1, font="-family {Prototype} -size 12")
        c.execute("""Select max (EVENTID) from EVENT""")
        eventnextid = c.fetchall()
        eventnextid = eventnextid[0][0] + 1
        search_entry1.insert(0, eventnextid)
        search_entry1.config(state='readonly')

        search_entry1.insert(0,1)
        search_entry1.config(state = 'readonly')
        search_entry1.grid(row = 0, column = 2, padx = 10, pady = 10)

        empty_label1 = Label(Searchframe, font="-family {Prototype} -size 12", bg='white')
        empty_label1.grid(row=0, column=3, padx=10, pady=10)

        search_label2 = Label(Searchframe, text="Event Date", justify="center", bg="white", fg="black",
                              font="-family {Prototype} -size 12")
        search_label2.grid(row=0, column=4, padx=10, pady=10)

        cal = DateEntry(Searchframe, width=19,
        background='#044c92', foreground='white', borderwidth=1, font="-family {Prototype} -size 12", headersbackground = "#3a7ebf",
                        headersforeground = "white", selectbackground = "#044c92", selectforeground = "white",normalbackground = "white",
                        normalforeground = "black", weekendbackground = "white", weekendforeground = "black",
                        othermonthforeground = "black", othermonthbackground = "white", othermonthweforeground = "black",
                        othermonthwebackground= "white", date_pattern = "YYYY-MM-DD")
        # 3a7ebf
        cal.grid(row = 0, column=5, padx = 10, pady = 10)

        empty_label2 = Label(Searchframe, font="-family {Prototype} -size 12", bg='white')
        empty_label2.grid(row=0, column=6, padx=10, pady=10)

        search_label2 = Label(Searchframe, text="Event type", justify="center", bg="white", fg="black",
                              font="-family {Prototype} -size 12")
        search_label2.grid(row=0, column=7, padx=10, pady=10)


        c.execute("""SELECT EVENTTYPENAME FROM EVENTTYPE""")
        row = c.fetchall()
        event_list = []
        for i in row:
            event_list.append(i[0])
        global e_type
        e_type = StringVar()
        search_entry2 = ttk.Combobox(Searchframe, textvariable=e_type, font="-family {Prototype} -size 12")
        search_entry2['values'] = event_list
        search_entry2.grid(row=0, column=8, padx=10, pady=10)
        search_entry2.bind("<<ComboboxSelected>>")

        empty_label3 = Label(Searchframe,font="-family {Prototype} -size 12", bg = 'white')
        empty_label3.grid(row=0, column=9, padx=10, pady=10)

        search_event = tk.Button(Searchframe, borderwidth=0, text = 'Search', fg = 'white', font="-family {Prototype} -size 12",
                                 height = 0, width = 12, command = y.search)
        search_event.grid(row=0, column=10, padx=10, pady=10)
        search_event.configure(relief='flat')
        search_event.configure(background="#044c92")
        search_event.configure(cursor="hand2")
        search_event.configure(relief='solid')

        empty_label4 = Label(Searchframe, font="-family {Prototype} -size 12", bg='white')
        empty_label4.grid(row=0, column=11, padx=10, pady=10)

        # tree View Start
        global my_tree, records
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')

        # configure the tree view colors
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",  font="-size 9", height = 420)
        style.configure("Treeview.Heading", background = "#044c92", foreground = "white", font="-family {Prototype} -size 12")

        # change selected color
        style.map('Treeview',
                  background=[('selected', '#044c92')])

        # crate treview frame
        tree_frame = Frame(parent_frame, bg = "white", height = 420)
        tree_frame.place(relx=0.045, rely=0.25, height = 380)
        #tree_frame.pack(pady=(150,0))

        # treescrolly
        tree_scrolly = Scrollbar(tree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(tree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                               selectmode="extended")
        my_tree.pack(fill = BOTH, expand= 1)

        # configure scroll bar
        tree_scrolly.config(command=my_tree.yview)
        tree_scrollx.config(command=my_tree.xview)

        # define coloums
        my_tree['columns'] = ("VENUEID", "VENUENAME", "VENUEADDRESS", "VENUECAPACITY", "VENUECONTACT", "VENUECOST")

        # format our coloums
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("VENUEID", anchor=CENTER, width=160)
        my_tree.column("VENUENAME", anchor=CENTER, width=220)
        my_tree.column("VENUEADDRESS", anchor=CENTER, width=300)
        my_tree.column("VENUECAPACITY", anchor=CENTER, width=180)
        my_tree.column("VENUECONTACT", anchor=CENTER, width=180)
        my_tree.column("VENUECOST", anchor=CENTER, width=180)

        # define heading
        my_tree.heading("#0", text="", anchor=CENTER)
        my_tree.heading("VENUEID", text="Venue ID", anchor=CENTER)
        my_tree.heading("VENUENAME", text="Venue Name", anchor=CENTER)
        my_tree.heading("VENUEADDRESS", text="Venue Address", anchor=CENTER)
        my_tree.heading("VENUECAPACITY", text="Venue Capacity", anchor=CENTER)
        my_tree.heading("VENUECONTACT", text="Venue Contact", anchor=CENTER)
        my_tree.heading("VENUECOST", text="Venue Cost", anchor=CENTER)

        # data
        c.execute("""SELECT * FROM VENUE""")
        records = c.fetchall()

        # create stripped row tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#87cdee")

        # adding data
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], record[2], record[3], record[4], record[5]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], record[2], record[3], record[4], record[5]),
                               tags=('oddrow',))
            count += 1

        next_button = tk.Button(parent_frame, borderwidth=0, text='Next', fg='white',
                                 font="-family {Prototype} -size 12",
                                 height=0, width=12, command=y.next)
        next_button.place(relx = 0.865, rely = 0.9)
        next_button.configure(relief='flat')
        next_button.configure(background="#044c92")
        next_button.configure(cursor="hand2")
        next_button.configure(relief='solid')

    def additeminevent(self):
        q = itemq_entry.get()
        item =vitem_name.get()
        itemintrees = []
        for line in  myadf_tree.get_children():
            for value in myadf_tree.item(line)['values']:
                itemintrees.append(value)
                break
        if len(item) == 0 :
            messagebox.showerror("error","Select Any Item")
        elif item in itemintrees:
            messagebox.showerror("error","Item Already Added")
        elif len(q) == 0 or q.isdecimal() == False or "0" == q[0:1]:
            messagebox.showerror("error","Invalid Quantity")
        else:
            it_count = len(myadf_tree.get_children())
            if it_count % 2 == 0:
                myadf_tree.insert(parent='', index='end', iid=it_count, text='', values=(item,q),
                                  tags=('evenrow',))
            else:
                myadf_tree.insert(parent='', index='end', iid=it_count, text='', values=(item,q),
                                  tags=('oddrow',))
    def deleteiteminevent(self):
        try :
            x = myadf_tree.selection()[0]
            myadf_tree.delete(x)
        except:
            messagebox.showerror("error","Select Item from table!")

    def addserviceinevent(self):
        service = vservice_name.get()
        serviceintrees = []
        for line in myads_tree.get_children():
            for value in myads_tree.item(line)['values']:
                serviceintrees.append(value)
                break
        if len(service) == 0:
            messagebox.showerror("error", "Select Any Service")
        elif service in serviceintrees:
            messagebox.showerror("error","Service Already Added")
        else:
            query = """SELECT SERVICECOST FROM SERVICE WHERE SERVICENAME = :a"""
            data =  c.execute(query,a= service)
            servicecost = data.fetchall()
            st_count = len(myads_tree.get_children())
            if st_count % 2 == 0:
                myads_tree.insert(parent='', index='end', iid=st_count, text='', values=(service, servicecost),
                                  tags=('evenrow',))
            else:
                myads_tree.insert(parent='', index='end', iid=st_count, text='', values=(service, servicecost),
                                  tags=('oddrow',))


    def deleteserviceinevent(self):
        try :
            x = myads_tree.selection()[0]
            myads_tree.delete(x)
        except:
            messagebox.showerror("error","Select Service from table!")

    def calculatetotal(self):
        total = 0
        item_records =[]
        service_records=[]
        for line in  myadf_tree.get_children():
            record =[]
            for value in myadf_tree.item(line)['values']:
                record.append(value)
            item_records.append(record)

        for line in  myads_tree.get_children():
            record =[]
            for value in myads_tree.item(line)['values']:
                record.append(value)
            service_records.append(record)


        print("items: ", item_records)
        print("service: ",service_records)
        for record in item_records:
             query = """SELECT ITEMUNITCOST FROM FOOD WHERE ITEMNAME =:a"""
             data = c.execute(query,a=record[0])
             unitcost = data.fetchall()
             total = total + int(unitcost[0][0]) * int(record[1])

        dec_type = dec_name1.get()
        vname = customer_entry9.get()
        noguest = customer_entry7.get()
        query = """SELECT VENUECAPACITY FROM VENUE WHERE VENUENAME =:a"""
        data = c.execute(query,a=vname)
        capacity = data.fetchall()

        if len(noguest) == 0 or noguest.isdecimal() == False or int(noguest) > capacity[0][0] :
            messagebox.showerror("error","Invalid No of guest")
        elif len(dec_type) ==0:
            messagebox.showerror("error","Select Decoration Type")
        elif len(vname) == 0:
            messagebox.showerror("error","Enter Venue")
        else:
            for record in service_records:
                query = """SELECT SERVICECOST FROM SERVICE WHERE SERVICENAME =:a"""
                data = c.execute(query, a=record[0])
                unitcost = data.fetchall()
                if record[0].lower() == 'chair' :
                    total = total + int(unitcost[0][0]) * int(noguest)
                elif record[0].lower() == 'table':
                    total = total + int(unitcost[0][0] * round(int(noguest)/8))
                else:
                    total = total + int(unitcost[0][0])

            query = "SELECT VENUECOST FROM VENUE WHERE VENUENAME=:a"
            data = c.execute(query,a =vname)
            row = c.fetchall()
            total = total + int(row[0][0])

            query = "SELECT DECORATIONCOST FROM DECORATION WHERE DECORATIONTYPE=:a"
            data = c.execute(query, a=dec_type)
            row = c.fetchall()
            total = total + int(row[0][0])

            total_entry.config(state='normal')
            total_entry.delete(0,END)
            total_entry.insert(0,total)
            total_entry.config(state='readonly')

    def booknow(self):
        eventid = eventnextid
        advancepayment = adpay
        total = total_entry.get()
        cid = customer_id_entry.get()
        cname = customer_name_entry.get()
        cemail = customer_email_entry.get()
        cnic = customer_cnic_entry.get()
        ccontact =customer_contact_entry.get()
        caddress = customer_address_entry.get()
        eventtype = e_type.get()
        dec_type = dec_name1.get()
        vname = customer_entry9.get()
        noguest = customer_entry7.get()
        query = """SELECT VENUECAPACITY FROM VENUE WHERE VENUENAME =:a"""
        data = c.execute(query, a=vname)
        capacity = data.fetchall()


        item_records = []
        service_records = []
        for line in myadf_tree.get_children():
            record = []
            for value in myadf_tree.item(line)['values']:
                record.append(value)
            item_records.append(record)

        for line in myads_tree.get_children():
            record = []
            for value in myads_tree.item(line)['values']:
                record.append(value)
            service_records.append(record)
        if len(total) == 0:
            messagebox.showerror("error","First Calculate Total Amount")
        elif len(cid) == 0 or cid.isdecimal() == False:
            messagebox.showerror("error","Invalid Customer ID")
        elif len(cname) > 30 or len(cname) == 0:
            messagebox.showerror("error","Invalid Name")
        elif len(cemail) >30 or len(cemail) == 0:
            messagebox.showerror("error","Invalid Email")
        elif len(cnic) > 13 or len(cnic) < 13 or len(cnic) == 0 or cnic.isdecimal() == False:
            messagebox.showerror("error","Invalid CNIC")
        elif len(ccontact) >11 or len(ccontact) < 11 or len(ccontact) == 0 or ccontact.isdecimal() == False:
            messagebox.showerror("error","Invalid Contact")
        elif len(caddress) > 50 or len(caddress) == 0:
            messagebox.showerror("error","Invalid Address")
        elif len(noguest) == 0 or noguest.isdecimal() == False or int(noguest) > capacity[0][0] :
            messagebox.showerror("error","Invalid No of guest")
        elif len(dec_type) == 0:
            messagebox.showerror("error","Select Decoration Type")
        elif len(vname) == 0:
            messagebox.showerror("error","Enter Venue")
        else:
            #adding in customer
            query ="""INSERT INTO CUSTOMER VALUES(:a,:b,:c,:d,:e,:f)"""
            c.execute(query,a=int(cid), b=cname, c=int(cnic), d=int(ccontact), e=cemail, f=caddress)

            # adding in event
            query = """SELECT EVENTTYPEID FROM EVENTTYPE WHERE EVENTTYPENAME = :x"""
            c.execute(query, x = eventtype)
            eventtypeid = c.fetchall()

            query = """SELECT DECORATIONID FROM DECORATION WHERE DECORATIONTYPE = :x"""
            c.execute(query, x=dec_type)
            decorationid = c.fetchall()

            query ="""INSERT INTO EVENT VALUES(:a,:b,TO_DATE(:c,'YYYY-MM-DD'),:d,:e,:f,:g,:h)"""
            c.execute(query, a=int(eventid), b=int(eventtypeid[0][0]), c=eventdate, d= int(noguest), e=int(advancepayment), f=int(cid),g=int(empidget), h=int(decorationid[0][0]))

            #ADDING IN EVENTDETAILS
            query = """SELECT VENUEID FROM VENUE WHERE VENUENAME = :x"""
            c.execute(query, x=vname)
            venueid = c.fetchall()

            query ="""INSERT INTO EVENTDETAIL VALUES(:a,:b,:c)"""
            c.execute(query, a=int(eventid), b=int(venueid[0][0]), c=int(total))

            #ADDING IN FOODDETAILS
            for item in item_records:
                query = """SELECT ITEMID FROM FOOD WHERE ITEMNAME = :x"""
                c.execute(query, x=item[0])
                itemid = c.fetchall()

                query = """INSERT INTO FOODDETAIL VALUES(:a,:b,:c)"""
                c.execute(query, a=int(eventid), b=int(itemid[0][0]), c=int(item[1]))

            #ADDING IN SERVICEDETAIL
            for service in service_records:
                query = """SELECT SERVICEID FROM SERVICE WHERE SERVICENAME = :x"""
                c.execute(query, x=service[0])
                serviceid = c.fetchall()

                query = """INSERT INTO SERVICEDETAIL VALUES(:a,:b)"""
                c.execute(query, a=int(eventid), b=int(serviceid[0][0]))

            c.execute("COMMIT")
            messagebox.showinfo('showinfo', 'Book event successfully')
            y.home()



    def next(self):
        global adpay, eventdate, dec_name1, customer_entry9, customer_entry7,total_entry,customer_name_entry,customer_cnic_entry,customer_id_entry,customer_contact_entry,customer_email_entry,customer_address_entry
        eventdate = cal.get()
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        if len(values) == 0:
            messagebox.showerror("error","Select Venue!")
        elif len(e_type.get()) == 0:
            messagebox.showerror("error","Select Event Type!")
        else:
            y.clear_frame()
            #CUSTOMER DETAIL Frame
            customerframe = LabelFrame(parent_frame, background="white", width='920px', height='50px', text = 'Add Event Detail',
                       cursor="hand2", relief='groove', bd = 2, font= "-family {Prototype} -size 15", fg ="#044c92",
                                 labelanchor = NW)
            customerframe.place(relx=0.085, rely=0.07)

            empty_label1 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label1.grid(row=0, column=0, padx=10, pady=10)

            customer_label1 = Label(customerframe, text="Customer ID", justify="center", bg="white", fg="black",
                       font="-family {Prototype} -size 12")
            customer_label1.grid(row = 0, column = 1, padx = 10, pady = 10)

            customer_id_entry = Entry(customerframe, relief = 'solid', bd = 1, font="-family {Prototype} -size 12")
            c.execute("""Select max (CUSTOMERID) FROM CUSTOMER""")
            customernextid = c.fetchall()
            customernextid = customernextid[0][0] + 1
            customer_id_entry.insert(0, customernextid)
            customer_id_entry.config(state='readonly')
            customer_id_entry.grid(row = 0, column = 2, padx = 10, pady = 10)

            empty_label2 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label2.grid(row=0, column=3, padx=10, pady=10)

            empty_label13 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label13.grid(row=1, column=0, padx=10, pady=10)

            customer_label2 = Label(customerframe, text="Customer Name", justify="center", bg="white", fg="black",
                              font="-family {Prototype} -size 12")
            customer_label2.grid(row=1, column=1, padx=10, pady=10)

            customer_name_entry = Entry(customerframe, relief='solid', bd=1, font="-family {Prototype} -size 12")
            customer_name_entry.grid(row=1, column=2, padx=10, pady=10)

            empty_label3 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label3.grid(row=1, column=3, padx=10, pady=10)

            empty_label14 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label14.grid(row=2, column=0, padx=10, pady=10)

            customer_label3 = Label(customerframe, text="CNIC", justify="center", bg="white", fg="black",
                                font="-family {Prototype} -size 12")
            customer_label3.grid(row=2, column=1, padx=10, pady=10)

            customer_cnic_entry = Entry(customerframe, relief='solid', bd=1, font="-family {Prototype} -size 12")
            customer_cnic_entry.grid(row=2, column=2, padx=10, pady=10)

            empty_label4 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label4.grid(row=2, column=3, padx=10, pady=10)

            empty_label5 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label5.grid(row=3, column=0, padx=10, pady=10)

            customer_label4 = Label(customerframe, text="Contact", justify="center", bg="white", fg="black",
                                font="-family {Prototype} -size 12")
            customer_label4.grid(row=3, column=1, padx=10, pady=10)

            customer_contact_entry = Entry(customerframe, relief='solid', bd=1, font="-family {Prototype} -size 12")
            customer_contact_entry.grid(row=3, column=2, padx=10, pady=10)

            empty_label6 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label6.grid(row=3, column=3, padx=10, pady=10)

            empty_label16 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label16.grid(row=4, column=0, padx=10, pady=10)

            customer_label5 = Label(customerframe, text="Email", justify="center", bg="white", fg="black",
                                font="-family {Prototype} -size 12")
            customer_label5.grid(row=4, column=1, padx=10, pady=10)
            customer_email_entry = Entry(customerframe, relief='solid', bd=1, font="-family {Prototype} -size 12")
            customer_email_entry.grid(row=4, column=2, padx=10, pady=10)

            empty_label7 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label7.grid(row=4, column=3, padx=10, pady=10)

            empty_label17 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label17.grid(row=5, column=0, padx=10, pady=10)

            customer_label6 = Label(customerframe, text="Address", justify="center", bg="white", fg="black",
                                font="-family {Prototype} -size 12")
            customer_label6.grid(row=5, column=1, padx=10, pady=10)
            customer_address_entry = Entry(customerframe, relief='solid', bd=1, font="-family {Prototype} -size 12")
            customer_address_entry.grid(row=5, column=2, padx=10, pady=10)

            empty_label8 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label8.grid(row=5, column=3, padx=10, pady=10)

            empty_label9 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label9.grid(row=6, column=0, padx=10, pady=10)

            customer_label7 = Label(customerframe, text="No of Guest", justify="center", bg="white", fg="black",
                                font="-family {Prototype} -size 12")
            customer_label7.grid(row=6, column=1, padx=10, pady=10)
            customer_entry7 = Entry(customerframe, relief='solid', bd=1, font="-family {Prototype} -size 12")
            customer_entry7.grid(row=6, column=2, padx=10, pady=10)

            empty_label10 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label10.grid(row=6, column=3, padx=10, pady=10)

            empty_label18 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label18.grid(row=7, column=0, padx=10, pady=10)

            customer_label8 = Label(customerframe, text="Advance Payment", justify="center", bg="white", fg="black",
                                font="-family {Prototype} -size 12")
            customer_label8.grid(row=7, column=1, padx=10, pady=10)
            customer_entry8 = Entry(customerframe, relief='solid', bd=1, font="-family {Prototype} -size 12")
            adpay = round(int(values[-1]) * 0.5)
            customer_entry8.insert(0,adpay)
            customer_entry8.config(state='readonly')
            customer_entry8.grid(row=7, column=2, padx=10, pady=10)

            empty_label11 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label11.grid(row=7, column=3, padx=10, pady=10)

            empty_label11 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label11.grid(row=8, column=0, padx=10, pady=10)

            customer_label9 = Label(customerframe, text="Venue Name", justify="center", bg="white", fg="black",
                                font="-family {Prototype} -size 12")
            customer_label9.grid(row=8, column=1, padx=10, pady=10)
            customer_entry9 = Entry(customerframe, relief='solid', bd=1, font="-family {Prototype} -size 12")
            customer_entry9.insert(0,values[1])
            customer_entry9.config(state='readonly')
            customer_entry9.grid(row=8, column=2, padx=10, pady=10)

            empty_label12 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label12.grid(row=8, column=3, padx=10, pady=10)
#------------------------------------------------------------------------------
            empty_label12 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label12.grid(row=9, column=0, padx=10, pady=10)

            customer_label10 = Label(customerframe, text="Decoration Type", justify="center", bg="white", fg="black",
                                font="-family {Prototype} -size 12")
            customer_label10.grid(row=9, column=1, padx=10, pady=10)
            c.execute("""SELECT DECORATIOnTYPE FROM DECORATION""")
            row = c.fetchall()
            dec_name = []
            for i in row:
                dec_name.append(i[0])
            dec_name1 = StringVar()
            customer_entry10 = ttk.Combobox(customerframe, textvariable=dec_name1, font="-family {Prototype} -size 12")
            customer_entry10['values'] = dec_name
            customer_entry10.grid(row=9, column=2, padx=10, pady=10)
            customer_entry10.bind("<<ComboboxSelected>>")

            empty_label20 = Label(customerframe, font="-family {Prototype} -size 12", bg='white')
            empty_label20.grid(row=9, column=3, padx=10, pady=10)


            book_btn = tk.Button(parent_frame, text="Book", height=0, width=22, foreground='white',
                                font="-family {Prototype} -size 12", command=y.booknow)
            book_btn.configure(relief='flat')
            book_btn.configure(background="#044c92")
            book_btn.configure(borderwidth="0px")
            book_btn.configure(cursor="hand2")
            book_btn.configure(relief='flat')
            book_btn.place(relx = 0.16, rely =0.87)

            global myadf_tree,myads_tree,vitem_name, itemq_entry,vservice_name, serviceq_entry
            #add food tree
            # tree View Start
            # add some style
            style = ttk.Style()

            # pick a theme
            style.theme_use('default')

            # configure the tree view colors
            style.configure("Treeview",
                            background="#044c92",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="white",
                            width=1250)
            style.configure("Treeview.Heading", background="#044c92", foreground="white",
                            font="-family {Prototype} -size 12")
            # change selected color
            style.map('Treeview',
                      background=[('selected', '#044c92')])

            # crate treview frame
            tree_frame = Frame(parent_frame, width=653, height=550)
            tree_frame.configure(background="black")
            # tree_frame.pack(pady = (50,0))
            tree_frame.place(relx=0.45, rely=0.09, height=180)

            # treescrolly
            tree_scrolly = Scrollbar(tree_frame)
            tree_scrolly.pack(side=RIGHT, fill=Y)

            # treescrolly
            tree_scrollx = Scrollbar(tree_frame, orient='horizontal')
            tree_scrollx.pack(side=BOTTOM, fill=X)

            # create tree view
            myadf_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                                    selectmode="extended")
            myadf_tree.pack(fill=BOTH, expand=1)

            # configure scroll bar
            tree_scrolly.config(command=myadf_tree.yview)
            tree_scrollx.config(command=myadf_tree.xview)

            # define coloums
            myadf_tree['columns'] = ("ItemName", "Quantity")

            # format our coloums
            myadf_tree.column("#0", width=0, stretch=NO)
            myadf_tree.column("ItemName", anchor=CENTER, width=180)
            myadf_tree.column("Quantity", anchor=CENTER, width=150)

            # define heading
            myadf_tree.heading("#0", text="", anchor=W)
            myadf_tree.heading("ItemName", text="ITEM NAME", anchor=CENTER)
            myadf_tree.heading("Quantity", text="QUANTITY", anchor=CENTER)

            # create stripped row tags
            myadf_tree.tag_configure('oddrow', background="white")
            myadf_tree.tag_configure('evenrow', background="#87cdee")

            # Selecting food for event
            item_lable = Label(parent_frame, text="Item :", justify="center", bg="white", fg="black",
                                     font="-family {Prototype} -size 12")
            item_lable.place(relx = 0.72, rely = 0.1)
            c.execute("""SELECT ITEMNAME FROM FOOD""")
            row = c.fetchall()
            item_name = []
            for i in row:
                item_name.append(i[0])
            vitem_name = StringVar()
            itembox = ttk.Combobox(parent_frame, textvariable=vitem_name, font="-family {Prototype} -size 12")
            itembox['values'] = item_name
            itembox.place(relx= 0.79,rely =0.1)
            itembox.bind("<<ComboboxSelected>>")

            itemq_lable = Label(parent_frame, text="Quantity :", justify="center", bg="white", fg="black",
                               font="-family {Prototype} -size 12")
            itemq_lable.place(relx=0.72, rely=0.18)

            itemq_entry = Entry(parent_frame, relief='solid', bd=1, font="-family {Prototype} -size 12")
            itemq_entry.place(relx = 0.79,rely=0.18)

            additem_btn = tk.Button(parent_frame, text="ADD", height=0, width=15, foreground='white',
                                  font="-family {Prototype} -size 12", command=y.additeminevent)
            additem_btn.configure(relief='flat')
            additem_btn.configure(background="#044c92")
            additem_btn.configure(borderwidth="0px")
            additem_btn.configure(cursor="hand2")
            additem_btn.configure(relief='flat')
            additem_btn.place(relx=0.75, rely=0.26)

            deleteitem_btn = tk.Button(parent_frame, text="DELETE", height=0, width=15, foreground='white',
                                    font="-family {Prototype} -size 12", command=y.deleteiteminevent)
            deleteitem_btn.configure(relief='flat')
            deleteitem_btn.configure(background="#044c92")
            deleteitem_btn.configure(borderwidth="0px")
            deleteitem_btn.configure(cursor="hand2")
            deleteitem_btn.configure(relief='flat')
            deleteitem_btn.place(relx=0.87, rely=0.26)

            #add service tree here
            # tree View Start
            # add some style
            style = ttk.Style()

            # pick a theme
            style.theme_use('default')

            # configure the tree view colors
            style.configure("Treeview",
                            background="#044c92",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="white",
                            width=1250)
            style.configure("Treeview.Heading", background="#044c92", foreground="white",
                            font="-family {Prototype} -size 12")
            # change selected color
            style.map('Treeview',
                      background=[('selected', '#044c92')])

            # crate treview frame
            tree_frame2 = Frame(parent_frame, width=653, height=550)
            tree_frame2.configure(background="black")
            # tree_frame.pack(pady = (50,0))
            tree_frame2.place(relx=0.45, rely=0.5, height=180)

            # treescrolly
            tree_scrolly2 = Scrollbar(tree_frame2)
            tree_scrolly2.pack(side=RIGHT, fill=Y)

            # treescrolly
            tree_scrollx2 = Scrollbar(tree_frame2, orient='horizontal')
            tree_scrollx2.pack(side=BOTTOM, fill=X)

            # create tree view
            myads_tree = ttk.Treeview(tree_frame2, yscrollcommand=tree_scrolly2.set, xscrollcommand=tree_scrollx2.set,
                                      selectmode="extended")
            myads_tree.pack(fill=BOTH, expand=1)

            # configure scroll bar
            tree_scrolly2.config(command=myads_tree.yview)
            tree_scrollx2.config(command=myads_tree.xview)

            # define coloums
            myads_tree['columns'] = ("ServiceName", "ServiceCost")

            # format our coloums
            myads_tree.column("#0", width=0, stretch=NO)
            myads_tree.column("ServiceName", anchor=CENTER, width=180)
            myads_tree.column("ServiceCost", anchor=CENTER, width=150)

            # define heading
            myads_tree.heading("#0", text="", anchor=W)
            myads_tree.heading("ServiceName", text="SERVICE NAME", anchor=CENTER)
            myads_tree.heading("ServiceCost", text="COST", anchor=CENTER)

            # create stripped row tags
            myads_tree.tag_configure('oddrow', background="white")
            myads_tree.tag_configure('evenrow', background="#87cdee")

            # Selecting food for event
            service_lable = Label(parent_frame, text="Service :", justify="center", bg="white", fg="black",
                               font="-family {Prototype} -size 12")
            service_lable.place(relx=0.72, rely=0.51)
            c.execute("""SELECT SERVICENAME FROM SERVICE""")
            row = c.fetchall()
            service_name = []
            for i in row:
                service_name.append(i[0])
            vservice_name = StringVar()
            servicebox = ttk.Combobox(parent_frame, textvariable=vservice_name, font="-family {Prototype} -size 12")
            servicebox['values'] = service_name
            servicebox.place(relx=0.79, rely=0.51)
            servicebox.bind("<<ComboboxSelected>>")


            addservice_btn = tk.Button(parent_frame, text="ADD", height=0, width=15, foreground='white',
                                    font="-family {Prototype} -size 12", command=y.addserviceinevent)
            addservice_btn.configure(relief='flat')
            addservice_btn.configure(background="#044c92")
            addservice_btn.configure(borderwidth="0px")
            addservice_btn.configure(cursor="hand2")
            addservice_btn.configure(relief='flat')
            addservice_btn.place(relx=0.75, rely=0.59)

            deleteservice_btn = tk.Button(parent_frame, text="DELETE", height=0, width=15, foreground='white',
                                       font="-family {Prototype} -size 12", command=y.deleteserviceinevent)
            deleteservice_btn.configure(relief='flat')
            deleteservice_btn.configure(background="#044c92")
            deleteservice_btn.configure(borderwidth="0px")
            deleteservice_btn.configure(cursor="hand2")
            deleteservice_btn.configure(relief='flat')
            deleteservice_btn.place(relx=0.87, rely=0.59)

            total_lable = Label(parent_frame, text="Total :", justify="center", bg="white", fg="black",
                                   font="-family {Prototype} -size 12")
            total_lable.place(relx=0.72, rely=0.75)

            total_entry = Entry(parent_frame, relief='solid', bd=1, font="-family {Prototype} -size 12")
            total_entry.config(state='readonly')
            total_entry.place(relx=0.79, rely=0.75)

            calculate_btn = tk.Button(parent_frame, text="Calculate  Total", height=0, width=20, foreground='white',
                                          font="-family {Prototype} -size 12", command=y.calculatetotal)
            calculate_btn.configure(relief='flat')
            calculate_btn.configure(background="#044c92")
            calculate_btn.configure(borderwidth="0px")
            calculate_btn.configure(cursor="hand2")
            calculate_btn.configure(relief='flat')
            calculate_btn.place(relx=0.8, rely=0.83)




    def venue(self):
        global sv_entry, myv_tree, sv_var
        y.clear_frame()
        parent_frame.configure(background="white")

        vtree_frame = LabelFrame(parent_frame, text="Venue Detail", width=1224, height=550,
                                 font="-family {Prototype} -size 15",
                                 fg="#044c92", bg="white", bd=2, relief='groove')
        vtree_frame.place(relx=0.05, rely=0.05)
        sv_var = IntVar()
        idf_r = Radiobutton(vtree_frame, text="ID", variable=sv_var, value=0, bg='white',
                            font="-family {Prototype} -size 12")
        idf_r.place(relx=0.01, rely=0.02)
        namev_r = Radiobutton(vtree_frame, text="Name", variable=sv_var, value=1, bg='white',
                              font="-family {Prototype} -size 12")
        namev_r.place(relx=0.08, rely=0.02)
        sv_entry = Entry(vtree_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        sv_entry.place(relx=0.22, rely=0.02)
        sv_entry.bind("<KeyRelease>", y.checkentryvenue)

        # tree View Start
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')

        # configure the tree view colors
        style.configure("Treeview",
                        background="#044c92",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        width=1250)
        style.configure("Treeview.Heading", background="#044c92", foreground="white",
                        font="-family {Prototype} -size 12")
        # change selected color
        style.map('Treeview',
                  background=[('selected', '#044c92')])

        # crate treview frame
        tree_frame = Frame(vtree_frame, width=653, height=550)
        tree_frame.configure(background="black")
        tree_frame.place(relx=0.0, rely=0.1, height=470)

        # treescrolly
        tree_scrolly = Scrollbar(tree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(tree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        myv_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                                selectmode="extended")
        myv_tree.pack(fill=BOTH, expand=1)

        # configure scroll bar
        tree_scrolly.config(command=myv_tree.yview)
        tree_scrollx.config(command=myv_tree.xview)

        # define coloums
        myv_tree['columns'] = (
            "VenueID", "VenueName", "VenueAddress", "VenueCapacity", "VenueContact", "VenueCost")

        # format our coloums
        myv_tree.column("#0", width=0, stretch=NO)
        myv_tree.column("VenueID", anchor=CENTER, width=160)
        myv_tree.column("VenueName", anchor=CENTER, width=200)
        myv_tree.column("VenueAddress", anchor=CENTER, width=300)
        myv_tree.column("VenueCapacity", anchor=CENTER, width=180)
        myv_tree.column("VenueContact", anchor=CENTER, width=180)
        myv_tree.column("VenueCost", anchor=CENTER, width=180)

        # define heading
        myv_tree.heading("#0", text="", anchor=W)
        myv_tree.heading("VenueID", text="VENUE ID", anchor=CENTER)
        myv_tree.heading("VenueName", text="VENUE NAME", anchor=CENTER)
        myv_tree.heading("VenueAddress", text="VENUE ADDRESS", anchor=CENTER)
        myv_tree.heading("VenueCapacity", text="VENUE CAPACITY", anchor=CENTER)
        myv_tree.heading("VenueContact", text="VENUE CONTACT", anchor=CENTER)
        myv_tree.heading("VenueCost", text="VENUE COST", anchor=CENTER)

        # create stripped row tags
        myv_tree.tag_configure('oddrow', background="white")
        myv_tree.tag_configure('evenrow', background="#87cdee")

        # data
        y.viewallvenue()

    def food(self):
        global sf_entry, myf_tree, sf_var, foodid_entry, fname_entry, funitprice_entry, f_v_ID_entry
        y.clear_frame()
        parent_frame.configure(background="white")

        ftree_frame = LabelFrame(parent_frame, text="Food Detail", width=653, height=550,
                                 font="-family {Prototype} -size 15",
                                 fg="#044c92", bg="white", bd=2, relief='groove')
        ftree_frame.place(relx=0.02, rely=0.05)
        sf_var = IntVar()
        idf_r = Radiobutton(ftree_frame, text="ID", variable=sf_var, value=0, bg='white',
                            font="-family {Prototype} -size 12")
        idf_r.place(relx=0.01, rely=0.02)
        namef_r = Radiobutton(ftree_frame, text="Name", variable=sf_var, value=1, bg='white',
                              font="-family {Prototype} -size 12")
        namef_r.place(relx=0.08, rely=0.02)
        sf_entry = Entry(ftree_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        sf_entry.place(relx=0.22, rely=0.02)
        sf_entry.bind("<KeyRelease>", y.checkentryfood)

        # tree View Start
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')

        # configure the tree view colors
        style.configure("Treeview",
                        background="#044c92",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        width=1250)
        style.configure("Treeview.Heading", background="#044c92", foreground="white",
                        font="-family {Prototype} -size 12")
        # change selected color
        style.map('Treeview',
                  background=[('selected', '#044c92')])

        # crate treview frame
        tree_frame = Frame(ftree_frame, width=653, height=550)
        tree_frame.configure(background="black")
        #tree_frame.pack(pady = (50,0))
        tree_frame.place(relx = 0.0, rely = 0.1, height = 470)

        # treescrolly
        tree_scrolly = Scrollbar(tree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(tree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        myf_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                                selectmode="extended")
        myf_tree.pack(fill=BOTH, expand=1)

        # configure scroll bar
        tree_scrolly.config(command=myf_tree.yview)
        tree_scrollx.config(command=myf_tree.xview)

        # define coloums
        myf_tree['columns'] = (
            "ItemID", "ItemName", "ItemUnitCost", "VendorID")

        # format our coloums
        myf_tree.column("#0", width=0, stretch=NO)
        myf_tree.column("ItemID", anchor=CENTER, width=150)
        myf_tree.column("ItemName", anchor=CENTER, width=180)
        myf_tree.column("ItemUnitCost", anchor=CENTER, width=150)
        myf_tree.column("VendorID", anchor=CENTER, width=150)

        # define heading
        myf_tree.heading("#0", text="", anchor=W)
        myf_tree.heading("ItemID", text="ITEM ID", anchor=CENTER)
        myf_tree.heading("ItemName", text="ITEM NAME", anchor=CENTER)
        myf_tree.heading("ItemUnitCost", text="ITEM UNIT COST", anchor=CENTER)
        myf_tree.heading("VendorID", text="VENDOR ID", anchor=CENTER)

        # create stripped row tags
        myf_tree.tag_configure('oddrow', background="white")
        myf_tree.tag_configure('evenrow', background="#87cdee")

        # data
        y.viewallfood()
        #------------------------------------VENDOR------------------------------------------
        global svendor_entry, myvendor_tree, svendor_var, vendorid_entry, vendorname_entry, vendorcontact_entry, vendoraddress_entry
        vendortree_frame = LabelFrame(parent_frame, text="Vendor Detail", width=653, height=550,
                                      font="-family {Prototype} -size 15",
                                      fg="#044c92", bg="white", bd=2, relief='groove')
        vendortree_frame.place(relx=0.51, rely=0.05)
        svendor_var = IntVar()
        idvendor_r = Radiobutton(vendortree_frame, text="ID", variable=svendor_var, value=0, bg='white',
                                 font="-family {Prototype} -size 12")
        idvendor_r.place(relx=0.01, rely=0.02)
        namevendor_r = Radiobutton(vendortree_frame, text="Name", variable=svendor_var, value=1, bg='white',
                                   font="-family {Prototype} -size 12")
        namevendor_r.place(relx=0.08, rely=0.02)
        svendor_entry = Entry(vendortree_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        svendor_entry.place(relx=0.22, rely=0.02)
        svendor_entry.bind("<KeyRelease>", y.checkentryvendor)
        # tree View Start
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')

        # configure the tree view colors
        style.configure("Treeview",
                        background="#044c92",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        width=1250)
        style.configure("Treeview.Heading", background="#044c92", foreground="white",
                        font="-family {Prototype} -size 12")
        # change selected color
        style.map('Treeview',
                  background=[('selected', '#044c92')])

        # crate treview frame
        vtree_frame = Frame(vendortree_frame, width=1250, height=300)
        vtree_frame.configure(background="black")
        vtree_frame.place(relx=0.0, rely=0.1, height=470, width = 650)
        #vtree_frame.pack(pady=(50, 0))

        # treescrolly
        tree_scrolly = Scrollbar(vtree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(vtree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        myvendor_tree = ttk.Treeview(vtree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                                     selectmode="extended")
        myvendor_tree.pack(fill=BOTH, expand=1)

        # configure scroll bar
        tree_scrolly.config(command=myvendor_tree.yview)
        tree_scrollx.config(command=myvendor_tree.xview)

        # define coloums
        myvendor_tree['columns'] = (
            "VendorID", "VendorName", "VendorContact", "VendorAddress")

        # format our coloums
        myvendor_tree.column("#0", width=0, stretch=NO)
        myvendor_tree.column("VendorID", anchor=CENTER, width=120)
        myvendor_tree.column("VendorName", anchor=CENTER, width=150)
        myvendor_tree.column("VendorContact", anchor=CENTER, width=150)
        myvendor_tree.column("VendorAddress", anchor=CENTER, width=220)

        # define heading
        myvendor_tree.heading("#0", text="", anchor=W)
        myvendor_tree.heading("VendorID", text="VENDOR ID", anchor=CENTER)
        myvendor_tree.heading("VendorName", text="VENDOR NAME", anchor=CENTER)
        myvendor_tree.heading("VendorContact", text="VENDOR CONTACT", anchor=CENTER)
        myvendor_tree.heading("VendorAddress", text="VENDOR ADDRESS", anchor=CENTER)

        # create stripped row tags
        myvendor_tree.tag_configure('oddrow', background="white")
        myvendor_tree.tag_configure('evenrow', background="#87cdee")

        # data
        y.viewallvendor()

    def services(self):
        global sdec_entry, mydec_tree, sdec_var, decid_entry, dectype_entry, deccost_entry
        global sser_entry, myser_tree, sser_var, serid_entry, sername_entry, sercost_entry
        y.clear_frame()
        parent_frame.configure(background="white")

        dectree_frame = LabelFrame(parent_frame, text="Decoration Detail", width=653, height=550,
                                  font="-family {Prototype} -size 15",
                                  fg="#044c92", bg="white", bd=2, relief='groove')
        dectree_frame.place(relx=0.02, rely=0.05)
        sdec_var = IntVar()
        iddec_r = Radiobutton(dectree_frame, text="ID", variable=sdec_var, value=0, bg='white',
                              font="-family {Prototype} -size 12")
        iddec_r.place(relx=0.01, rely=0.02)
        namedec_r = Radiobutton(dectree_frame, text="Name", variable=sdec_var, value=1, bg='white',
                                font="-family {Prototype} -size 12")
        namedec_r.place(relx=0.08, rely=0.02)
        sdec_entry = Entry(dectree_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        sdec_entry.place(relx=0.22, rely=0.02)
        sdec_entry.bind("<KeyRelease>", y.checkentrydec)
        # tree View Start
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')

        # configure the tree view colors
        style.configure("Treeview",
                        background="#044c92",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        width=1250)
        style.configure("Treeview.Heading", background="#044c92", foreground="white",
                        font="-family {Prototype} -size 12")
        # change selected color
        style.map('Treeview',
                  background=[('selected', '#044c92')])

        # crate treview frame
        tree_frame = Frame(dectree_frame, width=653, height=550)
        tree_frame.configure(background="black")
        tree_frame.place(relx=0.0, rely=0.1, height=470)
        #tree_frame.pack(pady=(50, 0))

        # treescrolly
        tree_scrolly = Scrollbar(tree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(tree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        mydec_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                                  selectmode="extended")
        mydec_tree.pack(fill=BOTH, expand=1)

        # configure scroll bar
        tree_scrolly.config(command=mydec_tree.yview)
        tree_scrollx.config(command=mydec_tree.xview)

        # define coloums
        mydec_tree['columns'] = (
            "DecorationID", "DecorationType", "DecorationCost")

        # format our coloums
        mydec_tree.column("#0", width=0, stretch=NO)
        mydec_tree.column("DecorationID", anchor=CENTER, width=200)
        mydec_tree.column("DecorationType", anchor=CENTER, width=230)
        mydec_tree.column("DecorationCost", anchor=CENTER, width=200)

        # define heading
        mydec_tree.heading("#0", text="", anchor=W)
        mydec_tree.heading("DecorationID", text="DECORATION ID", anchor=CENTER)
        mydec_tree.heading("DecorationType", text="DECORATION TYPE", anchor=CENTER)
        mydec_tree.heading("DecorationCost", text="DECORATION COST", anchor=CENTER)

        # create stripped row tags
        mydec_tree.tag_configure('oddrow', background="white")
        mydec_tree.tag_configure('evenrow', background="#87cdee")

        # data
        y.viewalldec()

        #---------------------------------------------SERVICES-------------------------------------------
        sertree_frame = LabelFrame(parent_frame, text="Service Detail", width=653, height=550,
                                   font="-family {Prototype} -size 15",
                                   fg="#044c92", bg="white", bd=2, relief='groove')
        sertree_frame.place(relx=0.51, rely=0.05)
        sser_var = IntVar()
        idser_r = Radiobutton(sertree_frame, text="ID", variable=sser_var, value=0, bg='white',
                              font="-family {Prototype} -size 12")
        idser_r.place(relx=0.01, rely=0.02)
        nameser_r = Radiobutton(sertree_frame, text="Name", variable=sser_var, value=1, bg='white',
                                font="-family {Prototype} -size 12")
        nameser_r.place(relx=0.08, rely=0.02)
        sser_entry = Entry(sertree_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        sser_entry.place(relx=0.22, rely=0.02)
        sser_entry.bind("<KeyRelease>", y.checkentryser)

        # tree View Start
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')

        # configure the tree view colors
        style.configure("Treeview",
                        background="#044c92",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        width=1250)
        style.configure("Treeview.Heading", background="#044c92", foreground="white",
                        font="-family {Prototype} -size 12")
        # change selected color
        style.map('Treeview',
                  background=[('selected', '#044c92')])

        # crate treview frame
        sertree_frame = Frame(sertree_frame, width=653, height=550)
        sertree_frame.configure(background="black")
        sertree_frame.place(relx=0.0, rely=0.1, height=470)
        #sertree_frame.pack(pady=(50, 0))

        # treescrolly
        tree_scrolly = Scrollbar(sertree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(sertree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        myser_tree = ttk.Treeview(sertree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                                  selectmode="extended")
        myser_tree.pack(fill=BOTH, expand=1)

        # configure scroll bar
        tree_scrolly.config(command=myser_tree.yview)
        tree_scrollx.config(command=myser_tree.xview)

        # define coloums
        myser_tree['columns'] = (
            "ServiceID", "ServiceName", "ServiceCost")

        # format our coloums
        myser_tree.column("#0", width=0, stretch=NO)
        myser_tree.column("ServiceID", anchor=CENTER, width=200)
        myser_tree.column("ServiceName", anchor=CENTER, width=230)
        myser_tree.column("ServiceCost", anchor=CENTER, width=200)

        # define heading
        myser_tree.heading("#0", text="", anchor=W)
        myser_tree.heading("ServiceID", text="SERVICE ID", anchor=CENTER)
        myser_tree.heading("ServiceName", text="SERVICE NAME", anchor=CENTER)
        myser_tree.heading("ServiceCost", text="SERVICE COST", anchor=CENTER)

        # create stripped row tags
        myser_tree.tag_configure('oddrow', background="white")
        myser_tree.tag_configure('evenrow', background="#87cdee")

        # data
        y.viewallser()

    def profile(self):
        global eemail_entry, econtact_entry, eaddress_entry, curr_pass_entry, new_pass_entry, conf_pass_entry
        y.clear_frame()
        parent_frame.configure(background="white")

        record_frame = LabelFrame(parent_frame, text="Personal Detail", width=1250, height=200,
                                  font="-family {Prototype} -size 20",
                                  fg="#044c92", bg="white", bd=2, relief='groove')
        record_frame.place(relx=0.22, rely=0.02)

        empid_lable = Label(record_frame, text="ID", font="-family {Prototype} -size 14", bg="white")
        empid_lable.grid(row=0, column=0, padx=10, pady=10)
        empid_entry = Entry(record_frame, font="-family {Prototype} -size 14", relief='solid', bd=1)
        empid_entry.grid(row=0, column=1, padx=10, pady=10)
        c.execute("SELECT * FROM EMPLOYEE WHERE EMPLOYEEID = :x", x = empidget)
        allemprec = c.fetchall()
        empid_entry.insert(0, allemprec[0][0])
        empid_entry.config(state='readonly')

        ename_lable = Label(record_frame, text="Name", font="-family {Prototype} -size 14", bg='white')
        ename_lable.grid(row=0, column=2, padx=10, pady=10)
        ename_entry = Entry(record_frame, font="-family {Prototype} -size 14", relief='solid', bd=1)
        ename_entry.grid(row=0, column=3, padx=10, pady=10)
        ename_entry.insert(0, allemprec[0][1])
        ename_entry.config(state='readonly')

        eemail_lable = Label(record_frame, text="Email", font="-family {Prototype} -size 14", bg='white')
        eemail_lable.grid(row=1, column=0, padx=10, pady=10)
        eemail_entry = Entry(record_frame, font="-family {Prototype} -size 14", relief='solid', bd=1)
        eemail_entry.grid(row=1, column=1, padx=10, pady=10)
        eemail_entry.insert(0, allemprec[0][2])

        econtact_lable = Label(record_frame, text="Contact", font="-family {Prototype} -size 14", bg='white')
        econtact_lable.grid(row=1, column=2, padx=10, pady=10)
        econtact_entry = Entry(record_frame, font="-family {Prototype} -size 14", relief='solid', bd=1)
        econtact_entry.grid(row=1, column=3, padx=10, pady=10)
        contact=allemprec[0][3]
        new_contact = "0"+str(contact)
        econtact_entry.insert(0, new_contact)

        eaddress_lable = Label(record_frame, text="Address", font="-family {Prototype} -size 14", bg='white')
        eaddress_lable.grid(row=2, column=0, padx=10, pady=10)
        eaddress_entry = Entry(record_frame, font="-family {Prototype} -size 14", relief='solid', bd=1)
        eaddress_entry.grid(row=2, column=1, padx=10, pady=10)
        eaddress_entry.insert(0, allemprec[0][4])

        ehdate_lable = Label(record_frame, text="Hire-Date", font="-family {Prototype} -size 14", bg='white')
        ehdate_lable.grid(row=2, column=2, padx=10, pady=10)
        ehdate_entry = Entry(record_frame, font="-family {Prototype} -size 14", relief='solid', bd=1)
        ehdate_entry.grid(row=2, column=3, padx=10, pady=10)
        h_date = allemprec[0][5]
        h_date = datetime.date(h_date)
        ehdate_entry.insert(0, h_date)
        ehdate_entry.config(state='readonly')

        esal_lable = Label(record_frame, text="Salary", font="-family {Prototype} -size 14", bg='white')
        esal_lable.grid(row=3, column=0, padx=10, pady=10)
        esal_entry = Entry(record_frame, font="-family {Prototype} -size 14", relief='solid', bd=1)
        esal_entry.grid(row=3, column=1, padx=10, pady=10)
        esal_entry.insert(0, allemprec[0][6])
        esal_entry.config(state='readonly')

        upd_btn = tk.Button(parent_frame, text="UPDATE", height=0, width=17, foreground='white',
                            font="-family {Prototype} -size 16", command=y.update_profile)
        upd_btn.configure(relief='flat')
        upd_btn.configure(background="#044c92")
        upd_btn.configure(borderwidth="0px")
        upd_btn.configure(cursor="hand2")
        upd_btn.configure(relief='flat')
        upd_btn.place(relx=0.42, rely=0.42)

        change_pass_frame = LabelFrame(parent_frame, text="Change Password", width=1250, height=200,
                                  font="-family {Prototype} -size 20",
                                  fg="#044c92", bg="white", bd=2, relief='groove')
        change_pass_frame.place(relx=0.32, rely=0.52)

        curr_pass_lable = Label(change_pass_frame, text="Current Password", font="-family {Prototype} -size 14", bg="white")
        curr_pass_lable.grid(row=0, column=0, padx=10, pady=10)
        curr_pass_entry = Entry(change_pass_frame, font="-family {Prototype} -size 14", relief='solid', bd=1, show = '*')
        curr_pass_entry.grid(row=0, column=1, padx=10, pady=10)

        new_pass_lable = Label(change_pass_frame, text="New Password", font="-family {Prototype} -size 14", bg="white")
        new_pass_lable.grid(row=1, column=0, padx=10, pady=10)
        new_pass_entry = Entry(change_pass_frame, font="-family {Prototype} -size 14", relief='solid', bd=1, show = '*')
        new_pass_entry.grid(row=1, column=1, padx=10, pady=10)

        conf_pass_lable = Label(change_pass_frame, text="Confirm Password", font="-family {Prototype} -size 14", bg="white")
        conf_pass_lable.grid(row=2, column=0, padx=10, pady=10)
        conf_pass_entry = Entry(change_pass_frame, font="-family {Prototype} -size 14", relief='solid', bd=1, show = '*')
        conf_pass_entry.grid(row=2, column=1, padx=10, pady=10)

        chng_pass_btn = tk.Button(parent_frame, text="Change Password", height=0, width=17, foreground='white',
                            font="-family {Prototype} -size 16", command=y.change_pass)
        chng_pass_btn.configure(relief='flat')
        chng_pass_btn.configure(background="#044c92")
        chng_pass_btn.configure(borderwidth="0px")
        chng_pass_btn.configure(cursor="hand2")
        chng_pass_btn.configure(relief='flat')
        chng_pass_btn.place(relx=0.42, rely=0.85)

    def logout(self):
        top.destroy()
        import main
        main.x.mainpagegui()



    def mainpagegui(self):
        global top
        top = Tk()
        topimg = PhotoImage(file='images/logon.png')
        top.iconphoto(False, topimg)
        top.geometry("1920x1001+-95+15")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.state('zoomed')
        top.resizable(0, 0)
        top.title("Event Mangemnt System")
        top.configure(background="#ffffff")


        topframe = tk.Frame(top)
        topframe.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=1)
        topframe.configure(relief='flat')
        topframe.configure(background="white")
        banericon = PhotoImage(file="images\Topbanner.png")
        topbanner = Label(topframe, image=banericon)
        topbanner.place(relx=0.0, rely=0.1)
        topbanner.pack()

        topframe2 = tk.Frame(top)
        topframe2.place(relx=0.0, rely=0.1, relheight=0.07
                       , relwidth=1)
        topframe2.configure(relief='flat')
        topframe2.configure(background="#044c92")

        logoicon = PhotoImage(file="images\logo.png")
        logo = Label(image=logoicon)
        bt_home = tk.Button(topframe2,image = logoicon,borderwidth=0,command=y.home)
        bt_home.place(relx=0.016, rely=0.02, height="40px", width="40px")
        bt_home.configure(relief='flat')
        bt_home.configure(background="#044c92")
        bt_home.configure(borderwidth="0px")
        bt_home.configure(cursor="hand2")
        bt_home.configure(relief= 'flat')



        bt_register = tk.Button(topframe2,command=y.bookevent)
        bt_register.place(relx=0.07, rely=0.2, height=30, width=180)
        bt_register.configure(activebackground="white")
        bt_register.configure(activeforeground="#044c92")
        bt_register.configure(background="white")
        bt_register.configure(disabledforeground="white")
        bt_register.configure(font="-family {Prototype} -size 13")
        bt_register.configure(foreground="#044c92")
        bt_register.configure(highlightbackground="white")
        bt_register.configure(highlightcolor="white")
        bt_register.configure(text='''Book Event''')
        bt_register.configure(relief='flat')
        bt_register.configure(cursor='hand2')
        # #
        bt_venue = tk.Button(topframe2,command=y.venue)
        bt_venue.place(relx=0.22, rely=0.2, height=30, width=180)
        bt_venue.configure(activebackground="white")
        bt_venue.configure(activeforeground="#044c92")
        bt_venue.configure(background="white")
        bt_venue.configure(cursor="hand2")
        bt_venue.configure(disabledforeground="#a3a3a3")
        bt_venue.configure(font="-family {Prototype} -size 13")
        bt_venue.configure(foreground="#044c92")
        bt_venue.configure(highlightbackground="white")
        bt_venue.configure(highlightcolor="white")
        bt_venue.configure(relief="flat")
        bt_venue.configure(text='''Venue''')
        #
        bt_food = tk.Button(topframe2,command=y.food)
        bt_food.place(relx=0.37, rely=0.2, height=30, width=180)
        bt_food.configure(activebackground="white")
        bt_food.configure(activeforeground="#044c92")
        bt_food.configure(background="white")
        bt_food.configure(disabledforeground="#a3a3a3")
        bt_food.configure(font="-family {Prototype} -size 13")
        bt_food.configure(foreground="#044c92")
        bt_food.configure(highlightbackground="white")
        bt_food.configure(highlightcolor="white")
        bt_food.configure(cursor="hand2")
        bt_food.configure(relief="flat")
        bt_food.configure(text='''Food''')
        #
        bt_services = tk.Button(topframe2,command=y.services)
        bt_services.place(relx=0.52, rely=0.2, height=30, width=180)
        bt_services.configure(activebackground="white")
        bt_services.configure(activeforeground="#044c92")
        bt_services.configure(background="white")
        bt_services.configure(disabledforeground="white")
        bt_services.configure(font="-family {Prototype} -size 13")
        bt_services.configure(foreground="#044c92")
        bt_services.configure(highlightbackground="white")
        bt_services.configure(highlightcolor="white")
        bt_services.configure(relief="flat")
        bt_services.configure(text='''Service''')
        bt_services.configure(cursor="hand2")

        bt_profile = tk.Button(topframe2,command=y.profile)
        bt_profile.place(relx=0.67, rely=0.2, height=30, width=180)
        bt_profile.configure(activebackground="white")
        bt_profile.configure(activeforeground="#044c92")
        bt_profile.configure(background="white")
        bt_profile.configure(disabledforeground="white")
        bt_profile.configure(font="-family {Prototype} -size 13")
        bt_profile.configure(foreground="#044c92")
        bt_profile.configure(highlightbackground="white")
        bt_profile.configure(highlightcolor="white")
        bt_profile.configure(relief="flat")
        bt_profile.configure(text='''Profile''')
        bt_profile.configure(cursor="hand2")

        bt_logout = tk.Button(topframe2,command=y.logout)
        bt_logout.place(relx=0.82, rely=0.2, height=30, width=180)
        bt_logout.configure(activebackground="white")
        bt_logout.configure(activeforeground="#044c92")
        bt_logout.configure(background="white")
        bt_logout.configure(disabledforeground="white")
        bt_logout.configure(font="-family {Prototype} -size 13")
        bt_logout.configure(foreground="#044c92")
        bt_logout.configure(highlightbackground="white")
        bt_logout.configure(highlightcolor="white")
        bt_logout.configure(relief="flat")
        bt_logout.configure(text='''Logout''')
        bt_logout.configure(cursor="hand2")
        y.parent_frame()
        y.home()
        top.mainloop()


y = GUI()
#y.mainpagegui()