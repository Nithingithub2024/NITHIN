from tkinter import *
from customtkinter import *
from tkinter import messagebox,ttk
from customtkinter import filedialog
import pymysql
from PIL import Image
from tooltip import *
import PIL
import PIL.Image
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
            try:
                int(phone.get())
            except:
                phone.configure( border_width=1.5,border_color='red')
                return
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
                con = pymysql.connect(host='localhost',user='root',password='root',database='project')
                c = con.cursor()
                sql = "insert into register(name,address,ph) values('%s','%s','%s')"%(name.get(),address.get(),phone.get())
                c.execute(sql)
                sql = "update register set username='%s',pasword='%s' where ph='%d'"%(username.get(),password.get(),int(phone.get()))
                c.execute(sql)
                con.commit()
                con.close()
                register_window.destroy()
                messagebox.showinfo("Information","Sign-in successfull.")
            except Exception as e:
                a=str(e)
                if a[-21:-3] == 'register.ph_UNIQUE' :
                    phone.configure( border_width=1.5,border_color='red')
                    messagebox.showerror("Error","Phonenumber already exists.")
                elif a[-27:-3] == 'register.username_UNIQUE':
                    username.configure( border_width=1.5,border_color='red')
                    messagebox.showerror("Error","Username already exists.") 
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
        name.focus()

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
    #focus fumctions
    def focus_to_address(event):
        address.focus()
        
    def focus_to_phone(event):
        if event.char=='\r' or str(event.keysym)=='Down':
            phone.focus()
        else:
            name.focus()
    def focus_to_user(event):
        if event.char=='\r' or str(event.keysym)=='Down':
            username.focus()
        else:
            address.focus()
    def focus_to_password(event):
        if event.char=='\r' or str(event.keysym)=='Down':    
            password.focus()
        else:
            phone.focus()
    def focus_to_submit(event):
        username.focus()
    #--focusings
    name.focus()
    name.bind('<Return>',focus_to_address)
    name.bind('<Down>',focus_to_address)
    address.bind('<Return>',focus_to_phone)
    address.bind('<Down>',focus_to_phone)
    address.bind('<Up>',focus_to_phone)
    phone.bind('<Return>',focus_to_user)
    phone.bind('<Down>',focus_to_user)
    phone.bind('<Up>',focus_to_user)
    username.bind('<Return>',focus_to_password)
    username.bind('<Down>',focus_to_password)
    username.bind('<Up>',focus_to_password)
    password.bind('<Return>',lambda event: submit())
    password.bind('<Up>',focus_to_submit)
    


    register_window.mainloop()

