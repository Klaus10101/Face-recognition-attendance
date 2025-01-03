from attendance import *
from Detector import main_app
from create_classifier import train_classifer
from create_dataset import start_capture
import tkinter as tk
from tkinter import font as tkfont
from tkinter import PhotoImage
import subprocess
import time
import box
# import cv2
names = set()
l=list(names)

class MainUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global names
        with open("nameslist.txt", "r") as f:
            x = f.read()
            z = x.rstrip().split(" ")
            for i in z:
                names.add(i)
        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.title("Face Recognition Attendance System")
        self.resizable(False, False)
        self.geometry("500x300")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.active_name = None
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, AttendancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

    def on_closing(self):

        if box.askokcancel("Quit", "Are you sure?"):
            global names
            # f =  open("nameslist.txt", "w")
            # for i in names:
            #         f.write(i+" ")
            self.destroy()


class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
         
            render = PhotoImage(file='homepagepic.png')
            img = tk.Label(self, image=render)
            img.image = render
            img.grid(row=1, column=1, rowspan=5, sticky="nsew")
            label = tk.Label(self, text="        Home Page        ", font=self.controller.title_font,fg="#263942")
            label.grid(row=0, sticky="ew")
            button1 = tk.Button(self, text="   Register  ", fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageOne"))
            button2 = tk.Button(self, text="   Check a User  ", fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageTwo"))
            button3 = tk.Button(self, text="   Attendance  ", fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("AttendancePage"))
            button4 = tk.Button(self, text="About", fg="#263942", bg="#ffffff", command=self.on_closing)
            button1.grid(row=1, column=0, ipady=3, ipadx=15, pady=15)
            button2.grid(row=2, column=0, ipady=3, ipadx=4, pady=15)
            button3.grid(row=3, column=0, ipady=3, ipadx=10, pady=15)
            button4.grid(row=4, column=0, ipady=3, ipadx=32, pady=15)


        def on_closing(self):
            box.showinfo("About", "Creators :\t\n Rohan\n Raviyansh\n Sarthak\n Uttkarsh")
               

class AttendancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        render = PhotoImage(file='a.png')
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=4, rowspan=17, padx=150,pady=50)
        label = tk.Label(self, text=" Attendance", font=self.controller.title_font,fg="#263942")
        label.grid(row=0, column=1, pady=2, padx=7)

        self.button1 = tk.Button(self, text="Mark Attendance", fg="#ffffff", bg="#263942",command=self.mark_attendance)
        self.button2 = tk.Button(self, text="Show Attendance", fg="#ffffff", bg="#263942",command=self.show_attendance)
        self.button3 = tk.Button(self, text="<-", fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("StartPage"))
          
        self.button1.grid(row=3, column=1, ipady=2, ipadx=5, pady=48)
        self.button2.grid(row=5, column=1, ipady=5, ipadx=5, pady=5)
        self.button3.grid(row=0, column=0,ipady=0, ipadx=0)
    def show_attendance(self):
            if box.askokcancel("Excel", "wanna open excel"):
                try:
                    subprocess.Popen([r"C:\Program Files\LibreOffice\program\scalc.exe",r"C:\Users\DELL\Documents\project_12_A-1\att.csv"])
                except:
                    box.showinfo("something went wrong !!!")

    def attendance_mark_succesfuly(self):
        box.showinfo("Attendance", "Atendance marked successfully")
            


    def mark_attendance(self):
        stu()                          #_______
        present()                      #-------| ye function attendance.py mei se import kiye hain
        self.attendance_mark_succesfuly() 
        add()                       #___|
        
    




class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        

        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="Enter the name", fg="#263942", font='Helvetica 12 bold').grid(row=0, column=0, pady=10, padx=5)
        self.user_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.user_name.grid(row=0, column=1, pady=10, padx=10)
        self.buttoncanc = tk.Button(self, text="Cancel", bg="#ffffff", fg="#263942", command=lambda: controller.show_frame("StartPage"))
        self.buttonext = tk.Button(self, text="Next", fg="#ffffff", bg="#263942", command=self.start_training)
        self.buttoncanc.grid(row=2, column=0, pady=30, ipadx=2, ipady=4)
        self.buttonext.grid(row=2, column=1, pady=30, ipadx=2, ipady=4)

    def start_training(self):
        global names
        
        if self.user_name.get() == "None":
            box.showerror("Error", "Name cannot be 'None'")
            return
        elif self.user_name.get() in names:
            box.showerror("Error", "User already exists!")
            return
        elif len(self.user_name.get()) == 0:
            box.showerror("Error", "Name cannot be empty!")
            return
        name = self.user_name.get()
        names.add(name)
        with open("nameslist.txt", "a") as f:
                    f.write(name+" ")

        self.controller.active_name = name
        self.controller.frames["PageTwo"].refresh_names()
        self.controller.show_frame("PageThree")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global names
        self.controller = controller
        tk.Label(self, text="Select user", fg="#263942", font='Helvetica 12 bold').grid(row=0, column=0, padx=10, pady=10)
        self.buttoncanc = tk.Button(self, text="Cancel", command=lambda: controller.show_frame("StartPage"), bg="#ffffff", fg="#263942")
        self.menuvar = tk.StringVar(self)
        self.dropdown = tk.OptionMenu(self, self.menuvar, *names)
        self.dropdown.config(bg="lightgrey")
        self.dropdown["menu"].config(bg="lightgrey")
        self.buttonext = tk.Button(self, text="Next", command=self.nextfoo, fg="#ffffff", bg="#263942")
        self.dropdown.grid(row=0, column=1, ipadx=8, padx=10, pady=10)
        self.buttoncanc.grid(row=1, ipadx=5, ipady=4, column=0, pady=10)
        self.buttonext.grid(row=1, ipadx=5, ipady=4, column=1, pady=10)

    def nextfoo(self):
        if self.menuvar.get() == "None":
            box.showerror("ERROR", "Name cannot be 'None'")
            return
        self.controller.active_name = self.menuvar.get()
        self.controller.show_frame("PageFour")

    def refresh_names(self):
        global names
        self.menuvar.set('')
        self.dropdown['menu'].delete(0, 'end')
        for name in names:
            self.dropdown['menu'].add_command(label=name, command=tk._setit(self.menuvar, name))

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.numimglabel = tk.Label(self, text="Number of images captured = 0", font='Helvetica 12 bold', fg="#263942")
        self.numimglabel.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)
        self.capturebutton = tk.Button(self, text="Capture Data Set", fg="#ffffff", bg="#263942", command=self.capimg)
        self.trainbutton = tk.Button(self, text="Train The Model", fg="#ffffff", bg="#263942",command=self.trainmodel)
        self.capturebutton.grid(row=1, column=0, ipadx=5, ipady=4, padx=10, pady=20)
        self.trainbutton.grid(row=1, column=1, ipadx=5, ipady=4, padx=10, pady=20)

    def capimg(self):
        self.numimglabel.config(text=str("Captured Images = 0 "))
        box.showinfo("INSTRUCTIONS", "We will Capture 10 pic of your Face.\n please turn your head in all directions one by one")
        x = start_capture(self.controller.active_name)
        self.controller.num_of_images = x
        self.numimglabel.config(text=str("Number of images captured = "+str(x)))

    def trainmodel(self):
        if self.controller.num_of_images < 150:
            box.showerror("ERROR", "No enough Data, Capture at least 100 images!")
            return
        train_classifer(self.controller.active_name)
        box.showinfo("SUCCESS", "The modele has been successfully trained!")
        self.controller.show_frame("PageFour")


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Face Recognition", font='Helvetica 16 bold')
        label.grid(row=0,column=0, sticky="ew")
        button1 = tk.Button(self, text="Face Recognition", command=self.openwebcam , fg="#ffffff", bg="#263942")
        
        button4 = tk.Button(self, text="Go to Home Page", command=lambda: self.controller.show_frame("StartPage"), bg="#ffffff", fg="#263942")
        button1.grid(row=1,column=0, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
       
        button4.grid(row=1,column=1, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)

    def openwebcam(self):
        box.showinfo("info","enter \"Esc\" to quit the camera window !! ")

        main_app(self.controller.active_name)
        return True
    

if __name__ == "__main__":
    app = MainUI()
    app.iconphoto(False, tk.PhotoImage(file='icon.ico'))
    app.mainloop()

