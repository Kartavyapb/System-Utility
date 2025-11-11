import base64
import hashlib
import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding

class Passwrd:
    def __init__(self,file_path):
        self.win = Tk()
        self.win.wm_title("Password")
        self.win.geometry('370x200')
        self.win.configure(bg="lightblue")
        self.file_path = file_path

        self.label1 = Label(master=self.win, text="Password",
                            font=('consolas', 8, 'bold'), bg="blue", fg='black')
        self.label1.place(x=20, y=20, width=150, height=30)

        self.label2 = Label(master=self.win, text="Confirm Password",
                            font=('consolas', 8, 'bold'), bg="blue", fg='black')
        self.label2.place(x=20, y=80, width=150, height=30)

        self.enpass1 = Entry(master=self.win, show="*", font=('consolas', 8, 'bold'))
        self.enpass1.place(x=190, y=20, width=160, height=30)

        self.enpass2 = Entry(master=self.win, show="*", font=('consolas', 8, 'bold'))
        self.enpass2.place(x=190, y=80, width=160, height=30)

        self.btnok = Button(master=self.win, text="OK", font=('consolas', 10, 'bold'),command=self.ok_button)
        self.btnok.place(x=60, y=140, width=90, height=30)
        self.win.bind('<Return>', lambda event: self.on_enter())

        self.btncancel = Button(master=self.win, text="Cancel", font=('consolas', 10, 'bold'))
        self.btncancel.place(x=200, y=140, width=90, height=30)

        self.win.mainloop()

    # Generate a key from a password (optional)
    """def generate_key(self,pass1, salt):
        password=pass1
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password)
        return key"""

    """def generate_key_from_password(self, password):
        # Use SHA-256 to hash the password and use the first 32 bytes as the key
        password_hash = hashlib.sha256(password.encode()).digest()
        return base64.urlsafe_b64encode(password_hash[:32])"""

    def ok_button(self):
        pass1=self.enpass1.get()
        pass2=self.enpass2.get()
        if pass1==pass2:
            with open(self.file_path, 'rb') as file:
                data = file.read()
                encrypted_data = self.cipher.encrypt(data)

            encrypted_file_path = self.file_path + ".enc"
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            """# Generate the key from the password
            key = Fernet.generate_key()

            # string the key in a file
            with open('filekey.key', 'wb') as filekey:
                filekey.write(key)

            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()

            # using the generated key
            fernet = Fernet(key)"""

            # opening the original file to encrypt
            """try:
                with open(self.file_path, 'rb') as file:
                    original = file.read()
            except PermissionError:
                print(f"Permission Denied: Unable to read the file {self.file_path}")
            except FileNotFoundError:
                print(f"File Not Found: {self.file_path} does not exist")
            except Exception as e:
                print(f"An error occurred: {e}")"""

            """with open(self.file_path, 'rb') as file:
                original = file.read()

            # encrypting the file
            encrypted = fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open(self.file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)"""

            # Create a Fernet encryption object
            """cipher = Fernet(key)

            # Read the file data
            with open(self.file_path, 'rb') as file:
                file_data = file.read()

            # Encrypt the file data
            encrypted_data = cipher.encrypt(file_data)

            # Write the encrypted data back to the file
            with open(self.file_path, 'wb') as file:
                file.write(encrypted_data)"""


            """salt = os.urandom(16)  # Generate a random salt
            key = self.generate_key(pass1, salt)

            # AES requires the data to be padded to block size
            backend = default_backend()
            iv = os.urandom(16)  # Initialization vector
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
            encryptor = cipher.encryptor()

            # Padding data to block size (16 bytes for AES)
            padder = padding.PKCS7(algorithms.AES.block_size).padder()

            with open(input_file, 'rb') as f:
                plaintext = f.read()

            padded_data = padder.update(plaintext) + padder.finalize()

            ciphertext = encryptor.update(padded_data) + encryptor.finalize()

            # Write salt, iv, and ciphertext to output file
            with open(output_file, 'wb') as f:
                f.write(salt + iv + ciphertext)"""

            messagebox.showinfo("Project Says","Your file is Successfully Encrypted")
        else:
            messagebox.showerror("Project Says","Password and Confirm Password must be Same")

    def on_enter(self):
        self.ok_button()

    def get_data1(self):
        password1 = self.enpass1.get()
        return password1

    def get_data2(self):
        password2 = self.enpass2.get()
        return password2

