import subprocess
import tkinter
import winreg
from tkinter import *
from tkinter import messagebox


class Performance:
    def __init__(self):
        self.win = Tk()
        self.win.wm_title("SystemPerformance")
        self.win.geometry('600x400')
        self.win.configure(bg="lightblue")

        self.label1 = Label(master=self.win, text="System Performance...             ", font=('consolas', 18, 'bold'),
                            bg="blue", fg='black')
        self.label1.place(x=10, y=5, width=575, height=50)

        self.listbox1 = Listbox(master=self.win, font=('consolas', 12, 'bold'))
        self.listbox1.place(x=20, y=58, width=200, height=250)

        self.listbox2 = Listbox(master=self.win, font=('consolas', 12, 'bold'))
        self.listbox2.place(x=340, y=58, width=200, height=250)

        self.btnrtsft = Button(master=self.win, text=">>", font=('consolas', 12, 'bold'),
                               command=self.transfer_items)
        self.btnrtsft.place(x=250, y=140, width=60, height=30)

        self.btnlftsft = Button(master=self.win, text="<<", font=('consolas', 12, 'bold'),
                                command=self.transfer_itemslft)
        self.btnlftsft.place(x=250, y=200, width=60, height=30)

        self.btninstlst = Button(master=self.win, text="Installed Program List", font=('consolas', 12, 'bold'),
                                 command=self.display_installed_software)
        self.btninstlst.place(x=20, y=325, width=210, height=30)

        self.btnuninstlst = Button(master=self.win, text="Uninstalled Programs", font=('consolas', 12, 'bold'),
                                   command=self.uninstall_softwares)
        self.btnuninstlst.place(x=340, y=325, width=210, height=30)

        self.btnback = Button(master=self.win, text="Back", font=('consolas', 12, 'bold'),command=self.go_back)
        self.btnback.place(x=40, y=365, width=80, height=30)

        self.btnext = Button(master=self.win, text="Exit", font=('consolas', 12, 'bold'), command=self.exit)
        self.btnext.place(x=450, y=365, width=80, height=30)

        self.win.mainloop()

    def get_installed_software(self):
        software_list = []

        # Registry paths for installed 64-bit and 32-bit software
        reg_paths = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion|Uninstall"
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
        self.listbox1.delete(0, tkinter.END)  # Clear the listbox before displaying new results
        installed_software = self.get_installed_software()

        if installed_software:
            for software in sorted(installed_software):
                self.listbox1.insert(tkinter.END, software)
        else:
            self.listbox1.insert(tkinter.END, "No software found")

    def transfer_items(self):
        selected_items = self.listbox1.curselection()

        for index in selected_items[::-1]:
            item = self.listbox1.get(index)
            self.listbox2.insert(tkinter.END, item)

        for index in reversed(selected_items):
            self.listbox1.delete(index)

    def transfer_itemslft(self):
        selected_items = self.listbox2.curselection()

        for index in selected_items[::-1]:
            item = self.listbox2.get(index)
            self.listbox1.insert(tkinter.END, item)

        for index in reversed(selected_items):
            self.listbox2.delete(index)

    def uninstall_softwares(self):
        selected_software = self.listbox2.get(tkinter.ACTIVE)
        if selected_software:
            response = messagebox.askyesno("Uninstall", f"Are you sure you want to uninstall {selected_software}?")
            if response:
                try:
                    # Uninstall software using WMIC command
                    subprocess.run(f"wmic product where name='{selected_software}' call uninstall", shell=True,check=True)
                    messagebox.showinfo("Success", f"{selected_software} has been uninstalled successfully.")
                except subprocess.CalledProcessError:
                    messagebox.showerror("Error", f"Failed to uninstall {selected_software}.")
        else:
            messagebox.showwarning("No selection", "Please select a software to uninstall.")

    def go_back(self):
        self.win.destroy()

    def exit(self):
        self.win.quit()


if __name__ == "__main__":
    perform = Performance()












"""
import tkinter as tk
from tkinter import Listbox, Button


# Function to transfer selected items from one listbox to another
def transfer_items():
    # Get selected items from source Listbox
    selected_items = source_listbox.curselection()
    for i in selected_items:
        # Get the actual value from the source listbox
        item = source_listbox.get(i)
        # Insert the selected item into the destination listbox
        destination_listbox.insert(tk.END, item)

    # Optional: Remove the transferred items from the source Listbox
    for i in reversed(selected_items):  # Reverse to avoid index shifting issue
        source_listbox.delete(i)


# Create the main window
root = tk.Tk()
root.title("Transfer Items Between Listboxes")

# Source Listbox (Installed Software)
source_listbox = Listbox(root, selectmode=tk.MULTIPLE)
source_listbox.grid(row=0, column=0, padx=10, pady=10)

# Add some example items to the source listbox
installed_software = ['Software 1', 'Software 2', 'Software 3', 'Software 4']
for software in installed_software:
    source_listbox.insert(tk.END, software)

# Button to transfer items
transfer_button = Button(root, text="Transfer", command=transfer_items)
transfer_button.grid(row=0, column=1, padx=10, pady=10)

# Destination Listbox (Transferred Software)
destination_listbox = Listbox(root)
destination_listbox.grid(row=0, column=2, padx=10, pady=10)

# Run the application
root.mainloop()
"""
