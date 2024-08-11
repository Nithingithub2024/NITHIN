from tkinter import *
from customtkinter import *
from tkinter import messagebox
import pymysql
def register():
    def submit():
        #checking for empty field
        if name.get()=='':
            name.configure( border_width=1.5,border_color='red')
            return
        else:
            name.configure( border_width=1.5,border_color='grey')
        if address.get()=='':
            address.configure( border_width=1.5,border_color='red')
            return
        else:
            address.configure( border_width=1.5,border_color='grey')
        if len(phone.get())!=10:
            phone.configure( border_width=1.5,border_color='red')
            return
        else:
            phone.configure( border_width=1.5,border_color='grey')
        if 20<len(username.get()) or len(username.get())<1:
            username.configure( border_width=1.5,border_color='red')
            return
        else:
            username.configure( border_width=1.5,border_color='grey')
        if len(password.get())<8 or len(password.get())>15:
            password.configure(  border_width=1.5,border_color='red')
            password_alert.configure(text_color='red')
            return
        else:
            try:
                password.configure( border_width=1.5,border_color='grey')
                password_alert.configure(text_color='grey')
                #saving details to data base 
                con=pymysql.connect(host='localhost',user='root',passwd='root',database='project')
                c=con.cursor()
                sql = "insert into register(name,address,ph) values('%s','%s',%d)"%(name.get(),address.get(),int(phone.get()))
                c.execute(sql)
                sql="update register set username='%s',pasword='%s' where ph=%d"%(username.get(),password.get(),int(phone.get()))
                c.execute(sql)
                con.commit()
                con.close()
                register_window.destroy()
                messagebox.showinfo("Information","Sign-in successfull.")
            except Exception as e:
                a=str(e)
                if a[-21:-3] =='register.ph_UNIQUE' :
                    phone.configure( border_width=1.5,border_color='red')
                    messagebox.showinfo("Information","Phonenumber already exists.")
                elif a[-27:-3] == 'register.username_UNIQUE':
                    username.configure( border_width=1.5,border_color='red')
                    messagebox.showinfo("Information","Username already exists.")
                else:
                    print("error"+a)
                con.rollback()
                con.close()
        # print(register_window.winfo_geometry())
    def clear():
        #CLEARING ALL THE FIELDS
        name.delete(0,END)
        address.delete(0,END)
        phone.delete(0,END)
        username.delete(0,END)
        password.delete(0,END)
        #TURNING 1ST FIELD'S BORDER INTO RED AND OTHER TO GREY 
        name.configure( border_width=1.5,border_color='red')
        address.configure( border_width=1.5,border_color='grey')
        phone.configure( border_width=1.5,border_color='grey')
        username.configure( border_width=1.5,border_color='grey')
        password.configure( border_width=1.5,border_color='grey')
        password_alert.configure(text_color='grey')


    register_window=Toplevel()
    register_window.title("Register")
    register_window.grab_set()    #disabling root
    register_window.focus()
    register_window.config(borderwidth=50,bg='violet')
    register_window.geometry("429x349+562+228")
    #creating lables
    name_label = CTkLabel(register_window,text="Name",anchor="e",font=('arial',15)) 
    address_label = CTkLabel(register_window,text="Address",font=('arial',15)) 
    phone_label = CTkLabel(register_window,text="Phone number",font=('arial',15)) 
    username_label = CTkLabel(register_window,text="User name",font=('arial',15)) 
    password_label = CTkLabel(register_window,text="Password",font=('arial',15)) 
    password_alert = CTkLabel(register_window,text="password length should \nbe between 8 to 15 character")

    #creating entry field 
    name = CTkEntry(register_window,font=('arial',15),border_width=1.5,border_color='grey',fg_color='white',corner_radius=5,width=160) 
    address = CTkEntry(register_window,font=('arial',15), border_width=1.5,border_color='grey',fg_color='white',corner_radius=5,width=160) 
    phone = CTkEntry(register_window,font=('arial',15), border_width=1.5,border_color='grey',fg_color='white',corner_radius=5,width=160) 
    username = CTkEntry(register_window,font=('arial',15), border_width=1.5,border_color='grey',fg_color='white',corner_radius=5,width=160) 
    password = CTkEntry(register_window,font=('arial',15), border_width=1.5,border_color='grey',fg_color='white',corner_radius=5,width=160) 

    #creating buttons
    submit_button = CTkButton(register_window,text="SUBMIT",fg_color='#636363',command=submit,corner_radius=25,hover_color='#222222',font=('arial',15))
    clear_button = CTkButton(register_window,text="Clear",command=clear,corner_radius=25,font=('arial',15),width=100)

    #placing everyting into the screen
    #--labels--
    name_label.grid(row=0,column=0,sticky='w',padx=20)
    address_label.grid(row=1,column=0,sticky='w',padx=20)
    phone_label.grid(row=2,column=0,sticky='w',padx=20)
    username_label.grid(row=3,column=0,sticky='w',padx=20)
    password_label.grid(row=4,column=0,sticky='w',padx=20)
    password_alert.grid(row=5,column=1)
    #--labels--
    #--entrys--
    name.grid(row=0,column=1,padx=10,pady=(0,10))
    address.grid(row=1,column=1,padx=10,pady=(0,10))
    phone.grid(row=2,column=1,padx=10,pady=(0,10))
    username.grid(row=3,column=1,padx=10,pady=(0,10))
    password.grid(row=4,column=1,padx=10,pady=0)
    #--entrys--
    #--buttons--
    clear_button.grid(row=6,column=0,padx=20)
    submit_button.grid(row=6,column=1,pady=10)
    #--buttons--


    register_window.mainloop()

def CRUD():
    messagebox.showinfo("Information","Log-in successfull.")
    pass