def CRUD(userdetails):
    messagebox.showinfo("Information","Log-in successfull.")
    #functions
    userdetails_window=None
    def logoutfunc():
        if userdetails_window!=None:
            userdetails_window.grab_release()
            userdetails_window.destroy()
        crud_window.grab_release()
        root.deiconify()
        crud_window.destroy()
    def details():
        global userdetails_window
        userdetails_window =Toplevel(crud_window)
        sc_width = int((crud_window.winfo_screenwidth()/2)-(145))
        sc_heigt = int((crud_window.winfo_screenheight()/2)-(100))
        userdetails_window.geometry(f"290x200+{sc_width}+{sc_heigt}")
        userdetails_window.grab_set()
        userdetails_window.focus()
        userdetails_window.title('User details')
        userdetails_window.resizable(False,False)
        #labels for details
        CTkLabel(userdetails_window,text='Name:').grid(row=0,column=0,sticky=E,pady=(10,0))
        CTkLabel(userdetails_window,text='Phone number:').grid(row=1,column=0,sticky=E,padx=(55,0))
        CTkLabel(userdetails_window,text='Address:').grid(row=2,column=0,sticky=E)
        CTkLabel(userdetails_window,text='Username:').grid(row=3,column=0,sticky=E)
        CTkLabel(userdetails_window,text='Password:').grid(row=4,column=0,sticky=E)
        CTkLabel(userdetails_window,text=f'{userdetails[0][0]}').grid(row=0,column=1,sticky=W,padx=(10,0),pady=(10,0))
        CTkLabel(userdetails_window,text=f'{userdetails[0][2]}').grid(row=1,column=1,sticky=W,padx=(10,0))
        CTkLabel(userdetails_window,text=f'{userdetails[0][1]}').grid(row=2,column=1,sticky=W,padx=(10,0))
        CTkLabel(userdetails_window,text=f'{userdetails[0][3]}').grid(row=3,column=1,sticky=W,padx=(10,0))
        CTkLabel(userdetails_window,text=f'{userdetails[0][4]}').grid(row=4,column=1,sticky=W,padx=(10,0))
        #buttons
        def okfunc():
            userdetails_window.destroy()
            crud_window.focus()
        ok = CTkButton(userdetails_window,corner_radius=5,width=80,fg_color='#01b401',text='OK',hover_color='#00a400',command=okfunc)
        ok.grid(pady=10,row=5,column=0,padx=(30,0))
        logout_button = CTkButton(userdetails_window,image=CTkImage(login),corner_radius=5,width=80,fg_color='#e01b1b',text='Logout',hover_color='#c51a1a',command=logoutfunc)
        logout_button.grid(pady=10,row=5,column=1,padx=(30,0))
        userdetails_window.mainloop()
    def show():
        try:
            con=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cu=con.cursor()
            sql="select * from student;"
            cu.execute(sql)
            val=cu.fetchall()
            for i in val :
                table.insert('','end',values=i)
            con.close()
        except Exception as e:
            messagebox.showerror('Error',e)
            con.close 
    def img_select():
        id_entry.configure( border_width=1.5,border_color='#1a75ff')
        name_entry.configure( border_width=1.5,border_color='#1a75ff')
        address_entry.configure( border_width=1.5,border_color='#1a75ff')
        phone_entry.configure( border_width=1.5,border_color='#1a75ff')
        imgpath_entry.configure( border_width=1.5,border_color='#1a75ff')
        try:
            stud_img_path = filedialog.askopenfilename(initialdir='C:/Users/ADMIN/Pictures',title='Select the image',filetypes=(('png files','*.png'),('jpg files','*.jpg'),('jpeg files','*.jpeg'),('All files','*.*')))
            stud_img = CTkImage(Image.open(stud_img_path),size=(150,150))
            person_label.configure(image=stud_img)
            imgpath_entry.delete(0,END)
            imgpath_entry.insert(0,stud_img_path)
            return
        except PIL.UnidentifiedImageError :
            messagebox.showerror('ERROR','Please select a image file')
            person_label.configure(image=CTkImage(person,size=(150,150)))
        except EXCEPTION as e:
            person_label.configure(image=CTkImage(person,size=(150,150)))
            print(e)
    def insert():
        name_entry.configure( border_width=1.5,border_color='#1a75ff')
        address_entry.configure( border_width=1.5,border_color='#1a75ff')
        phone_entry.configure( border_width=1.5,border_color='#1a75ff')
        imgpath_entry.configure( border_width=1.5,border_color='#1a75ff')
        if id_entry.get()=='':
            id_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            try:
                int(id_entry.get())
            except:
                id_entry.configure( border_width=1.5,border_color='red')
                return
            id_entry.configure( border_width=1.5,border_color='#1a75ff')
        if name_entry.get()=='':
            name_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            name_entry.configure( border_width=1.5,border_color='#1a75ff')
        if address_entry.get()=='':
            address_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            address_entry.configure( border_width=1.5,border_color='#1a75ff')
        if len(phone_entry.get())!=10:
            phone_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            try:
                int(phone_entry.get())
            except:
                phone_entry.configure( border_width=1.5,border_color='red')
                return
            phone_entry.configure( border_width=1.5,border_color='#1a75ff')
            try:
                try:
                    Image.open(imgpath_entry.get())
                    imgpath_entry.configure( border_width=1.5,border_color='#1a75ff')
                except Exception as e:
                    imgpath_entry.configure( border_width=1.5,border_color='red')
                    print(e)
                    return
                con=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cu=con.cursor()
                sql="insert into student values(%d,'%s','%s',%d,'%s') "%(int(id_entry.get()),name_entry.get(),address_entry.get(),int(phone_entry.get()),imgpath_entry.get())
                cu.execute(sql)
                con.commit()
                table.insert('','end',values=(int(id_entry.get()),name_entry.get(),address_entry.get(),int(phone_entry.get()),imgpath_entry.get()))
                messagebox.showinfo(title='Information',message='Data inserted successfully.')
                name_entry.delete(0,END)
                address_entry.delete(0,END)
                id_entry.delete(0,END)
                phone_entry.delete(0,END)
                imgpath_entry.delete(0,END)
                person_label.configure(image=CTkImage(person,size=(150,150)))
                con.close()
                id_entry.focus()
                return
            except Exception as e:
                a=str(e)
                if a[-21:-3] == 'student. ph_UNIQUE' :
                    phone_entry.configure( border_width=1.5,border_color='red')
                    messagebox.showerror("Error","Phonenumber already exists.")
                elif a[-18:-3] == 'student.PRIMARY':
                    id_entry.configure( border_width=1.5,border_color='red')
                    messagebox.showerror("Error","ID already exists.")
                else:
                    messagebox.showerror(title='ERROR',message=e)
                con.rollback()
                con.close()
    def update():
        name_entry.configure( border_width=1.5,border_color='#1a75ff')
        address_entry.configure( border_width=1.5,border_color='#1a75ff')
        phone_entry.configure( border_width=1.5,border_color='#1a75ff')
        imgpath_entry.configure( border_width=1.5,border_color='#1a75ff')
        if id_entry.get()=='':
            id_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            try:
                int(id_entry.get())
                #connecting to database 
                con=pymysql.connect(host='localhost',user='root',password='root',database='project')
                c=con.cursor()
                #geting password using username
                sql="select id from student "
                c.execute(sql)
                ids=c.fetchall()
                con.close()
                ids[0]
                check=0
                for i in ids:
                    if i[0]==int(id_entry.get()):
                        check=1
                        break
                if check==1:
                    pass
                else:
                    messagebox.showerror('Error','ID not found.Check the ID and try again')
                    return
            except IndexError:
                messagebox.showerror('Error','No Information in database.\nPlease add details to update it.')
                return
            except Exception as e:
                id_entry.configure( border_width=1.5,border_color='red')
                return
            id_entry.configure( border_width=1.5,border_color='#1a75ff')
        if name_entry.get()=='':
            name_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            name_entry.configure( border_width=1.5,border_color='#1a75ff')
        if address_entry.get()=='':
            address_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            address_entry.configure( border_width=1.5,border_color='#1a75ff')
        if len(phone_entry.get())!=10:
            phone_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            try:
                int(phone_entry.get())
            except:
                phone_entry.configure( border_width=1.5,border_color='red')
                return
            phone_entry.configure( border_width=1.5,border_color='#1a75ff')    
            try:
                con=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cu=con.cursor()
                sql="update student set name='%s',address='%s',ph=%d, imgpath='%s' where id=%d "%(name_entry.get(),address_entry.get(),int(phone_entry.get()),imgpath_entry.get(),int(id_entry.get()))
                cu.execute(sql)
                con.commit()
                for i in table.get_children():
                    table.delete(i)
                show()
                messagebox.showinfo(title='Information',message='Data updated successfully.')
                name_entry.delete(0,END)
                address_entry.delete(0,END)
                id_entry.delete(0,END)
                phone_entry.delete(0,END)
                imgpath_entry.delete(0,END)
                person_label.configure(image=CTkImage(person,size=(150,150)))
                con.close()
                id_entry.focus()
                return
                
            except Exception as e:
                a=str(e)
                if a[-21:-3] == 'student. ph_UNIQUE' :
                    phone_entry.configure( border_width=1.5,border_color='red')
                    messagebox.showerror("Error","Phonenumber already exists.")
                else:
                    messagebox.showinfo(title='ERROR',message=e)
                con.rollback()
                con.close()
    def delete():
        name_entry.configure( border_width=1.5,border_color='#1a75ff')
        address_entry.configure( border_width=1.5,border_color='#1a75ff')
        phone_entry.configure( border_width=1.5,border_color='#1a75ff')
        imgpath_entry.configure( border_width=1.5,border_color='#1a75ff')
        if id_entry.get()=='':
            id_entry.configure( border_width=1.5,border_color='red')
            return
        else:
            try:
                int(id_entry.get())
                #connecting to database 
                con=pymysql.connect(host='localhost',user='root',password='root',database='project')
                c=con.cursor()
                #geting password using username
                sql="select id from student "
                c.execute(sql)
                ids=c.fetchall()
                con.close()
                ids[0]
                check=0
                for i in ids:
                    if i[0]==int(id_entry.get()):
                        check=1
                        break
                if check==1:
                    pass
                else:
                    messagebox.showerror('Error','ID not found.')
                    return
            except IndexError:
                messagebox.showerror('Error','No Information in database.')
                id_entry.configure( border_width=1.5,border_color='red')
                return
            except Exception as e:
                # print(e)
                id_entry.configure( border_width=1.5,border_color='red')
                return
            id_entry.configure( border_width=1.5,border_color='#1a75ff')
            ask = messagebox.askyesno('Confirmation',f'Are you sure to delete these details\nID : \nName : \n Address')
            if ask==1:    
                try:
                    con=pymysql.connect(host='localhost',user='root',password='root',database='project')
                    cu=con.cursor()
                    sql="delete from student where id=%d"%(int(id_entry.get()))
                    cu.execute(sql)
                    con.commit()
                    con.close()
                    for i in table.get_children():
                        table.delete(i)
                    show()
                    name_entry.delete(0,END)
                    address_entry.delete(0,END)
                    id_entry.delete(0,END)
                    phone_entry.delete(0,END)
                    imgpath_entry.delete(0,END)
                    person_label.configure(image=CTkImage(person,size=(150,150)))
                    messagebox.showinfo(title='Information',message='Data deleted successfully.')
                    id_entry.focus()
                except Exception as e:
                    con.rollback()
                    con.close()
                    messagebox.showinfo(title='ERROR',message=e)
    def search():
        id_entry.configure( border_width=1.5,border_color='#1a75ff')
        name_entry.configure( border_width=1.5,border_color='#1a75ff')
        address_entry.configure( border_width=1.5,border_color='#1a75ff')
        phone_entry.configure( border_width=1.5,border_color='#1a75ff')
        imgpath_entry.configure( border_width=1.5,border_color='#1a75ff')
        if search_entry.get()=='':
            search_entry.configure(border_color='red')
            return
        else:
            search_entry.configure(border_color='#1a75ff')
            try:
                int(search_entry.get())
                #connecting to database 
                con=pymysql.connect(host='localhost',user='root',password='root',database='project')
                c=con.cursor()
                #geting password using username
                sql="select id from student "
                c.execute(sql)
                ids=c.fetchall()
                con.close()
                ids[0]
                for i in table.get_children():
                    table.delete(i)
                show()
                pos=0
                check=0
                for i in ids:
                    if i[0]==int(search_entry.get()):
                        check=1
                        break
                    pos+=1
                if check==1:
                    table.selection_set(table.get_children()[pos])
                    vals = table.item(table.get_children()[pos])['values']
                    id_entry.delete(0,END)
                    name_entry.delete(0,END)
                    address_entry.delete(0,END)
                    phone_entry.delete(0,END)
                    imgpath_entry.delete(0,END)
                    id_entry.insert(0,vals[0])
                    name_entry.insert(0,vals[1])
                    address_entry.insert(0,vals[2])
                    phone_entry.insert(0,vals[3])
                    imgpath_entry.insert(0,vals[4])
                    person_label.configure(image=CTkImage(Image.open(vals[4]),size=(150,150)))
                    id_entry.focus()
                else:
                    messagebox.showerror('Error','ID not found.')
                    return
            except IndexError:
                messagebox.showerror('Error','No Information in database.\nPlease add details to update it.')
                return
            except Exception as e:
                search_entry.configure( border_width=1.5,border_color='red')
                print(e)
                return
            search_entry.configure( border_width=1.5,border_color='#1a75ff')
    def clear():
        name_entry.delete(0,END)
        address_entry.delete(0,END)
        id_entry.delete(0,END)
        phone_entry.delete(0,END)
        imgpath_entry.delete(0,END)
        id_entry.focus()
        person_label.configure(image=CTkImage(person,size=(150,150)))
        id_entry.configure( border_width=1.5,border_color='#1a75ff')
        name_entry.configure( border_width=1.5,border_color='#1a75ff')
        address_entry.configure( border_width=1.5,border_color='#1a75ff')
        phone_entry.configure( border_width=1.5,border_color='#1a75ff')
        imgpath_entry.configure( border_width=1.5,border_color='#1a75ff')
    def select(event):
        vals = table.item(table.selection())['values']
        id_entry.delete(0,END)
        name_entry.delete(0,END)
        address_entry.delete(0,END)
        phone_entry.delete(0,END)
        imgpath_entry.delete(0,END)
        id_entry.configure( border_width=1.5,border_color='#1a75ff')
        name_entry.configure( border_width=1.5,border_color='#1a75ff')
        address_entry.configure( border_width=1.5,border_color='#1a75ff')
        phone_entry.configure( border_width=1.5,border_color='#1a75ff')
        imgpath_entry.configure( border_width=1.5,border_color='#1a75ff')
        id_entry.insert(0,vals[0])
        name_entry.insert(0,vals[1])
        address_entry.insert(0,vals[2])
        phone_entry.insert(0,vals[3])
        imgpath_entry.insert(0,vals[4])
        person_label.configure(image=CTkImage(Image.open(vals[4]),size=(150,150)))
        id_entry.focus()
    #images
    login = Image.open('login.png')
    person = Image.open('person.png')
    search_img = Image.open('search.png')
    add = Image.open('add.png')
    upload_img = Image.open('upload.png')
    trash_img = Image.open('trash.png')
    clear_img = Image.open('clear.png')
    update_img = Image.open('update.png')
    user = Image .open('user.png')
    #creating toplevel
    crud_window=Toplevel()
    sc_width = int((crud_window.winfo_screenwidth()/2)-(300))
    sc_heigt = int((crud_window.winfo_screenheight()/2)-(280))
    crud_window.geometry(f"600x560+{sc_width}+{sc_heigt}")
    crud_window.grab_set()
    crud_window.configure(bg='#a366ff')
    crud_window.resizable(False,False)

    #creating frames
    frame_details = CTkFrame(crud_window,width=600,height=220,corner_radius=20,fg_color='white')
    frame_details.place(x=0,y=50)
    frame_image = CTkFrame(frame_details,corner_radius=10,width=150,height=150)
    frame_image.place(x=280,y=10)

    #creating labels
    CTkLabel(frame_details,text='ID:',font=('arial',15)).place(x=20,y=10)
    CTkLabel(frame_details,text='Name:',font=('arial',15)).place(x=20,y=50)
    CTkLabel(frame_details,text='Address:',font=('arial',15)).place(x=20,y=90)
    CTkLabel(frame_details,text='Phonenumber:',font=('arial',15)).place(x=20,y=130)
    CTkLabel(frame_details,text="ImagePath",font=('arial',15)).place(x=20,y=175)
    crud = CTkButton(crud_window,text="CRUD",width=10,font=('arial',15),anchor='center',text_color='black',corner_radius=10,fg_color='transparent')
    crud.place(x=10,y=10)
    person_label = CTkLabel(frame_image,text='',image=CTkImage(person,size=(150,150)))

    #creating entry fields
    id_entry = CTkEntry(frame_details, border_width=2, font=('arial',15),border_color='#1a75ff')
    name_entry = CTkEntry(frame_details, border_width=2, font=('arial',15),border_color='#1a75ff')
    address_entry = CTkEntry(frame_details, border_width=2, font=('arial',15),border_color='#1a75ff')
    phone_entry = CTkEntry(frame_details, border_width=2, font=('arial',15),border_color='#1a75ff')
    imgpath_entry = CTkEntry(frame_details, border_width=2, font=('arial',15),width=170,border_color='#1a75ff')
    search_entry = CTkEntry(frame_details, border_width=2,border_color='#1a75ff', font=('arial',15) ,width=90)

    #buttons
    logout = CTkButton(crud_window,image=CTkImage(user),hover_color='#955ee8',fg_color='#a366ff',text='',width=5,command=details)
    insert_button = CTkButton(frame_details,image=CTkImage(add),text="  ADD Details    ",fg_color='#009f56',hover_color='#018548',command=insert)
    update_button = CTkButton(frame_details,image=CTkImage(update_img),text="UPDATE Details",fg_color='#009f56',hover_color='#018548',command=update)
    delete_button = CTkButton(frame_details,image=CTkImage(trash_img),text="DELETE Details",fg_color='#009f56',hover_color='#018548',command=delete)
    upload_button = CTkButton(frame_details,image=CTkImage(upload_img),text='UPLOAD Image',fg_color='#009f56',width=125,hover_color='#018548',command=img_select)
    search_button = CTkButton(frame_details,text='',width=5,command=search,image=CTkImage(search_img),fg_color='transparent',hover_color='grey')
    clear_button =CTkButton(frame_details,image=CTkImage(clear_img),text="CLEAR Details",fg_color='#009f56',hover_color='#018548',command=clear)
    #tooltipmessage
    CreateToolTip(search_entry,'Search with id')
    CreateToolTip(logout,'User Details')
    #placing in screen
    person_label.pack()
    logout.place(x=550,y=10)
    id_entry.place(x=120,y=10)
    name_entry.place(x=120,y=50)
    address_entry.place(x=120,y=90)
    phone_entry.place(x=120,y=130)
    imgpath_entry.place(x=120,y=175)
    insert_button.place(x=450,y=55)
    update_button.place(x=450,y=95)
    delete_button.place(x=450,y=135)
    search_entry.place(x=450,y=10)
    search_button.place(x=550,y=10)
    upload_button.place(x=300,y=175)
    clear_button.place(x=450,y=175)

    #table
    style=ttk.Style()
    style.theme_use("vista")
    table=ttk.Treeview(crud_window,yscrollcommand=YView())
    table['columns']=("id","name","address","ph","imgpath")
    table.column("#0",width=0,stretch=NO)
    table.column("id",anchor=W,width=50)
    table.column("name",anchor=W,width=100)
    table.column("address",anchor=W,width=130)
    table.column("ph",anchor=W,width=120)
    table.column("imgpath",anchor=W,width=150)

    table.heading("#0",text="")
    table.heading("id",text="ID",anchor=W,)
    table.heading("name",text="NAME",anchor=W)
    table.heading("address",text="ADDRESS",anchor=W)
    table.heading("ph",text="PHONE NUMBER",anchor=W)
    table.heading("imgpath",text="Image path",anchor=W)
    table.place(x=25,y=300)
    show()
    table.bind('<Double-Button-1>',select)
    search_entry.bind('<Return>',search)
    #--focusings
    id_entry.focus()
    id_entry.bind('<Return>',lambda event :name_entry.focus())
    id_entry.bind('<Down>',lambda event :name_entry.focus())
    name_entry.bind('<Return>',lambda event :address_entry.focus())
    name_entry.bind('<Down>',lambda event :address_entry.focus())
    name_entry.bind('<Up>',lambda event:id_entry.focus())
    address_entry.bind('<Return>',lambda event :phone_entry.focus())
    address_entry.bind('<Down>',lambda event :phone_entry.focus())
    address_entry.bind('<Up>',lambda event :name_entry.focus())
    phone_entry.bind('<Return>',lambda event :imgpath_entry.focus())
    phone_entry.bind('<Down>',lambda event :imgpath_entry.focus())
    phone_entry.bind('<Up>',lambda event :address_entry.focus())
    imgpath_entry.bind('<Up>',lambda event :phone_entry.focus())
    crud_window.protocol("WM_DELETE_WINDOW",logoutfunc)
    crud_window.mainloop()
    return















