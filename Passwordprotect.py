import base64
import hashlib
import os
import tkinter
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk
from cryptography.fernet import Fernet



class Password:
    def __init__(self,file_path):
        self.file_path=file_path
        self.win = Tk()
        self.win.wm_title("Password")
        self.win.geometry('370x200')
        self.win.configure(bg="lightblue")

        self.label1=Label(master=self.win,text="Enter the Password",
                          font=('consolas', 8, 'bold'),bg="blue", fg='black')
        self.label1.place(x=20,y=20,width=150,height=30)

        self.label2=Label(master=self.win,text="Re-Enter Password",
                          font=('consolas', 8, 'bold'),bg="blue", fg='black')
        self.label2.place(x=20,y=80,width=150,height=30)

        self.enpass1=Entry(master=self.win,show="*",font=('consolas',8,'bold'))
        self.enpass1.place(x=190,y=20,width=160,height=30)

        self.enpass2=Entry(master=self.win,show="*",font=('consolas',8,'bold'))
        self.enpass2.place(x=190,y=80,width=160,height=30)

        self.btnsbmt=Button(master=self.win,text="Submit",font=('consolas', 10, 'bold'),command=self.submit_password)
        self.btnsbmt.place(x=150,y=140,width=90,height=30)
        self.win.bind('<Return>', lambda event: self.on_enter())

        self.win.mainloop()

    """def generate_key_from_password(self,password):
        # Use SHA-256 to hash the password and use the first 32 bytes as the key
        password_hash = hashlib.sha256(password.encode()).digest()
        return base64.urlsafe_b64encode(password_hash[:32])

    # Function to encrypt the file
    def encrypt_file(self,file_path, password):
        # Generate the key from the password
        key = set.generate_key_from_password(password)

        # Create a Fernet encryption object
        cipher = Fernet(key)

        # Read the file data
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Encrypt the file data
        encrypted_data = cipher.encrypt(file_data)

        # Write the encrypted data back to the file
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

        messagebox.showinfo("Project Says",f"The file '{file_path}' has been locked with the password.")
    """

    def lock_file_path(self,file_path, password):
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

    def submit_password(self):
        password1 = self.enpass1.get()
        password2 = self.enpass2.get()
        if password1==password2:
            password=password1
            self.lock_file_path(self.file_path, password)
        else:
            messagebox.showerror("Project Says","Password and Re-entered Password must be same")

    def on_enter(self):
        self.submit_password()



if __name__ == "__main__":
    password=Password()