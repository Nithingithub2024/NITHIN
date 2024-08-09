from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
import pymysql
#functions for buttons
def submit():
    pass
def clear():
    pass
def register():
    def submit():
        if name.get()=='':
            name.configure(border_width=1,border_color='red')
        if address.get()=='':
            address.configure(border_width=1,border_color='red')
        if phone.get()=='':
            phone.configure(border_width=1,border_color='red')
        if 20>len(username.get()):
            username.configure(border_width=1,border_color='red')
        if len(password.get())<8 or len(password.get())>15:
            password.configure(border_width=1,border_color='red')
            password_alert.configure(text_color='red')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',passwd='root',database='project')
                c=con.cursor()
                print("hgvdf",password.get())
            except:
                pass
    register_window=Toplevel()
    register_window.title("Register")
    register_window.grab_set()    #disabling root
    register_window.focus()
    register_window.config(borderwidth=40,bg='darkgrey')
    register_window.geometry("380x298+618+236")

    #creating lables
    name_label = CTkLabel(register_window,text="Name",anchor="e",font=('arial',15)) 
    address_label = CTkLabel(register_window,text="Address",font=('arial',15)) 
    phone_label = CTkLabel(register_window,text="Phone number",font=('arial',15)) 
    username_label = CTkLabel(register_window,text="User name",font=('arial',15)) 
    password_label = CTkLabel(register_window,text="Password",font=('arial',15)) 
    password_alert = CTkLabel(register_window,text="password length should \nbe between 8 to 15 character")

    #creating entry field 
    name = CTkEntry(register_window,font=('arial',15),border_width=0,corner_radius=0) 
    address = CTkEntry(register_window,font=('arial',15),border_width=0,corner_radius=0) 
    phone = CTkEntry(register_window,font=('arial',15),border_width=0,corner_radius=0) 
    username = CTkEntry(register_window,font=('arial',15),border_width=0,corner_radius=0) 
    password = CTkEntry(register_window,font=('arial',15),border_width=0,corner_radius=0) 

    #creating buttons
    submit_button = CTkButton(register_window,text="SUBMIT",fg_color='#636363',command=submit,corner_radius=25,hover_color='#222222',font=('arial',15))
    clear_button = CTkButton(register_window,text="Clear",command=clear,corner_radius=25,font=('arial',15))

    #placing everyting into the screen
    #--labels--
    name_label.grid(row=0,column=0,sticky='w')
    address_label.grid(row=1,column=0,sticky='w')
    phone_label.grid(row=2,column=0,sticky='w')
    username_label.grid(row=3,column=0,sticky='w')
    password_label.grid(row=4,column=0,sticky='w')
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
    clear_button.grid(row=6,column=0)
    submit_button.grid(row=6,column=1,pady=10)


    register_window.mainloop()

#creating a window
root=Tk()
root.title("PROJECT")
root.resizable(False,False)
root.config(bg='darkgrey')
#placing window in center of sreen
sc_width = int((root.winfo_screenwidth()/2)-(200))
sc_heigt = int((root.winfo_screenheight()/2)-(135))
root.geometry(f"400x270+{sc_width}+{sc_heigt}")

#creating labels
username_label = CTkLabel(root,text="USERNAME",font=('arial',15))
password_label = CTkLabel(root,text="PASSWORD",font=('arial',15))
register_label = CTkLabel(root,text="If you don't have a account register below",font=('arial',15))

#creating entry boxes
username = CTkEntry(root,font=('arial',15),border_width=0,corner_radius=0)
password = CTkEntry(root,font=('arial',15),border_width=0,corner_radius=0,show='*')

#creating buttons
submit_button = CTkButton(root,text="SUBMIT",fg_color='#636363',command=submit,corner_radius=25,hover_color='#222222',font=('arial',15))
clear_button = CTkButton(root,text="Clear",command=clear,corner_radius=25,font=('arial',15))
register_button = CTkButton(root,text="Register",command=register,corner_radius=25,font=('arial',15))

#placing all items in screen 
username_label.grid(row=0,column=0,padx=(50,10),pady=(50,10))
password_label.grid(row=1,column=0,padx=(50,10),pady=(0,10))
username.grid(row=0,column=1,padx=(10,50),pady=(50,10))
password.grid(row=1,column=1,padx=(10,50),pady=(0,10))
clear_button.grid(row=2,column=0,padx=(50,10),pady=(0,10))
submit_button.grid(row=2,column=1,padx=(10,50),pady=(0,10))
register_label.grid(row=3,column=0,columnspan=2,padx=(10,10),pady=(0,0))
register_button.grid(row=4,column=0,columnspan=2,padx=(10,10),pady=(0,50))

root.mainloop()
