from tkinter import *
from PIL import Image
def enter(event):
    print("clicked")
class temp:
    a=10
    print('hi')
root = Tk()
imgl = Image.open('eyeopen.png')
# imgd = Image.open('eyeclose.png')
# img = Image(dark_image=imgl,light_image=imgd)
eye = Button(root,text='thrs',command=lambda : temp())
entry = Entry(root)
entry.pack()
entry.bind('<Return>',lambda event : print("hi"))
eye.pack()
eye.bind_all('<Return>',enter)
root.mainloop()