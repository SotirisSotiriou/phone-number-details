
from pydoc import describe
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font

from pytz import timezone

import phone_details


class App():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.w1.title('Phone Number Details')
        self.label1 = Label(self.w1, text = "Phone Number", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 16, weight = "normal"), cursor = "arrow", state = "normal")
        self.label1.place(x = 150, y = 70, width = 190, height = 22)
        self.button1 = Button(self.w1, text = "Show", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal", command=self.show_details)
        self.button1.place(x = 200, y = 160, width = 90, height = 42)
        self.ltext1 = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.ltext1.place(x = 130, y = 110, width = 220, height = 32)
        self.text2 = Text(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.text2.place(x = 90, y = 240, width = 320, height = 150)

    def show_details(self):
        self.text2.delete(1.0,"end")
        tz, car, description, valid, possible = phone_details.getDetails(self.ltext1.get())
        timezoneStr = "".join(tz)
        self.text2.insert(1.0,"Timezone: "+timezoneStr)
        self.text2.insert("end","\n"+"Carrier: "+car)
        self.text2.insert("end","\n"+"Description: "+description)
        self.text2.insert("end","\n"+"Valid: "+str(valid))
        self.text2.insert("end","\n"+"Possible: "+str(possible))


class Home():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#8a8a8a')
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#8a8a8a')
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.button1 = Button(self.w1, text = "GO", bg = "#2c2c2c", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal", command=self.show_app)
        self.button1.place(x = 205, y = 234, width = 90, height = 42)
        self.label1 = Label(self.w1, text = "Phone Details", bg = "#8a8a8a", fg = "#ffffff", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 16), cursor = "arrow", state = "normal")
        self.label1.place(x = 160, y = 160, width = 210, height = 22)

    def show_app(self):
        self.w1.destroy()
        app = App(0)
        app.w1.mainloop()

a = Home(0)
a.w1.mainloop()