#variables
eye_state = 3  

#functions for buttons
def submit():
    try:
        #connecting to database 
        con=pymysql.connect(host='localhost',user='root',password='root',database='project')
        c=con.cursor()
        #geting password using username
        sql="select pasword from register where username='%s'"%(username.get())
        c.execute(sql)
        password_in_database = c.fetchall()[0]
        #verifiying password
        if password_in_database[0]==password.get():
            username.configure(border_color='blue')
            password.configure(border_color='blue')
            # root.geometry('370x270')
            root.iconify()
            sql="select * from register where username='%s'"%(username.get())
            c.execute(sql)
            userdetails=c.fetchall()
            CRUD(userdetails)
        else:
            username.configure(border_color='blue')
            password.configure(border_color='red')
            messagebox.showerror('Error','Wrong password')
            password.focus()
            con.close()
    except IndexError as e:
        if str(e)=='tuple index out of range':
            username.configure(border_color='red')
            password.configure(border_color='blue')
            messagebox.showerror('Error','Username does not exists.')
            username.focus()
        else:
            print(e)
        con.close()
    except Exception as e:
        messagebox.showerror('Error',e)
        con.close()
def clear():
    username.delete(0,END)
    password.delete(0,END)
    username.focus()
def eye():
    global eye_state
    if eye_state%2!=0:
        password.configure(show='')
        eye_button.configure(image=eyecl)
        eye_state-=1
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
username.bind('<Return>',lambda event : password.focus())
password.bind('<Return>',lambda event :submit())
password.bind('<Up>',lambda event : username.focus())
username.bind('<Down>',lambda event : password.focus())

root.mainloop()
