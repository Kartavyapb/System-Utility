from datetime import datetime
from tkinter import *
from pymysql import *
from tkinter import messagebox
import SystemUtlt

class Login:
    def __init__(self):
        self.win = Tk()
        self.win.wm_title("Form1")
        self.win.geometry('600x400')
        self.win.configure(bg="lightblue")

        self.label1=Label(master=self.win,text="Welcome",font=('consolas',16,'bold'),bg="lightblue",fg='black')
        self.label1.place(x=260,y=20,width=90,height=20)

        self.label2 = Label(master=self.win, text="System Utility 2024", font=('consolas', 16, 'bold'),bg="lightblue",fg='black')
        self.label2.place(x=150, y=50, width=300, height=20)

        self.label3 = Label(master=self.win,text="User ID",font=('consolas',12,'bold'),bg="lightblue",fg='black')
        self.label3.place(x=100,y=120,width=90,height=30)

        self.label4 = Label(master=self.win,text="Password",font=('consolas',12,'bold'),bg="lightblue",fg='black')
        self.label4.place(x=100,y=200,width=90,height=30)

        current_date=datetime.now().strftime("%A,%Y-%m-%d")
        self.label5 = Label(master=self.win,text=current_date,font=('consolas',8,'bold'),bg="lightblue",fg='black')
        self.label5.place(x=10,y=30,width=120,height=15)

        current_time=datetime.now().strftime("%I:%M:%S %p")
        self.label6 = Label(master=self.win,text=current_time,font=('consolas',8,'bold'),bg="lightblue",fg='black')
        self.label6.place(x=10,y=55,width=100,height=15)

        self.enuserid = Entry(master=self.win,font=('consolas',12,'bold'),fg='black')
        self.enuserid.place(x=250,y=120,width=150,height=30)

        self.enpass = Entry(master=self.win,show="*",font=('consolas',12,'bold'),fg='black')
        self.enpass.place(x=250,y=200,width=150,height=30)

        self.btnlgn = Button(master=self.win,text="LOGIN",font=('consolas',12,'bold'),command=self.login)
        self.btnlgn.place(x=100,y=300,width=80,height=30)
        self.win.bind('<Return>', lambda event: self.on_enter())

        self.btnext = Button(master=self.win,text="EXIT",font=('consolas',12,'bold'),command=self.exit)
        self.btnext.place(x=320,y=300,width=80,height=30)


        self.win.mainloop()

    def connectToDB(self):
        self.row = 0
        self.conn = connect(host='localhost', port=3306, user='root',
                            password='sa123', db='ISPDB')
        self.cur = self.conn.cursor()
        self.checkData()
        self.win.quit()

    def checkData(self):
        self.name=self.enuserid.get()
        self.passwrd=self.enpass.get()
        qry = "select * from Login where name='"+self.name+"' and pass='"+self.passwrd+"';"
        n=self.cur.execute(qry)
        self.data = self.cur.fetchall()

        if(n>0):
            messagebox.showinfo("Project Says","Valid Login")
            system = SystemUtlt.System()
            self.win.quit()
        else:
            messagebox.showerror("Project Says","Invalid Login")

    def login(self):
        self.connectToDB()

    def on_enter(self):
        self.connectToDB()


    def exit(self):
        self.win.quit()


if __name__ == "__main__":
    login=Login()


