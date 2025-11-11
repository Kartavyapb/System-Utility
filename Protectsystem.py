import msvcrt
import os
import time
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk

from pack_pythonproject.Passwordprotect import Password


class Protect:
    def __init__(self):
        self.win = Tk()
        self.win.wm_title("ProtectSystem")
        self.win.geometry('600x400')
        self.win.configure(bg="lightblue")

        """image_path = "lock_open_image.png"  # Change this to the actual image file path
        image = Image.open(image_path)
        image = image.resize((50, 50))  # Resize the image (if needed)
        lock_image = ImageTk.PhotoImage(image)
        self.image_label = Label(master=self.win, image=lock_image)
        self.image_label.place(x=450, y=140)"""

        self.label1 = Label(master=self.win, text="Protect System...                   ", font=('consolas', 18, 'bold'),bg="blue", fg='black')
        self.label1.place(x=10, y=5, width=575, height=50)

        self.btn1 = Button(master=self.win, text="Select to Lock...",anchor="nw",width=40,height=4,font=('consolas',12,'bold','underline'), bg="lightblue")
        self.btn1.place(x=40, y=90, width=350, height=150)

        self.rdwinlk = tkinter.BooleanVar(value=False)
        self.rdwinlk=Radiobutton(master=self.win,text="Window Lock",font=('consolas',12,'bold'),bg="lightblue",command=self.lock_file)
        self.rdwinlk.place(x=180,y=180,width=150,height=30)

        self.label2=Label(master=self.win,text="Folder Status",bg="lightblue")
        self.label2.place(x=450,y=60,width=70,height=30)

        self.label3=Label(master=self.win,text="Choose Folder",font=('consolas',12,'bold'),bg="lightblue")
        self.label3.place(x=30,y=270,width=120,height=30)

        self.enname=Entry(master=self.win,font=('consolas',12,'bold'))
        self.enname.place(x=170,y=270,width=250,height=30)

        self.btnbrws=Button(master=self.win,text="Browse",font=('consolas',12,'bold'),command=self.browse_folder)
        self.btnbrws.place(x=440,y=270,width=120,height=30)

        self.set_password_var = tkinter.BooleanVar()
        self.ckpass=Checkbutton(master=self.win,text="Set Password",bg="lightblue",variable=self.set_password_var)
        self.ckpass.place(x=460,y=310,width=140,height=30)

        self.btnback = Button(master=self.win, text="Back", font=('consolas', 12, 'bold'),command=self.go_back)
        self.btnback.place(x=40, y=350, width=80, height=30)

        self.btnext = Button(master=self.win, text="Exit", font=('consolas', 12, 'bold'),command=self.exit)
        self.btnext.place(x=420, y=350, width=80, height=30)

        self.win.mainloop()

    def browse_folder(self):
        folder_path = filedialog.askdirectory()  # Open file dialog to select a folder
        if folder_path:
            self.enname.delete(0, tkinter.END)   #Clear the Entry box
            self.enname.insert(0, folder_path)

    """def is_file_being_modified(self,filepath):
        initial_stats = os.stat(filepath)
        time.sleep(1)  # Wait for a second and check again
        current_stats = os.stat(filepath)

        if initial_stats.st_mtime != current_stats.st_mtime:
            return True  # File is being modified (possibly locked)

        return False  # No modification detected (might not be locked)
    """

    def is_file_locked(self,filepath):
        try:
            # Attempt to open the file in read/write mode ('r+')
            with open(filepath, 'r+'):
                pass  # File is not locked
            return False  # File is not locked
        except (OSError, IOError):
            return True  # File is locked or inaccessible

    def lock_file(self):
        file_path = self.enname.get()  # Get the selected file path
        if not file_path:
            messagebox.showwarning("Warning", "No file selected!")
            return
        else:
            if self.is_file_locked(file_path):
                image_path = "lock_image.png"  # Change this to the actual image file path
                image = Image.open(image_path)
                image = image.resize((50, 50))  # Resize the image (if needed)
                lock_image = ImageTk.PhotoImage(image)
                self.image_label = Label(master=self.win, image=lock_image)
                self.image_label.place(x=450, y=140)
                messagebox.showinfo("Project Says","Your file is already Locked")
            else:
                if self.set_password_var.get():
                    image_path = "lock_open_image.png"  # Change this to the actual image file path
                    image = Image.open(image_path)
                    image = image.resize((50, 50))  # Resize the image (if needed)
                    lock_image = ImageTk.PhotoImage(image)
                    self.image_label = Label(master=self.win, image=lock_image)
                    self.image_label.place(x=450, y=140)
                    password = Password(file_path)
                else:
                    messagebox.showinfo("Status", "Checkbox is not checked.")


    """def lock_file_path(self,file_path, password=None):
        folder, filename = os.path.split(file_path)
        if password:
            locked_filename = f"locked_{filename}_pwd{password}.lock"
        else:
            locked_filename = f"locked_{filename}.lock"

        new_file_path = os.path.join(folder, locked_filename)

        try:
            os.rename(file_path, new_file_path)
            messagebox.showinfo("Success", f"File locked successfully as {locked_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Error locking the file: {e}")

    def toggle_password_entry(self):
        if self.set_password_var.get():
            pass
            #password_entry.config(state=tkinter.NORMAL)
        else:
            pass
            #password_entry.config(state=tkinter.DISABLED)
    """
    def go_back(self):
        self.win.destroy()
    def exit(self):
        self.win.quit()


if __name__ == "__main__":
    protect=Protect()



"""
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to browse a file
def browse_file():
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)  # Clear current entry
    entry.insert(0, file_path)  # Insert selected file path

# Function to lock the file
def lock_file():
    file_path = entry.get()  # Get the selected file path
    if not file_path:
        messagebox.showwarning("Warning", "No file selected!")
        return

    # Check if password is required
    if set_password_var.get():
        password = password_entry.get()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password!")
            return
    else:
        password = None

    # Simulate file locking by renaming the file
    if window_lock_var.get():
        lock_file_path(file_path, password)

# Function to "lock" the file by renaming it
def lock_file_path(file_path, password=None):
    folder, filename = os.path.split(file_path)
    if password:
        locked_filename = f"locked_{filename}_pwd{password}.lock"
    else:
        locked_filename = f"locked_{filename}.lock"

    new_file_path = os.path.join(folder, locked_filename)

    try:
        os.rename(file_path, new_file_path)
        messagebox.showinfo("Success", f"File locked successfully as {locked_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error locking the file: {e}")

# Create the main window
root = tk.Tk()
root.title("Protect System")

# Create the window lock radio button
window_lock_var = tk.BooleanVar(value=False)
radio_btn = tk.Radiobutton(root, text="Window Lock", variable=window_lock_var, value=True, command=lock_file)
radio_btn.pack(pady=10)

# Entry to display selected file
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Browse button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Set password checkbox
set_password_var = tk.BooleanVar()
set_password_check = tk.Checkbutton(root, text="Set password", variable=set_password_var)
set_password_check.pack(pady=5)

# Password entry field (disabled initially)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)
password_entry.config(state=tk.DISABLED)

# Enable password entry field only when checkbox is checked
def toggle_password_entry():
    if set_password_var.get():
        password_entry.config(state=tk.NORMAL)
    else:
        password_entry.config(state=tk.DISABLED)

set_password_check.config(command=toggle_password_entry)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
"""