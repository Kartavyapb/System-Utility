from tkinter import *

from pack_pythonproject.Additionaltool import Additional
from pack_pythonproject.Cleanup import Cleanup
from pack_pythonproject.Customizewin import Customize
from pack_pythonproject.Protectsystem import Protect
from pack_pythonproject.Systemperfom import Performance


class System:
    def __init__(self):
        self.win = Tk()
        self.win.wm_title("Utility_System")
        self.win.geometry('600x400')
        self.win.configure(bg="lightblue")

        self.label1=Label(master=self.win,text="System Utility 2010",font=('consolas',18,'bold'),bg="blue",fg='black')
        self.label1.place(x=10,y=5,width=575,height=50)

        self.btn1=Button(master=self.win,text="",bg="lightblue")
        self.btn1.place(x=40,y=90,width=510,height=250)

        self.btncutwin=Button(master=self.win, text="Customize Windows", font=('consolas',12,'bold'), command=self.custwin)
        self.btncutwin.place(x=200,y=110,width=200,height=30)

        self.btnemtbn=Button(master=self.win,text="Empty RecycleBin",font=('consolas',12,'bold'),command=self.clean)
        self.btnemtbn.place(x=80,y=180,width=200,height=30)

        self.btnincper = Button(master=self.win, text="Increase Performance", font=('consolas', 12, 'bold'),command=self.performance)
        self.btnincper.place(x=300, y=180, width=200, height=30)

        self.btnprtstm = Button(master=self.win, text="Protect System", font=('consolas', 12, 'bold'),command=self.prtsystm)
        self.btnprtstm.place(x=80, y=260, width=200, height=30)

        self.btnadtl = Button(master=self.win, text="Additional Tools", font=('consolas', 12, 'bold'),command=self.addtool)
        self.btnadtl.place(x=300, y=260, width=200, height=30)

        self.btnabout=Button(master=self.win,text="About",font=('consolas',12,'bold'))
        self.btnabout.place(x=100,y=355,width=80,height=30)

        self.btnext=Button(master=self.win,text="Exit",font=('consolas',12,'bold'),command=self.exit)
        self.btnext.place(x=380,y=355,width=80,height=30)

        self.win.mainloop()

    def custwin(self):
        customize = Customize()

    def prtsystm(self):
        protect = Protect()

    def addtool(self):
        add = Additional()

    def clean(self):
        clean = Cleanup()

    def performance(self):
        perform = Performance()

    def exit(self):
        self.win.quit()


if __name__ == "__main__":
    system=System()
