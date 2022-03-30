from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox , filedialog
from datetime import *
from tkcalendar import *
import cx_Oracle
import shutil
import os
global c, con
con = cx_Oracle.connect('databaseproject/databaseproject@//localhost:1521/pdborcll')
c = con.cursor()



class GUI:


    def parent_frame(self):
        global parent_frame
        parent_frame = tk.Frame(top)
        parent_frame.place(relx=0.0, rely=0.17, relheight=0.85, relwidth=1)
        parent_frame.configure(relief='flat')
        parent_frame.configure(background="white")


    def clear_frame(self):
        for widgets in parent_frame.winfo_children():
            widgets.destroy()

    def browsefile(self):
        global fileloc , fnames
        fileloc = filedialog.askopenfilenames(initialdir = "/",title = "Select a file",filetypes = (("JPEG","*.jpg*"),("PNG","*.png*")))
        if len(fileloc) == 5:
            pass
        else:
            messagebox.showerror("error","Select five images only")
            y.browsefile()


    def clear_empentries(self):
        empid_entry.config(state = 'normal')
        empid_entry.delete(0, END)
        ename_entry.delete(0, END)
        eemail_entry.delete(0, END)
        econtact_entry.delete(0, END)
        eaddress_entry.delete(0, END)
        ehdate_entry.delete(0, END)
        esal_entry.delete(0, END)
        empid_entry.insert(0, enextid)
        empid_entry.config(state='readonly')

    def clear_venueentries(self):
        venueid_entry.config(state='normal')
        venueid_entry.delete(0, END)
        vname_entry.delete(0, END)
        vaddress_entry.delete(0, END)
        vcontact_entry.delete(0, END)
        vcapacity_entry.delete(0, END)
        vcost_entry.delete(0, END)
        venueid_entry.insert(0,vnextid)
        venueid_entry.config(state="readonly")

    def clear_foodentries(self):
        foodid_entry.config(state='normal')
        foodid_entry.delete(0, END)
        fname_entry.delete(0, END)
        funitprice_entry.delete(0, END)
        f_v_ID_entry.delete(0, END)
        foodid_entry.insert(0,fnextid)
        foodid_entry.config(state='readonly')

    def clear_vendorentries(self):
        vendorid_entry.config(state='normal')
        vendorid_entry.delete(0, END)
        vendorname_entry.delete(0, END)
        vendorcontact_entry.delete(0, END)
        vendoraddress_entry.delete(0, END)
        vendorid_entry.insert(0,vendornextid)
        vendorid_entry.config(state='readonly')

    def clear_decentries(self):
        decid_entry.config(state='normal')
        decid_entry.delete(0, END)
        dectype_entry.delete(0, END)
        deccost_entry.delete(0, END)
        decid_entry.insert(0,decnextid)
        decid_entry.config(state='readonly')

    def clear_serentries(self):
        serid_entry.config(state='normal')
        serid_entry.delete(0, END)
        sername_entry.delete(0, END)
        sercost_entry.delete(0, END)
        serid_entry.insert(0,sernextid)
        serid_entry.config(state='readonly')


    def checkentry(self,e):
        typed = s_entry.get()
        selected = s_var.get()
        if typed == '':
            data = e_records
        else:
            data = []
            for record in e_records:
                if selected == 0:
                    if typed in str(record[selected]):
                        data.append(record)
                else:
                    if typed.lower() in record[selected].lower():
                        data.append(record)
        for record in my_tree.get_children():
            my_tree.delete(record)
        count=0
        for record in data:
            if count % 2 == 0:
                my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                               tags=('oddrow',))
            count +=1

    def checkentryvenue(self,e):
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
        count=0
        for record in data:
            if count % 2 == 0:
                myv_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],"0"+str(record[4]),record[5]),tags=('evenrow',))
            else:
                myv_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2], record[3], "0"+str(record[4]), record[5]),
                               tags=('oddrow',))
            count +=1

    def checkentryfood(self, e):
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
        count = 0
        for record in data:
            if count % 2 == 0:
                myf_tree.insert(parent='', index='end', iid=count, text='',
                                values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
            else:
                myf_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], record[2],record[3]),
                                tags=('oddrow',))
            count += 1

    def checkentryvendor(self, e):
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
        count = 0
        for record in data:
            if count % 2 == 0:
                myvendor_tree.insert(parent='', index='end', iid=count, text='',
                                     values=(record[0], record[1], "0" + str(record[2]), record[3]), tags=('evenrow',))
            else:
                myvendor_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], "0" + str(record[2]), record[3]),
                                     tags=('oddrow',))
            count += 1

    def checkentrydec(self, e):
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
        count = 0
        for record in data:
            if count % 2 == 0:
                mydec_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]),
                                  tags=('evenrow',))
            else:
                mydec_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], record[2]),
                                  tags=('oddrow',))
            count += 1

    def checkentryser(self, e):
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
        count = 0
        for record in data:
            if count % 2 == 0:
                myser_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]),
                                  tags=('evenrow',))
            else:
                myser_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], record[2]),
                                  tags=('oddrow',))
            count += 1



    def empselect_record(self,e):
        #clear entry
        empid_entry.config(state='normal')
        empid_entry.delete(0,END)
        ename_entry.delete(0,END)
        eemail_entry.delete(0,END)
        econtact_entry.delete(0,END)
        eaddress_entry.delete(0,END)
        ehdate_entry.delete(0,END)
        esal_entry.delete(0,END)

        #grab record
        selected = my_tree.focus()
        #grad record values
        values = my_tree.item(selected,'values')
        #entry insertion
        if len(values) !=0:
            empid_entry.insert(0, values[0])
            ename_entry.insert(0, values[1])
            eemail_entry.insert(0, values[2])
            econtact_entry.insert(0, values[3])
            eaddress_entry.insert(0, values[4])
            ehdate_entry.insert(0, values[5])
            esal_entry.insert(0, values[6])
            empid_entry.config(state='readonly')

    def vselect_record(self,e):
        #clear entry
        venueid_entry.config(state='normal')
        venueid_entry.delete(0,END)
        vname_entry.delete(0,END)
        vaddress_entry.delete(0,END)
        vcontact_entry.delete(0,END)
        vcapacity_entry.delete(0,END)
        vcost_entry.delete(0,END)

        #grab record
        selected = myv_tree.focus()
        #grad record values
        values = myv_tree.item(selected,'values')
        #entry insertion
        if len(values) !=0:
            venueid_entry.insert(0, values[0])
            vname_entry.insert(0, values[1])
            vaddress_entry.insert(0, values[2])
            vcapacity_entry.insert(0, values[3])
            vcontact_entry.insert(0, values[4])
            vcost_entry.insert(0, values[5])
            venueid_entry.config(state='readonly')

    def fselect_record(self, e):
        # clear entry
        foodid_entry.config(state='normal')
        foodid_entry.delete(0, END)
        fname_entry.delete(0, END)
        funitprice_entry.delete(0, END)
        f_v_ID_entry.delete(0, END)

        # grab record
        selected = myf_tree.focus()
        # grad record values
        values = myf_tree.item(selected, 'values')
        # entry insertion
        if len(values) != 0:
            foodid_entry.insert(0, values[0])
            fname_entry.insert(0, values[1])
            funitprice_entry.insert(0, values[2])
            f_v_ID_entry.insert(0, values[3])
            foodid_entry.config(state='readonly')

    def vendorselect_record(self, e):
        # clear entry
        vendorid_entry.config(state='normal')
        vendorid_entry.delete(0, END)
        vendorname_entry.delete(0, END)
        vendorcontact_entry.delete(0, END)
        vendoraddress_entry.delete(0, END)

        # grab record
        selected = myvendor_tree.focus()
        # grad record values
        values = myvendor_tree.item(selected, 'values')
        # entry insertion
        if len(values) != 0:
            vendorid_entry.insert(0, values[0])
            vendorname_entry.insert(0, values[1])
            vendorcontact_entry.insert(0, values[2])
            vendoraddress_entry.insert(0, values[3])
            vendorid_entry.config(state='readonly')

    def decselect_record(self, e):
        # clear entry
        decid_entry.config(state='normal')
        decid_entry.delete(0, END)
        dectype_entry.delete(0, END)
        deccost_entry.delete(0, END)

        # grab record
        selected = mydec_tree.focus()
        # grad record values
        values = mydec_tree.item(selected, 'values')
        # entry insertion
        if len(values) != 0:
            decid_entry.insert(0, values[0])
            dectype_entry.insert(0, values[1])
            deccost_entry.insert(0, values[2])
            decid_entry.config(state='readonly')

    def serselect_record(self, e):
        # clear entry
        serid_entry.config(state='normal')
        serid_entry.delete(0, END)
        sername_entry.delete(0, END)
        sercost_entry.delete(0, END)

        # grab record
        selected = myser_tree.focus()
        # grad record values
        values = myser_tree.item(selected, 'values')
        # entry insertion
        if len(values) != 0:
            serid_entry.insert(0, values[0])
            sername_entry.insert(0, values[1])
            sercost_entry.insert(0, values[2])
            serid_entry.config(state='readonly')


    def viewallemployee(self):
        global e_count,e_records
        c.execute("SELECT * FROM EMPLOYEE ORDER BY EMPLOYEEID ")
        e_records = c.fetchall()
        for record in my_tree.get_children():
            my_tree.delete(record)
        e_count = 0
        for record in e_records:
            date = record[5]
            date =datetime.date(date)
            if e_count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=e_count, text='', values=(
                    record[0], record[1], record[2], "0"+ str(record[3]), record[4], date, record[6]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=e_count, text='', values=(
                    record[0], record[1], record[2], "0"+str(record[3]), record[4], date, record[6]),
                               tags=('oddrow',))
            e_count += 1

    def viewallvenue(self):
        global v_count,v_records
        c.execute("SELECT * FROM VENUE ORDER BY VENUEID ")
        v_records = c.fetchall()
        for record in myv_tree.get_children():
            myv_tree.delete(record)
        v_count = 0
        for record in v_records:
            if v_count % 2 == 0:
                myv_tree.insert(parent='', index='end', iid=v_count, text='', values=(
                    record[0], record[1], record[2], record[3], "0"+str(record[4]), record[5]),
                               tags=('evenrow',))
            else:
                myv_tree.insert(parent='', index='end', iid=v_count, text='', values=(
                    record[0], record[1], record[2],record[3], "0"+str(record[4]), record[5]),
                               tags=('oddrow',))
            v_count += 1

    def viewallfood(self):
        global f_count, f_records
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
                    record[0], record[1], record[2], record[3]),
                                tags=('oddrow',))
            f_count += 1

    def viewallvendor(self):
        global vendor_count, vendor_records
        c.execute("SELECT * FROM VENDOR ORDER BY VENDORID ")
        vendor_records = c.fetchall()
        for record in myvendor_tree.get_children():
            myvendor_tree.delete(record)
        vendor_count = 0
        for record in vendor_records:
            if vendor_count % 2 == 0:
                myvendor_tree.insert(parent='', index='end', iid=vendor_count, text='', values=(
                    record[0], record[1], "0" + str(record[2]), record[3]),
                                     tags=('evenrow',))
            else:
                myvendor_tree.insert(parent='', index='end', iid=vendor_count, text='', values=(
                    record[0], record[1], "0" + str(record[2]), record[3]),
                                     tags=('oddrow',))
            vendor_count += 1

    def viewalldec(self):
        global dec_count, dec_records
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
                    record[0], record[1], record[2]),
                                  tags=('oddrow',))
            dec_count += 1

    def viewallser(self):
        global ser_count, ser_records
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
                    record[0], record[1], record[2]),
                                  tags=('oddrow',))
            ser_count += 1



    def addemployee(self):
        global enextid
        eid =empid_entry.get()
        ename =ename_entry.get()
        email =eemail_entry.get()
        econ =econtact_entry.get()
        edd =eaddress_entry.get()
        ed =ehdate_entry.get()
        esal =esal_entry.get()
        c.execute("SELECT * FROM EMPLOYEE")
        allempecords= c.fetchall()
        empids= []
        for record in allempecords:
            empids.append(record[0])
        if int(eid) in empids:
            messagebox.showerror("error","Employee id already exists!")
        elif len(ename) > 30 or len(ename) == 0:
            messagebox.showerror("error","Invalid Name!")
        elif len(email) > 30 or len(email) == 0 or "@" not in email:
            messagebox.showerror("error","Invalid Email!")
        elif len(econ) > 11 or len(econ) < 11 or len(econ) == 0 or econ.isdecimal() == False or "03" != econ[0:2]:
            messagebox.showerror("error","Invalid Number!")
        elif len(ed) == 0:
            messagebox.showerror("error","Invalid Date")
        elif len(edd) > 50 or len(edd) == 0:
            messagebox.showerror("error","Invalid Address Address !")
        elif len(esal) >8 or len(esal) == 0 or esal.isdecimal() == False:
            messagebox.showerror("error","Invalid Salary")
        else:
            for record in my_tree.get_children():
                my_tree.delete(record)
            query ="""INSERT INTO EMPLOYEE VALUES (:a,:b,:c,:d,:e,TO_DATE(:f,'YYYY-MM-DD'),:g)"""
            c.execute(query,a = eid, b=ename,c =email,d=int(econ),e=edd,f =ed,g = int(esal))
            c.execute("""commit""")
            c.execute("""Select max (EMPLOYEEID) from EMPLOYEE""")
            enextid = c.fetchall()
            enextid = enextid[0][0] + 1
            y.viewallemployee()
            y.clear_empentries()

    def deleteemployee(self):
        # grab record
        selected = my_tree.focus()
        # grad record values
        values = my_tree.item(selected, 'values')
        if len(values) == 0:
            messagebox.showerror("error","No employee selected!")
        else:
            try:
                c.execute("""DELETE FROM EMPLOYEE WHERE EMPLOYEEID = :a""",a =values[0])
                c.execute("""commit""")
                y.viewallemployee()
                y.clear_empentries()
            except:
                messagebox.showerror("error","selected Employee have some events")


    def updateemployee(self):
        eid =empid_entry.get()
        ename =ename_entry.get()
        email =eemail_entry.get()
        econ =econtact_entry.get()
        edd =eaddress_entry.get()
        ed =ehdate_entry.get()
        esal =esal_entry.get()
        if len(ename) > 30 or len(ename) == 0:
            messagebox.showerror("error","Invalid Name!")
        elif len(email) > 30 or len(email) == 0 or "@" not in email:
            messagebox.showerror("error","Invalid Email!")
        elif len(econ) > 11 or len(econ) < 11 or len(econ) == 0 or econ.isdecimal() == False or "03" != econ[0:2]:
            messagebox.showerror("error","Invalid Number!")
        elif len(ed) == 0:
            messagebox.showerror("error","Invalid Date")
        elif len(edd) > 50 or len(edd) == 0:
            messagebox.showerror("error","Invalid Address Address !")
        elif len(esal) >8 or len(esal) == 0 or esal.isdecimal() == False:
            messagebox.showerror("error","Invalid Salary")
        else:
            for record in my_tree.get_children():
                my_tree.delete(record)
            query ="""UPDATE EMPLOYEE SET EMPLOYEENAME=:b,EMPLOYEEEMAIL=:c,EMPLOYEECONTACT=:d,EMPLOYEEADDRESS=:e,EMPLOYEEHIREDATE = TO_DATE(:f,'YYYY-MM-DD'),EMPLOYEESALARY=:g WHERE EMPLOYEEID = :h"""
            c.execute(query,b=ename,c =email,d=int(econ),e=edd,f =ed,g = int(esal),h=eid)
            c.execute("""commit""")
            y.viewallemployee()
            y.clear_empentries()


    def addvenue(self):
        global vnextid
        vid = venueid_entry.get()
        vn =vname_entry.get()
        vd = vaddress_entry.get()
        vc =vcapacity_entry.get()
        vc =vcapacity_entry.get()
        vcon = vcontact_entry.get()
        vcost = vcost_entry.get()
        c.execute("SELECT * FROM VENUE")
        allvenuerecords = c.fetchall()
        venueids = []
        for record in allvenuerecords:
            venueids.append(record[0])
        if int(vid) in venueids:
            messagebox.showerror("error", "Venue id already exists!")
        elif len(vn) > 30 or len(vn) == 0:
            messagebox.showerror("error", "Invalid Name!")
        elif len(vd) > 50 or len(vd) == 0:
            messagebox.showerror("error", "Invalid Address!")
        elif len(vcon) > 11 or len(vcon) < 11 or len(vcon) == 0 or vcon.isdecimal() == False or "03" != vcon[0:2]:
            messagebox.showerror("error", "Invalid Number!")
        elif len(vc) > 4 or len(vc) == 0 or vc.isdecimal() == False:
            messagebox.showerror("error", "Invalid Capacity !")
        elif len(vcost) > 8 or len(vcost) == 0 or vcost.isdecimal() == False:
            messagebox.showerror("error", "Invalid Cost")
        # elif "fileloc" not in globals():
        #      messagebox.showerror("error","Select Images")
        else:

            for record in myv_tree.get_children():
                myv_tree.delete(record)
            # adding data
            query = """INSERT INTO VENUE VALUES (:a,:b,:c,:d,:e,:f)"""
            c.execute(query, a=int(vid), b=vn, c=vd, d=int(vc), e=int(vcon), f=int(vcost))
            c.execute("""commit""")
            c.execute("""Select max (VENUEID) from VENUE""")
            vnextid = c.fetchall()
            vnextid = vnextid[0][0] + 1
            y.viewallvenue()
            y.clear_venueentries()



    def deletevenue(self):
        # grab record
        global vnextid
        selected = myv_tree.focus()
        # grad record values
        values = myv_tree.item(selected, 'values')
        if len(values) == 0:
            messagebox.showerror("error", "No Venue selected!")
        else:
            try:
                c.execute("""DELETE FROM VENUE WHERE VENUEID = :a""", a=values[0])
                c.execute("""commit""")
                y.viewallvenue()
                y.clear_venueentries()
            except:
                messagebox.showerror("error", "selected Venue have some events")


    def updatevenue(self):
        vid = venueid_entry.get()
        vn = vname_entry.get()
        vd = vaddress_entry.get()
        vc = vcapacity_entry.get()
        vcon = vcontact_entry.get()
        vcost = vcost_entry.get()
        if len(vn) > 30 or len(vn) == 0:
            messagebox.showerror("error", "Invalid Name!")
        elif len(vd) > 50 or len(vd) == 0:
            messagebox.showerror("error", "Invalid Address!")
        elif len(vcon) > 11 or len(vcon) < 11 or len(vcon) == 0 or vcon.isdecimal() == False or "03" != vcon[0:2]:
            messagebox.showerror("error", "Invalid Number!")
        elif len(vc) > 4 or len(vc) == 0 or vc.isdecimal() == False:
            messagebox.showerror("error", "Invalid Capacity !")
        elif len(vcost) > 8 or len(vcost) == 0 or vcost.isdecimal() == False:
            messagebox.showerror("error", "Invalid Cost")
        else:
            for record in myv_tree.get_children():
                myv_tree.delete(record)
            query = """UPDATE VENUE SET VENUENAME=:b,VENUEADDRESS=:c,VENUECAPACITY=:d,VENUECONTACT=:e,VENUECOST=:f  WHERE VENUEID=:a"""
            c.execute(query, a=int(vid), b=vn, c=vd, d=int(vc), e=int(vcon), f=int(vcost))
            c.execute("""commit""")
            y.viewallvenue()
            y.clear_venueentries()

    def addfood(self):
        global fnextid
        fid = foodid_entry.get()
        fn =fname_entry.get()
        fp =funitprice_entry.get()
        fvid =f_v_ID_entry.get()
        c.execute("SELECT * FROM FOOD")
        allfoodrecords = c.fetchall()
        foodids = []
        for record in allfoodrecords:
            foodids.append(record[0])
        c.execute("SELECT * FROM VENDOR")
        allvendorrecords = c.fetchall()
        vendorids = []
        for record in allvendorrecords:
            vendorids.append(record[0])
        if int(fid) in foodids:
            messagebox.showerror("error", "Item id already exists!")
        elif len(fn) > 30 or len(fn) == 0:
            messagebox.showerror("error", "Invalid Name!")
        elif len(fp) > 8 or len(fp) == 0 or fp.isdecimal() == False:
            messagebox.showerror("error", "Invalid Cost!")
        elif len(fvid) == 0 or int(fvid) not in vendorids or fvid.isdecimal() == False:
            messagebox.showerror("error", "Vendor id not exists!")
        else:
            for record in myf_tree.get_children():
                myf_tree.delete(record)
            query = """INSERT INTO FOOD VALUES (:a,:b,:c,:d)"""
            c.execute(query,a = int(fid), b=fn, c=int(fp), d=int(fvid))
            c.execute("""commit""")
            c.execute("""Select max (ITEMID) from FOOD""")
            fnextid = c.fetchall()
            fnextid = fnextid[0][0] + 10
            y.viewallfood()
            y.clear_foodentries()

    def deletefood(self):
        selected = myf_tree.focus()
        # grad record values
        values = myf_tree.item(selected, 'values')
        if len(values) == 0:
            messagebox.showerror("error", "No Food selected!")
        else:
            try:
                c.execute("""DELETE FROM FOOD WHERE ITEMID = :a""", a=values[0])
                c.execute("""commit""")
                y.viewallfood()
                y.clear_foodentries()
            except:
                messagebox.showerror("error", "selected Item have some events")

    def updatefood(self):
        fid = foodid_entry.get()
        fn = fname_entry.get()
        fp = funitprice_entry.get()
        fvid = f_v_ID_entry.get()
        c.execute("SELECT * FROM VENDOR")
        allvendorrecords = c.fetchall()
        vendorids = []
        for record in allvendorrecords:
            vendorids.append(record[0])
        if len(fn) > 30 or len(fn) == 0:
            messagebox.showerror("error", "Invalid Name!")
        elif len(fp) > 8 or len(fp) == 0 or fp.isdecimal() == False:
            messagebox.showerror("error", "Invalid Cost!")
        elif len(fvid) == 0 or int(fvid) not in vendorids or  fvid.isdecimal() == False:
            messagebox.showerror("error", "Vendor id not exists!")
        else:
            for record in myf_tree.get_children():
                myf_tree.delete(record)
            query = """UPDATE FOOD SET ITEMNAME=:b,ITEMUNITCOST=:c,VENDORID=:d WHERE ITEMID=:a """
            c.execute(query, a=int(fid), b=fn, c=int(fp), d=int(fvid))
            c.execute("""commit""")
            y.viewallfood()
            y.clear_foodentries()

    def addvendor(self):
        global vendornextid
        vid = vendorid_entry.get()
        vn = vendorname_entry.get()
        vc = vendorcontact_entry.get()
        vd =vendoraddress_entry.get()
        c.execute("SELECT * FROM VENDOR")
        allvendorrecords = c.fetchall()
        vendorids = []
        for record in allvendorrecords:
            vendorids.append(record[0])
        if int(vid) in vendorids:
            messagebox.showerror("error", "Vendor id already exists!")
        elif len(vn) > 50 or len(vn) == 0:
            messagebox.showerror("error", "Invalid Name!")
        elif len(vc) > 11 or len(vc) < 11 or len(vc) == 0 or vc.isdecimal() == False or "03" != vc[0:2]:
            messagebox.showerror("error", "Invalid Contact!")
        elif len(vd)> 50 or len(vd) == 0:
            messagebox.showerror("error", "Invalid Address!")
        else:
            for record in myvendor_tree.get_children():
                myvendor_tree.delete(record)
            query = """INSERT INTO VENDOR VALUES (:a,:b,:c,:d)"""
            c.execute(query,a = int(vid), b=vn, c=int(vc), d=vd)
            c.execute("""commit""")
            c.execute("""Select max (VENDORID) from VENDOR""")
            vendornextid = c.fetchall()
            vendornextid = vendornextid[0][0] + 10
            y.viewallvendor()
            y.clear_vendorentries()

    def deletevendor(self):
        selected = myvendor_tree.focus()
        # grad record values
        values = myvendor_tree.item(selected, 'values')
        if len(values) == 0:
            messagebox.showerror("error", "No Vendor selected!")
        else:
            try:
                c.execute("""DELETE FROM VENDOR WHERE VENDORID = :a""", a=values[0])
                c.execute("""commit""")
                y.viewallvendor()
                y.clear_vendorentries()
            except:
                messagebox.showerror("error", "selected Vendor have some food in events")

    def updatevendor(self):
        vid = vendorid_entry.get()
        vn = vendorname_entry.get()
        vc = vendorcontact_entry.get()
        vd = vendoraddress_entry.get()
        if len(vn) > 30 or len(vn) == 0:
            messagebox.showerror("error", "Invalid Name!")
        elif len(vc) > 11 or len(vc) < 11 or len(vc) == 0 or vc.isdecimal() == False or "03" != vc[0:2]:
            messagebox.showerror("error", "Invalid Contact!")
        elif len(vd) > 50 or len(vd) == 0:
            messagebox.showerror("error", "Invalid Address!")
        else:
            for record in myvendor_tree.get_children():
                myvendor_tree.delete(record)
            query = """UPDATE VENDOR SET VENDORNAME=:b,VENDORCONTACT=:c,VENDORADDRESS=:d WHERE VENDORID =:a"""
            c.execute(query, a=int(vid), b=vn, c=int(vc), d=vd)
            c.execute("""commit""")
            y.viewallvendor()
            y.clear_vendorentries()

    def adddecoration(self):
        global decnextid
        did = decid_entry.get()
        dt = dectype_entry.get()
        dc = deccost_entry.get()
        c.execute("SELECT * FROM DECORATION")
        alldecrecords = c.fetchall()
        decids = []
        for record in alldecrecords:
            decids.append(record[0])
        if int(did) in decids:
            messagebox.showerror("error", "Decoration id already exists!")
        elif len(dt) > 30 or len(dt) == 0:
            messagebox.showerror("error", "Invalid Decoration Tyoe!")
        elif len(dc)> 8 or len(dc) == 0 or dc.isdecimal() == False:
            messagebox.showerror("error", "Invalid Cost!")
        else:
            for record in mydec_tree.get_children():
                mydec_tree.delete(record)
            query = """INSERT INTO DECORATION VALUES (:a,:b,:c)"""
            c.execute(query,a = int(did), b=dt, c=int(dc))
            c.execute("""commit""")
            c.execute("""Select max (DECORATIONID) from DECORATION""")
            decnextid = c.fetchall()
            decnextid = decnextid[0][0] + 10
            y.viewalldec()
            y.clear_decentries()

    def deletedecoration(self):
        selected = mydec_tree.focus()
        # grad record values
        values = mydec_tree.item(selected, 'values')
        if len(values) == 0:
            messagebox.showerror("error", "No Decoration selected!")
        else:
            try:
                c.execute("""DELETE FROM DECORATION WHERE DECORATIONID = :a""", a=values[0])
                c.execute("""commit""")
                y.viewalldec()
                y.clear_decentries()
            except:
                messagebox.showerror("error", "selected Decoration have some events")

    def updatedecoration(self):
        did = decid_entry.get()
        dt = dectype_entry.get()
        dc = deccost_entry.get()
        if len(dt) > 30 or len(dt) == 0:
            messagebox.showerror("error", "Invalid Decoration Tyoe!")
        elif len(dc) > 8 or len(dc) == 0 or dc.isdecimal() == False:
            messagebox.showerror("error", "Invalid Cost!")
        else:
            for record in mydec_tree.get_children():
                mydec_tree.delete(record)
            query = """UPDATE DECORATION SET DECORATIONTYPE= :b,DECORATIONCOST=:c WHERE DECORATIONID=:a"""
            c.execute(query, a=int(did), b=dt, c=int(dc))
            c.execute("""commit""")
            y.viewalldec()
            y.clear_decentries()

    def addservices(self):
        global sernextid
        sid = serid_entry.get()
        sn = sername_entry.get()
        sc =sercost_entry.get()
        c.execute("SELECT * FROM SERVICE")
        allserrecords = c.fetchall()
        serids = []
        for record in allserrecords:
            serids.append(record[0])
        if len(sid) == 0 or int(sid) in serids:
            messagebox.showerror("error", "Service id already exists!")
        elif len(sn) > 30 or len(sn) == 0:
            messagebox.showerror("error", "Invalid Service Name!")
        elif len(sc)> 8 or len(sc) == 0 or sc.isdecimal() == False:
            messagebox.showerror("error", "Invalid Cost!")
        else:
            for record in myser_tree.get_children():
                myser_tree.delete(record)
            query = """INSERT INTO SERVICE VALUES (:a,:b,:c)"""
            c.execute(query,a = int(sid), b=sn, c=int(sc))
            c.execute("""commit""")
            c.execute("""Select max (SERVICEID) from SERVICE""")
            sernextid = c.fetchall()
            sernextid = sernextid[0][0] + 10
            y.viewallser()
            y.clear_serentries()

    def deleteservices(self):
        selected = myser_tree.focus()
        # grad record values
        values = myser_tree.item(selected, 'values')
        if len(values) == 0:
            messagebox.showerror("error", "No Service selected!")
        else:
            try:
                c.execute("""DELETE FROM SERVICE WHERE SERVICEID = :a""", a=values[0])
                c.execute("""commit""")
                y.viewallser()
                y.clear_serentries()
            except:
                messagebox.showerror("error", "selected Service have some events")

    def updateservices(self):
        sid = serid_entry.get()
        sn = sername_entry.get()
        sc = sercost_entry.get()
        if len(sn) > 30 or len(sn) == 0:
            messagebox.showerror("error", "Invalid Service Name!")
        elif len(sc) > 8 or len(sc) == 0 or sc.isdecimal() == False:
            messagebox.showerror("error", "Invalid Cost!")
        else:
            for record in myser_tree.get_children():
                myser_tree.delete(record)
            query = """UPDATE SERVICE SET SERVICENAME=:b,SERVICECOST=:c WHERE SERVICEID=:a"""
            c.execute(query, a=int(sid), b=sn, c=int(sc))
            c.execute("""commit""")
            y.viewallser()
            y.clear_serentries()




    def home(self):
        y.clear_frame()
        parent_frame.configure(background="white")

        # DATABASE
        c.execute("""SELECT COUNT(EMPLOYEEID) FROM EMPLOYEE""")
        totalemployee = c.fetchall()

        c.execute("""SELECT COUNT(EVENTID) FROM EVENT""")
        totalevents = c.fetchall()

        c.execute("""SELECT COUNT(EVENTID) FROM EVENT WHERE EVENTDATE = SYSDATE""")
        todayevent = c.fetchall()

        c.execute("""SELECT COUNT(EVENTID) FROM EVENT WHERE EVENTDATE > SYSDATE""")
        upcomming = c.fetchall()

        frame1 = Frame(parent_frame, background="#3a7ebf", width='130px', height='130px',
                       cursor="hand2", relief='sunken')
        frame1.place(relx=0.125, rely=0.10)

        label1 = Label(frame1, text="No of Employees", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 15")
        label1.place(relx=0.07, rely=0.16)
        if (totalemployee[0][0]) < 9:
            totalemployee = '0' + str(totalemployee[0][0])
        label2 = Label(frame1, text=totalemployee, justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 40")
        label2.place(relx=0.30, rely=0.38)

        frame2 = Frame(parent_frame, background="#3a7ebf", width='130px', height='130px',
                       cursor="hand2", relief='sunken')
        frame2.place(relx=0.325, rely=0.10)
        label1 = Label(frame2, text="Total Events", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 15")
        label1.place(relx=0.16, rely=0.16)
        if (totalevents[0][0]) < 9:
            totalevents = '0' + str(totalevents[0][0])
        label2 = Label(frame2, text=totalevents, justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 40")
        label2.place(relx=0.33, rely=0.38)

        frame3 = Frame(parent_frame, background="#3a7ebf", width='130px', height='130px',
                       cursor="hand2", relief='sunken')
        frame3.place(relx=0.525, rely=0.10)
        label1 = Label(frame3, text="Today's Events", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 15")
        label1.place(relx=0.08, rely=0.16)
        if (todayevent[0][0]) < 9:
            todayevent = '0' + str(todayevent[0][0])
        label2 = Label(frame3, text=todayevent, justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 40")
        label2.place(relx=0.30, rely=0.38)

        frame4 = Frame(parent_frame, background="#3a7ebf", width='130px', height='130px',
                       cursor="hand2", relief='sunken')
        frame4.place(relx=0.725, rely=0.10)
        label1 = Label(frame4, text="Upcomming Events", justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 14")
        label1.place(relx=0.025, rely=0.16)
        if (upcomming[0][0]) < 9:
            upcomming = '0' + str(upcomming[0][0])
        label2 = Label(frame4, text=upcomming, justify="center", bg="#3a7ebf", fg="white",
                       font="-family {Prototype} -size 40")
        label2.place(relx=0.30, rely=0.38)

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
                        fieldbackground="white")
        style.configure("Treeview.Heading", background="#044c92", foreground="white",
                        font="-family {Prototype} -size 12")
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
        c.execute("SELECT * FROM Event ORDER BY EVENTDATE DESC")
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
                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                               tags=('oddrow',))
            count += 1


    def registeremployee(self):
        global s_entry,my_tree,s_var,empid_entry,ename_entry,eemail_entry,econtact_entry, eaddress_entry,ehdate_entry,esal_entry,enextid
        y.clear_frame()
        parent_frame.configure(background="white")

        record_frame = LabelFrame(parent_frame, text="Records", width=1250, height=200,
                                font="-family {Prototype} -size 15",
                                fg="#044c92", bg="white", bd=2, relief='groove')
        record_frame.place(relx=0.05, rely=0.05)


        etree_frame = LabelFrame(parent_frame,text="Employee Detail", width =1300, height = 350,font = "-family {Prototype} -size 15",
                                fg ="#044c92",bg="white",bd=2,relief='groove')
        etree_frame.place(relx=0.05,rely =0.35)
        s_var = IntVar()
        id_r = Radiobutton(etree_frame, text="ID", variable=s_var, value=0,bg='white',font = "-family {Prototype} -size 12")
        id_r.place(relx=0.01,rely=0.02)
        name_r = Radiobutton(etree_frame, text="Name", variable=s_var, value=1, bg='white',font = "-family {Prototype} -size 12")
        name_r.place(relx=0.08,rely=0.02)
        s_entry = Entry(etree_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        s_entry.place(relx=0.175,rely=0.02)
        s_entry.bind("<KeyRelease>",y.checkentry)
        # c.execute("""Select EMPLOYEE_Employee_ID.nextval from dual""")
        # enextid = c.fetchall()
        empid_lable = Label(record_frame, text="ID",font = "-family {Prototype} -size 12",bg="white")
        empid_lable.grid(row=0, column=0, padx=10, pady=10)
        empid_entry = Entry(record_frame,font = "-family {Prototype} -size 12",relief='solid',bd=1)
        empid_entry.grid(row=0, column=1, padx=10, pady=10)
        c.execute("""Select max (EMPLOYEEID) from EMPLOYEE""")
        enextid = c.fetchall()
        enextid = enextid[0][0] + 1
        empid_entry.insert(0,enextid)
        empid_entry.config(state='readonly')

        ename_lable = Label(record_frame, text="Name",font = "-family {Prototype} -size 12",bg='white')
        ename_lable.grid(row=0, column=2, padx=10, pady=10)
        ename_entry = Entry(record_frame,font = "-family {Prototype} -size 12",relief='solid',bd=1)
        ename_entry.grid(row=0, column=3, padx=10, pady=10)

        eemail_lable = Label(record_frame, text="Email", font="-family {Prototype} -size 12", bg='white')
        eemail_lable.grid(row=0, column=4, padx=10, pady=10)
        eemail_entry = Entry(record_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        eemail_entry.grid(row=0, column=5, padx=10, pady=10)

        econtact_lable = Label(record_frame, text="Contact", font="-family {Prototype} -size 12", bg='white')
        econtact_lable.grid(row=0, column=6, padx=10, pady=10)
        econtact_entry = Entry(record_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        econtact_entry.grid(row=0, column=7, padx=10, pady=10)

        eaddress_lable = Label(record_frame, text="Address", font="-family {Prototype} -size 12", bg='white')
        eaddress_lable.grid(row=1, column=0, padx=10, pady=10)
        eaddress_entry = Entry(record_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        eaddress_entry.grid(row=1, column=1, padx=10, pady=10)

        ehdate_lable = Label(record_frame, text="Hire-Date", font="-family {Prototype} -size 12", bg='white')
        ehdate_lable.grid(row=1, column=2, padx=10, pady=10)
        ehdate_entry = DateEntry(record_frame,width =19,bd=1,
                        background='#044c92', foreground='white', borderwidth=1, font="-family {Prototype} -size 12",
                        headersbackground="#3a7ebf",
                        headersforeground="white", selectbackground="#044c92", selectforeground="white",
                        normalbackground="white",
                        normalforeground="black", weekendbackground="white", weekendforeground="black",
                        othermonthforeground="black", othermonthbackground="white", othermonthweforeground="black",
                        othermonthwebackground="white",date_pattern = "YYYY-MM-DD")
        # 3a7ebf
        ehdate_entry.grid(row=1, column=3, padx=10, pady=10)

        esal_lable = Label(record_frame, text="Salary", font="-family {Prototype} -size 12", bg='white')
        esal_lable.grid(row=1, column=4, padx=10, pady=10)
        esal_entry = Entry(record_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        esal_entry.grid(row=1, column=5, padx=10, pady=10)

        clr_btn = tk.Button(parent_frame, text="CLEAR", height=0, width=15, foreground='white',
                            font="-family {Prototype} -size 12",command = y.clear_empentries)
        clr_btn.configure(relief='flat')
        clr_btn.configure(background="#044c92")
        clr_btn.configure(borderwidth="0px")
        clr_btn.configure(cursor="hand2")
        clr_btn.configure(relief='flat')
        clr_btn.place(relx=0.625,rely= 0.27)

        add_btn = tk.Button(parent_frame,text= "ADD",height=0,width=15,foreground='white',font="-family {Prototype} -size 12",command = y.addemployee)
        add_btn.configure(relief='flat')
        add_btn.configure(background="#044c92")
        add_btn.configure(borderwidth="0px")
        add_btn.configure(cursor="hand2")
        add_btn.configure(relief='flat')
        add_btn.place(relx=0.25,rely=0.27)

        update_btn = tk.Button(parent_frame, text="UPDATE", height=0, width=15, foreground='white',
                            font="-family {Prototype} -size 12",command = y.updateemployee)
        update_btn.configure(relief='flat')
        update_btn.configure(background="#044c92")
        update_btn.configure(borderwidth="0px")
        update_btn.configure(cursor="hand2")
        update_btn.place(relx=0.375,rely=0.27)

        delete_btn = tk.Button(parent_frame, text="DELETE", height=0, width=15, foreground='white',
                               font="-family {Prototype} -size 12",command = y.deleteemployee)
        delete_btn.configure(background="#044c92")
        delete_btn.configure(borderwidth="0px")
        delete_btn.configure(cursor="hand2")
        delete_btn.configure(relief='flat')
        delete_btn.place(relx=0.5,rely=0.27)

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
        style.configure("Treeview.Heading", background="#044c92", foreground="white",font="-family {Prototype} -size 12")
        # change selected color
        style.map('Treeview',
                  background=[('selected', '#044c92')])

        # crate treview frame
        tree_frame = Frame(etree_frame,width=1250,height=300)
        tree_frame.configure(background="black")
        tree_frame.pack(pady=(50,0))

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
        my_tree['columns'] = ("EMPLOYEEID", "EMPLOYEENAME", "EMPLOYEEEMAIL", "EMPLOYEECONTACT", "EMPLOYEEADDRESS", "EMPLOYEEHIREDATE", "EMPLOYEESALARY")

        # format our coloums
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("EMPLOYEEID", anchor=CENTER, width=180)
        my_tree.column("EMPLOYEENAME", anchor=CENTER, width=180)
        my_tree.column("EMPLOYEEEMAIL", anchor=CENTER, width=180)
        my_tree.column("EMPLOYEECONTACT", anchor=CENTER, width=180)
        my_tree.column("EMPLOYEEADDRESS", anchor=CENTER, width=180)
        my_tree.column("EMPLOYEEHIREDATE", anchor=CENTER, width=180)
        my_tree.column("EMPLOYEESALARY", anchor=CENTER, width=180)

        # define heading
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("EMPLOYEEID", text="EMPLOYEE ID", anchor=CENTER)
        my_tree.heading("EMPLOYEENAME", text="EMPLOYEE NAME", anchor=CENTER)
        my_tree.heading("EMPLOYEEEMAIL", text="EMPLOYEE EMAIL", anchor=CENTER)
        my_tree.heading("EMPLOYEEADDRESS", text="EMPLOYEE ADDRESS", anchor=CENTER)
        my_tree.heading("EMPLOYEECONTACT", text="EMPLOYEE CONTACT", anchor=CENTER)
        my_tree.heading("EMPLOYEEHIREDATE", text="EMPLOYEE HIREDATE", anchor=CENTER)
        my_tree.heading("EMPLOYEESALARY", text="EMPLOYEE SALARY", anchor=CENTER)


        # create stripped row tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#87cdee")

        #data
        y.viewallemployee()

        #bind selected record
        my_tree.bind("<ButtonRelease-1>",y.empselect_record)



    def venue(self):
        global sv_entry, myv_tree, sv_var, venueid_entry, vname_entry, vaddress_entry, vcontact_entry, vcost_entry,vcapacity_entry ,vnextid
        y.clear_frame()
        parent_frame.configure(background="white")

        vrecord_frame = LabelFrame(parent_frame, text="Records", width=1250, height=200,
                                  font="-family {Prototype} -size 15",
                                  fg="#044c92", bg="white", bd=2, relief='groove')
        vrecord_frame.place(relx=0.05, rely=0.05)

        vtree_frame = LabelFrame(parent_frame, text="Venue Detail", width=1300, height=350,
                                 font="-family {Prototype} -size 15",
                                 fg="#044c92", bg="white", bd=2, relief='groove')
        vtree_frame.place(relx=0.05, rely=0.35)

        sv_var = IntVar()
        idv_r = Radiobutton(vtree_frame, text="ID", variable=sv_var, value=0, bg='white',
                           font="-family {Prototype} -size 12")
        idv_r.place(relx=0.01, rely=0.02)
        namev_r = Radiobutton(vtree_frame, text="Name", variable=sv_var, value=1, bg='white',
                             font="-family {Prototype} -size 12")
        namev_r.place(relx=0.08, rely=0.02)
        sv_entry = Entry(vtree_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        sv_entry.place(relx=0.175, rely=0.02)
        sv_entry.bind("<KeyRelease>", y.checkentryvenue)

        venueid_lable = Label(vrecord_frame, text="ID", font="-family {Prototype} -size 12", bg="white")
        venueid_lable.grid(row=0, column=0, padx=10, pady=10)
        venueid_entry = Entry(vrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        venueid_entry.grid(row=0, column=1, padx=10, pady=10)
        c.execute("""Select max (VENUEID) from VENUE""")
        vnextid = c.fetchall()
        vnextid = vnextid[0][0] + 1
        venueid_entry.insert(0, vnextid)
        venueid_entry.config(state='readonly')

        vname_lable = Label(vrecord_frame, text="Name", font="-family {Prototype} -size 12", bg='white')
        vname_lable.grid(row=0, column=2, padx=10, pady=10)
        vname_entry = Entry(vrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vname_entry.grid(row=0, column=3, padx=10, pady=10)

        vaddress_lable = Label(vrecord_frame, text="Address", font="-family {Prototype} -size 12", bg='white')
        vaddress_lable.grid(row=0, column=4, padx=10, pady=10)
        vaddress_entry = Entry(vrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vaddress_entry.grid(row=0, column=5, padx=10, pady=10)

        vcapacity_lable = Label(vrecord_frame, text="Capacity", font="-family {Prototype} -size 12", bg='white')
        vcapacity_lable.grid(row=0, column=6, padx=10, pady=10)
        vcapacity_entry = Entry(vrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vcapacity_entry.grid(row=0, column=7, padx=10, pady=10)

        vcontact_lable = Label(vrecord_frame, text="Contact", font="-family {Prototype} -size 12", bg='white')
        vcontact_lable.grid(row=1, column=0, padx=10, pady=10)
        vcontact_entry = Entry(vrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vcontact_entry.grid(row=1, column=1, padx=10, pady=10)


        vcost_lable = Label(vrecord_frame, text="Cost", font="-family {Prototype} -size 12", bg='white')
        vcost_lable.grid(row=1, column=2, padx=10, pady=10)
        vcost_entry = Entry(vrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vcost_entry.grid(row=1, column=3, padx=10, pady=10)

        # browse_lable = Label(vrecord_frame, text="Images", font="-family {Prototype} -size 12", bg='white')
        # browse_lable.grid(row=1, column=4, padx=10, pady=10)
        # br_btn = tk.Button(vrecord_frame, text="Browse", height=0, width=22, foreground='white',
        #                     font="-family {Prototype} -size 12", command=y.browsefile)
        # br_btn.configure(relief='flat')
        # br_btn.configure(background="#044c92")
        # br_btn.configure(borderwidth="0px")
        # br_btn.configure(cursor="hand2")
        # br_btn.configure(relief='flat')
        # br_btn.grid(row=1,column=5, padx = 10, pady=10)


        clr_btn = tk.Button(parent_frame, text="CLEAR", height=0, width=15, foreground='white',
                            font="-family {Prototype} -size 12", command=y.clear_venueentries)
        clr_btn.configure(relief='flat')
        clr_btn.configure(background="#044c92")
        clr_btn.configure(borderwidth="0px")
        clr_btn.configure(cursor="hand2")
        clr_btn.configure(relief='flat')
        clr_btn.place(relx=0.625, rely=0.27)

        add_btn = tk.Button(parent_frame, text="ADD", height=0, width=15, foreground='white',
                            font="-family {Prototype} -size 12", command=y.addvenue)
        add_btn.configure(relief='flat')
        add_btn.configure(background="#044c92")
        add_btn.configure(borderwidth="0px")
        add_btn.configure(cursor="hand2")
        add_btn.configure(relief='flat')
        add_btn.place(relx=0.25, rely=0.27)

        update_btn = tk.Button(parent_frame, text="UPDATE", height=0, width=15, foreground='white',
                               font="-family {Prototype} -size 12", command=y.updatevenue)
        update_btn.configure(relief='flat')
        update_btn.configure(background="#044c92")
        update_btn.configure(borderwidth="0px")
        update_btn.configure(cursor="hand2")
        update_btn.place(relx=0.375, rely=0.27)

        delete_btn = tk.Button(parent_frame, text="DELETE", height=0, width=15, foreground='white',
                               font="-family {Prototype} -size 12", command=y.deletevenue)
        delete_btn.configure(background="#044c92")
        delete_btn.configure(borderwidth="0px")
        delete_btn.configure(cursor="hand2")
        delete_btn.configure(relief='flat')
        delete_btn.place(relx=0.5, rely=0.27)

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
        tree_frame = Frame(vtree_frame, width=1250, height=300)
        tree_frame.configure(background="black")
        tree_frame.pack(pady=(50, 0))

        # treescrolly
        tree_scrolly = Scrollbar(tree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(tree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        myv_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                               selectmode="extended")
        myv_tree.pack()

        # configure scroll bar
        tree_scrolly.config(command=myv_tree.yview)
        tree_scrollx.config(command=myv_tree.xview)

        # define coloums
        myv_tree['columns'] = (
        "VENUEID", "VENUENAME", "VENUEADDRESS", "VENUECAPACITY", "VENUECONTACT", "VENUECOST")

        # format our coloums
        myv_tree.column("#0", width=0, stretch=NO)
        myv_tree.column("VENUEID", anchor=CENTER, width=180)
        myv_tree.column("VENUENAME", anchor=CENTER, width=200)
        myv_tree.column("VENUEADDRESS", anchor=CENTER, width=260)
        myv_tree.column("VENUECAPACITY", anchor=CENTER, width=180)
        myv_tree.column("VENUECONTACT", anchor=CENTER, width=180)
        myv_tree.column("VENUECOST", anchor=CENTER, width=180)

        # define heading
        myv_tree.heading("#0", text="", anchor=W)
        myv_tree.heading("VENUEID", text="VENUE ID", anchor=CENTER)
        myv_tree.heading("VENUENAME", text="VENUE NAME", anchor=CENTER)
        myv_tree.heading("VENUEADDRESS", text="VENUE ADDRESS", anchor=CENTER)
        myv_tree.heading("VENUECAPACITY", text="VENUE CAPACITY", anchor=CENTER)
        myv_tree.heading("VENUECONTACT", text="VENUE CONTACT", anchor=CENTER)
        myv_tree.heading("VENUECOST", text="VENUE COST", anchor=CENTER)

        # create stripped row tags
        myv_tree.tag_configure('oddrow', background="white")
        myv_tree.tag_configure('evenrow', background="#87cdee")

        # data
        y.viewallvenue()

        # bind selected record
        myv_tree.bind("<ButtonRelease-1>", y.vselect_record)

    def food(self):
        global fnextid, sf_entry, myf_tree, sf_var, foodid_entry, fname_entry, funitprice_entry, f_v_ID_entry
        y.clear_frame()
        parent_frame.configure(background="white")

        frecord_frame = LabelFrame(parent_frame, text="Records", width=1250, height=200,
                                   font="-family {Prototype} -size 15",
                                   fg="#044c92", bg="white", bd=2, relief='groove')
        frecord_frame.place(relx=0.02, rely=0.05)

        ftree_frame = LabelFrame(parent_frame, text="Food Detail", width=1300, height=150,
                                 font="-family {Prototype} -size 15",
                                 fg="#044c92", bg="white", bd=2, relief='groove')
        ftree_frame.place(relx=0.02, rely=0.35)
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

        foodid_lable = Label(frecord_frame, text="Item ID", font="-family {Prototype} -size 12", bg="white")
        foodid_lable.grid(row=0, column=0, padx=10, pady=10)
        foodid_entry = Entry(frecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        foodid_entry.grid(row=0, column=1, padx=10, pady=10)
        c.execute("SELECT MAX(ITEMID) FROM FOOD")
        fnextid = c.fetchall()
        fnextid = fnextid[0][0] + 10
        foodid_entry.insert(0, fnextid)
        foodid_entry.config(state='readonly')

        fname_lable = Label(frecord_frame, text="Item Name", font="-family {Prototype} -size 12", bg='white')
        fname_lable.grid(row=0, column=2, padx=10, pady=10)
        fname_entry = Entry(frecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        fname_entry.grid(row=0, column=3, padx=10, pady=10)


        funitprice_lable = Label(frecord_frame, text="Unit Cost", font="-family {Prototype} -size 12", bg='white')
        funitprice_lable.grid(row=1, column=0, padx=10, pady=10)
        funitprice_entry = Entry(frecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        funitprice_entry.grid(row=1, column=1, padx=10, pady=10)

        f_v_ID_lable = Label(frecord_frame, text="Vendor ID", font="-family {Prototype} -size 12", bg='white')
        f_v_ID_lable.grid(row=1, column=2, padx=10, pady=10)
        c.execute("""SELECT VENDORID FROM VENDOR""")
        row = c.fetchall()
        vendor_list = []
        for i in row:
            vendor_list.append(i[0])
        e_type = StringVar()
        f_v_ID_entry = ttk.Combobox(frecord_frame, textvariable=e_type, font="-family {Prototype} -size 12")
        f_v_ID_entry['values'] = vendor_list
        f_v_ID_entry.grid(row=1, column=3, padx=10, pady=10)
        f_v_ID_entry.bind("<<ComboboxSelected>>")


        # f_v_ID_entry = Entry(frecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        # f_v_ID_entry.grid(row=1, column=3, padx=10, pady=10)

        clr_btn = tk.Button(parent_frame, text="CLEAR", height=0, width=12, foreground='white',
                            font="-family {Prototype} -size 12", command=y.clear_foodentries)
        clr_btn.configure(relief='flat')
        clr_btn.configure(background="#044c92")
        clr_btn.configure(borderwidth="0px")
        clr_btn.configure(cursor="hand2")
        clr_btn.configure(relief='flat')
        clr_btn.place(relx=0.36, rely=0.27)

        add_btn = tk.Button(parent_frame, text="ADD", height=0, width=12, foreground='white',
                            font="-family {Prototype} -size 12", command=y.addfood)
        add_btn.configure(relief='flat')
        add_btn.configure(background="#044c92")
        add_btn.configure(borderwidth="0px")
        add_btn.configure(cursor="hand2")
        add_btn.configure(relief='flat')
        add_btn.place(relx=0.06, rely=0.27)

        update_btn = tk.Button(parent_frame, text="UPDATE", height=0, width=12, foreground='white',
                               font="-family {Prototype} -size 12", command=y.updatefood)
        update_btn.configure(relief='flat')
        update_btn.configure(background="#044c92")
        update_btn.configure(borderwidth="0px")
        update_btn.configure(cursor="hand2")
        update_btn.place(relx=0.16, rely=0.27)

        delete_btn = tk.Button(parent_frame, text="DELETE", height=0, width=12, foreground='white',
                               font="-family {Prototype} -size 12", command=y.deletefood)
        delete_btn.configure(background="#044c92")
        delete_btn.configure(borderwidth="0px")
        delete_btn.configure(cursor="hand2")
        delete_btn.configure(relief='flat')
        delete_btn.place(relx=0.26, rely=0.27)

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
        tree_frame = Frame(ftree_frame, width=1250, height=300)
        tree_frame.configure(background="black")
        tree_frame.pack(pady=(50, 0))

        # treescrolly
        tree_scrolly = Scrollbar(tree_frame)
        tree_scrolly.pack(side=RIGHT, fill=Y)

        # treescrolly
        tree_scrollx = Scrollbar(tree_frame, orient='horizontal')
        tree_scrollx.pack(side=BOTTOM, fill=X)

        # create tree view
        myf_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                                selectmode="extended")
        myf_tree.pack(fill = BOTH, expand = 1)

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

        # bind selected record
        myf_tree.bind("<ButtonRelease-1>", y.fselect_record)
        # ------------------VENDOR-------------------------
        global vendornextid,svendor_entry, myvendor_tree, svendor_var, vendorid_entry, vendorname_entry, vendorcontact_entry, vendoraddress_entry

        vendorrecord_frame = LabelFrame(parent_frame, text="Records", width=1250, height=200,
                                        font="-family {Prototype} -size 15",
                                        fg="#044c92", bg="white", bd=2, relief='groove')
        vendorrecord_frame.place(relx=0.5, rely=0.05)

        vendortree_frame = LabelFrame(parent_frame, text="Vendor Detail", width=1300, height=150,
                                      font="-family {Prototype} -size 15",
                                      fg="#044c92", bg="white", bd=2, relief='groove')
        vendortree_frame.place(relx=0.51, rely=0.35)
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

        vendorid_lable = Label(vendorrecord_frame, text="Vendor ID", font="-family {Prototype} -size 12", bg="white")
        vendorid_lable.grid(row=0, column=0, padx=10, pady=10)
        vendorid_entry = Entry(vendorrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vendorid_entry.grid(row=0, column=1, padx=10, pady=10)
        c.execute("SELECT MAX(VENDORID) FROM VENDOR")
        vendornextid = c.fetchall()
        vendornextid = vendornextid[0][0] + 10
        vendorid_entry.insert(0, vendornextid)
        vendorid_entry.config(state='readonly')

        vendorname_lable = Label(vendorrecord_frame, text="Vendor Name", font="-family {Prototype} -size 12",
                                 bg='white')
        vendorname_lable.grid(row=0, column=2, padx=10, pady=10)
        vendorname_entry = Entry(vendorrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vendorname_entry.grid(row=0, column=3, padx=10, pady=10)

        vendorcontact_lable = Label(vendorrecord_frame, text="Contact", font="-family {Prototype} -size 12", bg='white')
        vendorcontact_lable.grid(row=1, column=0, padx=10, pady=10)
        vendorcontact_entry = Entry(vendorrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vendorcontact_entry.grid(row=1, column=1, padx=10, pady=10)

        vendoraddress_lable = Label(vendorrecord_frame, text="Address", font="-family {Prototype} -size 12", bg='white')
        vendoraddress_lable.grid(row=1, column=2, padx=10, pady=10)
        vendoraddress_entry = Entry(vendorrecord_frame, font="-family {Prototype} -size 12", relief='solid', bd=1)
        vendoraddress_entry.grid(row=1, column=3, padx=10, pady=10)

        clr_btn = tk.Button(parent_frame, text="CLEAR", height=0, width=12, foreground='white',
                            font="-family {Prototype} -size 12", command=y.clear_vendorentries)
        clr_btn.configure(relief='flat')
        clr_btn.configure(background="#044c92")
        clr_btn.configure(borderwidth="0px")
        clr_btn.configure(cursor="hand2")
        clr_btn.configure(relief='flat')
        clr_btn.place(relx=0.86, rely=0.27)

        add_btn = tk.Button(parent_frame, text="ADD", height=0, width=12, foreground='white',
                            font="-family {Prototype} -size 12", command=y.addvendor)
        add_btn.configure(relief='flat')
        add_btn.configure(background="#044c92")
        add_btn.configure(borderwidth="0px")
        add_btn.configure(cursor="hand2")
        add_btn.configure(relief='flat')
        add_btn.place(relx=0.56, rely=0.27)

        update_btn = tk.Button(parent_frame, text="UPDATE", height=0, width=12, foreground='white',
                               font="-family {Prototype} -size 12", command=y.updatevendor)
        update_btn.configure(relief='flat')
        update_btn.configure(background="#044c92")
        update_btn.configure(borderwidth="0px")
        update_btn.configure(cursor="hand2")
        update_btn.place(relx=0.66, rely=0.27)

        delete_btn = tk.Button(parent_frame, text="DELETE", height=0, width=12, foreground='white',
                               font="-family {Prototype} -size 12", command=y.deletevendor)
        delete_btn.configure(background="#044c92")
        delete_btn.configure(borderwidth="0px")
        delete_btn.configure(cursor="hand2")
        delete_btn.configure(relief='flat')
        delete_btn.place(relx=0.76, rely=0.27)

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
        vtree_frame.pack(pady=(50, 0))

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

        # bind selected record
        myvendor_tree.bind("<ButtonRelease-1>", y.vendorselect_record)



    def services(self):
        y.clear_frame()
        parent_frame.configure(background="white")
        global decnextid, sdec_entry, mydec_tree, sdec_var, decid_entry, dectype_entry, deccost_entry
        y.clear_frame()
        parent_frame.configure(background="white")

        decrecord_frame = LabelFrame(parent_frame, text="Records", width=900, height=200,
                                     font="-family {Prototype} -size 15",
                                     fg="#044c92", bg="white", bd=2, relief='groove')
        decrecord_frame.place(relx=0.02, rely=0.05)

        dectree_frame = LabelFrame(parent_frame, text="Decoration Detail", width=1300, height=150,
                                   font="-family {Prototype} -size 15",
                                   fg="#044c92", bg="white", bd=2, relief='groove')
        dectree_frame.place(relx=0.02, rely=0.35)
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

        decid_lable = Label(decrecord_frame, text="Decoration ID", font="-family {Prototype} -size 11", bg="white")
        decid_lable.grid(row=0, column=0, padx=10, pady=10)
        decid_entry = Entry(decrecord_frame, font="-family {Prototype} -size 11", relief='solid', bd=1)
        decid_entry.grid(row=0, column=1, padx=10, pady=10)
        c.execute("SELECT MAX(DECORATIONID) FROM DECORATION")
        decnextid = c.fetchall()
        decnextid = decnextid[0][0] + 10
        decid_entry.insert(0, decnextid)
        decid_entry.config(state='readonly')

        dectype_lable = Label(decrecord_frame, text="Decoration type", font="-family {Prototype} -size 11", bg='white')
        dectype_lable.grid(row=0, column=2, padx=10, pady=10)
        dectype_entry = Entry(decrecord_frame, font="-family {Prototype} -size 11", relief='solid', bd=1)
        dectype_entry.grid(row=0, column=3, padx=10, pady=10)

        deccost_lable = Label(decrecord_frame, text="Unit Cost", font="-family {Prototype} -size 11", bg='white')
        deccost_lable.grid(row=1, column=0, padx=10, pady=10)
        deccost_entry = Entry(decrecord_frame, font="-family {Prototype} -size 11", relief='solid', bd=1)
        deccost_entry.grid(row=1, column=1, padx=10, pady=10)

        clr_btn = tk.Button(parent_frame, text="CLEAR", height=0, width=12, foreground='white',
                            font="-family {Prototype} -size 12", command=y.clear_decentries)
        clr_btn.configure(relief='flat')
        clr_btn.configure(background="#044c92")
        clr_btn.configure(borderwidth="0px")
        clr_btn.configure(cursor="hand2")
        clr_btn.configure(relief='flat')
        clr_btn.place(relx=0.36, rely=0.27)

        add_btn = tk.Button(parent_frame, text="ADD", height=0, width=12, foreground='white',
                            font="-family {Prototype} -size 12", command=y.adddecoration)
        add_btn.configure(relief='flat')
        add_btn.configure(background="#044c92")
        add_btn.configure(borderwidth="0px")
        add_btn.configure(cursor="hand2")
        add_btn.configure(relief='flat')
        add_btn.place(relx=0.06, rely=0.27)

        update_btn = tk.Button(parent_frame, text="UPDATE", height=0, width=12, foreground='white',
                               font="-family {Prototype} -size 12", command=y.updatedecoration)
        update_btn.configure(relief='flat')
        update_btn.configure(background="#044c92")
        update_btn.configure(borderwidth="0px")
        update_btn.configure(cursor="hand2")
        update_btn.place(relx=0.16, rely=0.27)

        delete_btn = tk.Button(parent_frame, text="DELETE", height=0, width=12, foreground='white',
                               font="-family {Prototype} -size 12", command=y.deletedecoration)
        delete_btn.configure(background="#044c92")
        delete_btn.configure(borderwidth="0px")
        delete_btn.configure(cursor="hand2")
        delete_btn.configure(relief='flat')
        delete_btn.place(relx=0.26, rely=0.27)

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
        tree_frame = Frame(dectree_frame, width=1250, height=300)
        tree_frame.configure(background="black")
        tree_frame.pack(pady=(50, 0))

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

        # bind selected record
        mydec_tree.bind("<ButtonRelease-1>", y.decselect_record)

        # -------------------------------SERVICES----------------------------------------
        global sernextid,sser_entry, myser_tree, sser_var, serid_entry, sername_entry, sercost_entry

        serrecord_frame = LabelFrame(parent_frame, text="Records", width=600, height=200,
                                     font="-family {Prototype} -size 15",
                                     fg="#044c92", bg="white", bd=2, relief='groove')
        serrecord_frame.place(relx=0.51, rely=0.05)

        sertree_frame = LabelFrame(parent_frame, text="Service Detail", width=1300, height=150,
                                   font="-family {Prototype} -size 15",
                                   fg="#044c92", bg="white", bd=2, relief='groove')
        sertree_frame.place(relx=0.51, rely=0.35)
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

        serid_lable = Label(serrecord_frame, text="Service ID", font="-family {Prototype} -size 11", bg="white")
        serid_lable.grid(row=0, column=0, padx=10, pady=10)
        serid_entry = Entry(serrecord_frame, font="-family {Prototype} -size 11", relief='solid', bd=1)
        serid_entry.grid(row=0, column=1, padx=10, pady=10)
        c.execute("SELECT MAX(SERVICEID) FROM SERVICE")
        sernextid = c.fetchall()
        sernextid = sernextid[0][0] + 10
        serid_entry.insert(0, sernextid)
        serid_entry.config(state='readonly')

        sername_lable = Label(serrecord_frame, text="Service Name", font="-family {Prototype} -size 11",
                              bg='white')
        sername_lable.grid(row=0, column=2, padx=10, pady=10)
        sername_entry = Entry(serrecord_frame, font="-family {Prototype} -size 11", relief='solid', bd=1)
        sername_entry.grid(row=0, column=3, padx=10, pady=10)

        sercost_lable = Label(serrecord_frame, text="Service Cost", font="-family {Prototype} -size 11", bg='white')
        sercost_lable.grid(row=1, column=0, padx=10, pady=10)
        sercost_entry = Entry(serrecord_frame, font="-family {Prototype} -size 11", relief='solid', bd=1)
        sercost_entry.grid(row=1, column=1, padx=10, pady=10)

        clr_btn = tk.Button(parent_frame, text="CLEAR", height=0, width=12, foreground='white',
                            font="-family {Prototype} -size 12", command=y.clear_serentries)
        clr_btn.configure(relief='flat')
        clr_btn.configure(background="#044c92")
        clr_btn.configure(borderwidth="0px")
        clr_btn.configure(cursor="hand2")
        clr_btn.configure(relief='flat')
        clr_btn.place(relx=0.86, rely=0.27)

        add_btn = tk.Button(parent_frame, text="ADD", height=0, width=12, foreground='white',
                            font="-family {Prototype} -size 12", command=y.addservices)
        add_btn.configure(relief='flat')
        add_btn.configure(background="#044c92")
        add_btn.configure(borderwidth="0px")
        add_btn.configure(cursor="hand2")
        add_btn.configure(relief='flat')
        add_btn.place(relx=0.56, rely=0.27)

        update_btn = tk.Button(parent_frame, text="UPDATE", height=0, width=12, foreground='white',
                               font="-family {Prototype} -size 12", command=y.updateservices)
        update_btn.configure(relief='flat')
        update_btn.configure(background="#044c92")
        update_btn.configure(borderwidth="0px")
        update_btn.configure(cursor="hand2")
        update_btn.place(relx=0.66, rely=0.27)

        delete_btn = tk.Button(parent_frame, text="DELETE", height=0, width=12, foreground='white',
                               font="-family {Prototype} -size 12", command=y.deleteservices)
        delete_btn.configure(background="#044c92")
        delete_btn.configure(borderwidth="0px")
        delete_btn.configure(cursor="hand2")
        delete_btn.configure(relief='flat')
        delete_btn.place(relx=0.76, rely=0.27)

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
        sertree_frame = Frame(sertree_frame, width=1250, height=300)
        sertree_frame.configure(background="black")
        sertree_frame.pack(pady=(50, 0))

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

        # bind selected record
        myser_tree.bind("<ButtonRelease-1>", y.serselect_record)


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
        bt_home = tk.Button(topframe2, image=logoicon, borderwidth=0, command=y.home)
        bt_home.place(relx=0.016, rely=0.02, height="40px", width="40px")
        bt_home.configure(relief='flat')
        bt_home.configure(background="#044c92")
        bt_home.configure(borderwidth="0px")
        bt_home.configure(cursor="hand2")
        bt_home.configure(relief='flat')

        bt_register = tk.Button(topframe2, command=y.registeremployee)
        bt_register.place(relx=0.09, rely=0.2, height=30, width=170)
        bt_register.configure(activebackground="white")
        bt_register.configure(activeforeground="#044c92")
        bt_register.configure(background="white")
        bt_register.configure(disabledforeground="white")
        bt_register.configure(font="-family {Prototype} -size 15")
        bt_register.configure(foreground="#044c92")
        bt_register.configure(highlightbackground="white")
        bt_register.configure(highlightcolor="white")
        bt_register.configure(text='''Employee''')
        bt_register.configure(relief='flat')
        bt_register.configure(cursor='hand2')
        # #
        bt_venue = tk.Button(topframe2, command=y.venue)
        bt_venue.place(relx=0.27, rely=0.2, height=30, width=170)
        bt_venue.configure(activebackground="white")
        bt_venue.configure(activeforeground="#044c92")
        bt_venue.configure(background="white")
        bt_venue.configure(cursor="hand2")
        bt_venue.configure(disabledforeground="white")
        bt_venue.configure(font="-family {Prototype} -size 15")
        bt_venue.configure(foreground="#044c92")
        bt_venue.configure(highlightbackground="white")
        bt_venue.configure(highlightcolor="white")
        bt_venue.configure(relief="flat")
        bt_venue.configure(text='''Venue''')
        #
        bt_food = tk.Button(topframe2, command=y.food)
        bt_food.place(relx=0.45, rely=0.2, height=30, width=170)
        bt_food.configure(activebackground="white")
        bt_food.configure(activeforeground="#044c92")
        bt_food.configure(background="white")
        bt_food.configure(disabledforeground="white")
        bt_food.configure(font="-family {Prototype} -size 15")
        bt_food.configure(foreground="#044c92")
        bt_food.configure(highlightbackground="white")
        bt_food.configure(highlightcolor="#d9d9d9")
        bt_food.configure(cursor="hand2")
        bt_food.configure(relief="flat")
        bt_food.configure(text='''Food''')
        #
        bt_services = tk.Button(topframe2, command=y.services)
        bt_services.place(relx=0.63, rely=0.2, height=30, width=170)
        bt_services.configure(activebackground="white")
        bt_services.configure(activeforeground="#044c92")
        bt_services.configure(background="white")
        bt_services.configure(disabledforeground="white")
        bt_services.configure(font="-family {Prototype} -size 15")
        bt_services.configure(foreground="#044c92")
        bt_services.configure(highlightbackground="white")
        bt_services.configure(highlightcolor="white")
        bt_services.configure(relief="flat")
        bt_services.configure(text='''Service''')
        bt_services.configure(cursor="hand2")

        bt_logout = tk.Button(topframe2, command=y.logout)
        bt_logout.place(relx=0.81, rely=0.2, height=30, width=170)
        bt_logout.configure(activebackground="white")
        bt_logout.configure(activeforeground="#044c92")
        bt_logout.configure(background="white")
        bt_logout.configure(disabledforeground="white")
        bt_logout.configure(font="-family {Prototype} -size 15")
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
