import os
import subprocess
import tkinter
import winreg
from tkinter import *
from tkinter import filedialog


class Customize:
    def __init__(self):
        self.win = Tk()
        self.win.wm_title("CustomizeWindow")
        self.win.geometry('600x400')
        self.win.configure(bg="lightblue")

        self.label1 = Label(master=self.win, text="Customize Window...             ", font=('consolas', 18, 'bold'), bg="blue",fg='black')
        self.label1.place(x=10, y=5, width=575, height=50)

        self.btn1 = Button(master=self.win, text="", bg="lightblue")
        self.btn1.place(x=40, y=90, width=510, height=200)

        self.btnwinexpl = Button(master=self.win, text="Windows Explorer", font=('consolas', 12, 'bold'),command=self.open_wind_explorer)
        self.btnwinexpl.place(x=80, y=120, width=200, height=50)

        self.btnfndsftwr = Button(master=self.win, text="Find Software", font=('consolas', 12, 'bold'),command=self.find_software)
        self.btnfndsftwr.place(x=300, y=120, width=200, height=50)

        self.btncngdttm = Button(master=self.win, text="Changing Date / Time", font=('consolas', 12, 'bold'),command=self.change_date_time)
        self.btncngdttm.place(x=160, y=200, width=250, height=50)

        self.btnback = Button(master=self.win, text="Back", font=('consolas', 12, 'bold'),command=self.go_back)
        self.btnback.place(x=100, y=330, width=80, height=30)

        self.btnext = Button(master=self.win, text="Exit", font=('consolas', 12, 'bold'),command=self.exit)
        self.btnext.place(x=380, y=330, width=80, height=30)

        self.win.mainloop()



    def open_wind_explorer(self):
        folder_path = filedialog.askdirectory()
        if folder_path:  # Check if the user selected a folder
            os.startfile(folder_path)

    def change_date_time(self):
        subprocess.run("timedate.cpl", shell=True)

    def get_installed_software(self):
        software_list = []

        # Registry paths for installed 64-bit and 32-bit software
        reg_paths = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ]

        # Access the registry and gather installed software
        for reg_path in reg_paths:
            try:
                reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
                for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
                    try:
                        sub_key_name = winreg.EnumKey(reg_key, i)
                        sub_key = winreg.OpenKey(reg_key, sub_key_name)
                        software_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                        software_list.append(software_name)
                    except FileNotFoundError:
                        pass  # If no DisplayName, skip
                    except EnvironmentError:
                        pass  # Continue if other issues occur
            except FileNotFoundError:
                pass

        return software_list

    def display_installed_software(self):
        self.result_list.delete(0, tkinter.END)  # Clear the listbox before displaying new results
        installed_software = self.get_installed_software()

        if installed_software:
            for software in sorted(installed_software):
                self.result_list.insert(tkinter.END, software)
        else:
            self.result_list.insert(tkinter.END, "No software found")

    def find_software(self):
        root = tkinter.Tk()
        root.title("Installed Software")
        root.geometry("500x400")

        # Create and place a button to display installed software
        self.search_button = tkinter.Button(root, text="Show Installed Software", command=self.display_installed_software)
        self.search_button.pack(pady=10)

        # Create a Listbox to display the results
        self.result_list = tkinter.Listbox(root, width=60, height=20)
        self.result_list.pack(pady=10)

        # Run the Tkinter event loop
        root.mainloop()

    def go_back(self):
        self.win.destroy()
    def exit(self):
        self.win.quit()

if __name__ == "__main__":
    customize=Customize()