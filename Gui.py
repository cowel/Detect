from tkinter import Frame, Tk, BOTH, Text, Menu, END, Button, LEFT,X, Entry, END, Canvas, NW,Label,PhotoImage
from tkinter.filedialog import Open,askdirectory
import os
import subprocess

# importing only those functions 
# which are needed 
from tkinter import * 
from tkinter.ttk import *
import box_detect
from PIL import ImageTk,Image
class Example(Frame):
    def __init__(self, canvas):
        Frame.__init__(self, canvas)
        self.canvas = canvas
        # self.initUI()
  
    def initUI(self):
        
       
        self.pack(fill=BOTH, expand=1)
  
    

        # canvas=Canvas(self.parent, width=200, height=180)
      
        # canvas.create_image(50,50,anchor=NW,image=image)
        # canvas.pack()

  
        # self.txt = Text(self)
        # self.txt.pack(fill=BOTH, expand=1)
       
  
    def onOpen(self):
        ftypes = [('Image files', '*.jpg'), ('All files', '*')]
        dlg = Open(self, filetypes = ftypes)
        print(dlg)
        fl = dlg.show()
  
        if fl != '':
            # refactor 
            # fl is link img
            # 1 đường dẫn chứa file excel
            # Đặt tên file
            # Run xong thì mở file excel.
            # text = self.readFile(fl)
            # self.txt.insert(END, text)
            print(fl)
            fl1 = fl.replace(".jpg", ".xlsx"),

            self.entry = Entry(self.canvas,text = fl,width=500)
            self.entry1 = Entry(self.canvas,text = fl1,width=500)
            canvas.delete(text_open)
            self.entry.insert(0, fl)
            self.entry1.insert(0, fl1)

            self.entry.pack()
            self.id = canvas.create_window(250, 80, width=400, height=30,
                                       window=self.entry)
            self.id = canvas.create_window(250, 130, width=400, height=30,
                                       window=self.entry1)
            self.button_replace = Button(self.canvas, text='Replace path excel', width=20, command =self.onChange)
            self.button_replace.pack(expand=1,side = LEFT)
            self.id = canvas.create_window(250, 170, width=150, height=25,
                                       window=self.button_replace)

            self.button = Button(self.canvas, text='Run', width=20, command = lambda: box_detect.box_extraction(fl, fl.replace(".jpg", ".xlsx")  ))
            self.button.pack(expand=1,side = LEFT)
            self.id1 = canvas.create_window(250, 200, width=80, height=25,
                                       window=self.button)
            # pass

    def onChange(self):
        self.directory = askdirectory()
        self.entry1.delete(0, END)
        self.entry1.insert(0, self.directory)         
        # cmd = "start excel /home/phong/Documents/NhanDien/BoxDetection/example.xlsx"
        # subprocess.call(cmd, shell=True)
  
root = Tk()
root.title("Version 1.")
menubar = Menu(root)
image= PhotoImage(file='anh2.png')

root.config(menu=menubar)
fileMenu = Menu(menubar)
ex = Example(root)
fileMenu.add_command(label="Open", command=ex.onOpen)

menubar.add_cascade(label="File", menu=fileMenu)

# label = Label(root,bg = image, text = 'Please open your image ', font =( 
#   'Verdana', 18),state = DISABLED).pack(side = TOP, pady = 20) 
# label.place(x=100, y=306)
canvas = Canvas(root,width=500,height=450)
canvas.pack()
canvas.create_image(0,0, anchor=NW,image= image)
text_open = canvas.create_text(30, 150, anchor=W, fill="gold",font="VNI-Dom 18", 
                          text="Please open your file image") 

root.geometry("500x450")
root.mainloop()