class Additional(Passwrd):
    def __init__(self):
        self.win = Tk()
        self.win.wm_title("AdditionalTools")
        self.win.geometry('600x400')
        self.win.configure(bg="lightblue")

        self.label1 = Label(master=self.win, text="Additional Tools...                   ", font=('consolas', 18, 'bold'),bg="blue", fg='black')
        self.label1.place(x=10, y=5, width=575, height=50)

        self.btn1 = Button(master=self.win,bg="lightblue")
        self.btn1.place(x=40, y=70, width=500, height=120)

        self.btnbrwen=Button(master=self.win,text="Browse",font=('consolas',12,'bold'),command=self.browse_encry_folder)
        self.btnbrwen.place(x=80,y=90,width=80,height=30)

        self.enfileen=Entry(master=self.win,font=('consolas',12,'bold'))
        self.enfileen.place(x=250,y=90,width=250,height=30)

        self.btnencrp=Button(master=self.win,text="Encryption",font=('consolas',12,'bold'),command=self.encrypt_file)
        self.btnencrp.place(x=380,y=150,width=120,height=30)
        self.win.bind('<Return>', lambda event: self.on_enter_encryption())

        self.label2=Label(master=self.win,text="Output File :",font=('consolas',12,'bold'),bg="lightblue")
        self.label2.place(x=80,y=130,width=120,height=40)

        self.btn2= Button(master=self.win, bg="lightblue")
        self.btn2.place(x=40, y=210, width=500, height=120)

        self.btnbrwde = Button(master=self.win, text="Browse", font=('consolas', 12, 'bold'),command=self.browse_decry_folder)
        self.btnbrwde.place(x=80, y=230, width=80, height=30)

        self.enfilede = Entry(master=self.win, font=('consolas', 12, 'bold'))
        self.enfilede.place(x=250, y=230, width=250, height=30)

        self.btndecrpt = Button(master=self.win, text="Decryption", font=('consolas', 12, 'bold'),command=self.decrypt_file)
        self.btndecrpt.place(x=380, y=290, width=120, height=30)
        self.win.bind('<Return>', lambda event: self.on_enter_decryption())

        self.label3 = Label(master=self.win, text="Output File :", font=('consolas', 12, 'bold'), bg="lightblue")
        self.label3.place(x=80, y=270, width=120, height=40)

        self.btnback = Button(master=self.win, text="Back", font=('consolas', 12, 'bold'),command=self.go_back)
        self.btnback.place(x=40, y=360, width=80, height=30)

        self.btnext = Button(master=self.win, text="Exit", font=('consolas', 12, 'bold'),command=self.exit)
        self.btnext.place(x=420, y=360, width=80, height=30)

        self.win.mainloop()

    def browse_encry_folder(self):
        folder_path = filedialog.askopenfiles()  # Open file dialog to select a folder
        if folder_path:
            self.enfileen.delete(0, tkinter.END)   #Clear the Entry box
            self.enfileen.insert(0, folder_path)  # Insert the selected folder path

    def browse_decry_folder(self):
        folder_path = filedialog.askopenfiles()  # Open file dialog to select a folder
        if folder_path:
            self.enfilede.delete(0, tkinter.END)   #Clear the Entry box
            self.enfilede.insert(0, folder_path)  # Insert the selected folder path

    def encrypt_file(self):
        # Generate the key from the password
        file_path=self.enfileen.get()
        if self.enfileen.get():
                password = Passwrd(file_path)
        else:
            messagebox.showerror("Project Says","Please Select the file First")

    def on_enter_encryption(self):
        self.encrypt_file()

    def decrypt_file(self):
        # Generate the key from the password
        file_path=self.enfilede.get()
        if self.enfilede.get():
                password = Passwrd(file_path)
        else:
            messagebox.showerror("Project Says","Please Select the file First")

    def on_enter_decryption(self):
        self.decrypt_file()

    def go_back(self):
        self.win.destroy()

    def exit(self):
        self.win.quit()

if __name__ == "__main__":
    add=Additional()
