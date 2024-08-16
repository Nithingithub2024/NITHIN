from tkinter import *
from customtkinter import *
import pymysql,PIL.Image
from register_and_CRUD import *

#variables
eye_state = 1  

#functions for buttons
def submit():
    # CRUD()
    try:
        #connecting to database 
        con=pymysql.connect(host='localhost',user='root',passwd='root',database='project')
        c=con.cursor()
        #geting password using username
        sql="select pasword from register where username='%s'"%(username.get())
        c.execute(sql)
        password_in_database = c.fetchall()[0]
        #verifiying password
        if password_in_database[0]==password.get():
            username.configure(border_color='blue')
            password.configure(border_color='blue')
            CRUD()
        else:
            username.configure(border_color='blue')
            password.configure(border_color='red')
            messagebox.showerror('Error','Wrong password')
            password.focus()
    except IndexError as e:
        if str(e)=='tuple index out of range':
            username.configure(border_color='red')
            password.configure(border_color='blue')
            messagebox.showerror('Error','Username does not exists.')
            username.focus()
        else:
            print(e)
    except Exception as e:
        messagebox.showerror('Error',e)

def clear():
    username.delete(0,END)
    password.delete(0,END)
    username.focus()
def eye():
    global eye_state
    if eye_state%2!=0:
        password.configure(show='')
        eye_button.configure(image=eyecl)
        eye_state+=1
    else:
        password.configure(show='*')
        eye_button.configure(image=eyeop)
        eye_state+=1

#creating a window
root=Tk()
root.title("PROJECT")
root.resizable(False,False)
root.configure(bg='lightpink')

#images
img = PIL.Image.open('login.png')
login = CTkImage(img)
img = PIL.Image.open('eyeopen.png').resize((20,20))
eyeop = CTkImage(img)
img = PIL.Image.open("eyeclose.png").resize((20,20))
eyecl = CTkImage(img)

#placing window in center of sreen
sc_width = int((root.winfo_screenwidth()/2)-(185))
sc_heigt = int((root.winfo_screenheight()/2)-(135))
root.geometry(f"370x270+{sc_width}+{sc_heigt}")
frame = CTkFrame(root)

#creating labels
username_label = CTkLabel(root,text="USERNAME",font=('arial',15))
password_label = CTkLabel(root,text="PASSWORD",font=('arial',15))
register_label = CTkLabel(root,text="If you don't have a account register below",font=('arial',15))
loginimg_label = CTkLabel(root,image=login,text='')
login_label = CTkLabel(root,text="Login",font=('arial',15))

#creating entry boxes
username = CTkEntry(root,font=('arial',15),border_width=2,corner_radius=50,border_color='blue')
password = CTkEntry(root,font=('arial',15),border_width=2,corner_radius=50,show='*',border_color='blue')

#creating buttons text="SUBMIT",fg_color='white',text_color="blue",command=submit,corner_radius=5,hover_color='darkgrey',font=('arial',15),border_width=2,border_color="blue"
submit_button = CTkButton(root,text="SUBMIT",fg_color='#636363',command=submit,corner_radius=25,hover_color='#222222',font=('arial',15))
clear_button = CTkButton(root,text="Clear",command=clear,corner_radius=25,font=('arial',15),width=100)
register_button = CTkButton(root,text="Register",command=register,corner_radius=25,font=('arial',15))
eye_button = CTkButton(root,fg_color="transparent",image=eyeop,text='',width=5,hover=FALSE,command=eye)

#placing all items in screen #FF647F #FFC0CB
loginimg_label.grid(row=0,column=0,pady=(30,0),sticky='e')
login_label.grid(row=0,column=1,columnspan=2,pady=(30,0),sticky='w',ipadx=5)
username_label.grid(row=1,column=0,padx=(50,10),pady=(5,10))
password_label.grid(row=2,column=0,padx=(50,10),pady=(0,10))
username.grid(row=1,column=1,padx=(10,0),pady=(5,10))
password.grid(row=2,column=1,padx=(10,0),pady=(0,10),sticky='w')
clear_button.grid(row=3,column=0,padx=(50,10),pady=(0,10))
submit_button.grid(row=3,column=1,padx=(10,0),pady=(0,10))
register_label.grid(row=4,column=0,columnspan=3,padx=(30,0),pady=(0,0))
register_button.grid(row=5,column=0,columnspan=3,padx=(30,10),pady=(0,50))
eye_button.grid(row=2,column=2,sticky='n')

#focusing
username.bind('<Return>',lambda event: password.focus())

root.mainloop()
