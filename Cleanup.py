import os
from tkinter import *
from tkinter import messagebox
class Cleanup:
    def __init__(self):
        self.win = Tk()
        self.win.wm_title("CleanUpWindow")
        self.win.geometry('600x400')
        self.win.configure(bg="lightblue")

        self.label1 = Label(master=self.win, text="Clean Up Window...                   ", font=('consolas', 18, 'bold'),bg="blue", fg='black')
        self.label1.place(x=10, y=5, width=575, height=50)

        self.btnrcycl=Button(master=self.win,text="Clean Recyclebin",font=('consolas',14,'bold'),command=self.delete_confirmation)
        self.btnrcycl.place(x=60,y=100,width=200,height=60)

        self.btntemp=Button(master=self.win,text="Clean Temporary\nFile",font=('consolas',14,'bold'),command=self.temp_delete_confirmation)
        self.btntemp.place(x=300,y=100,width=200,height=60)

        #messagebox.showwarning("Confirm Multiple File Delete", "Are you sure you want to delete these 6 items?")


        self.win.mainloop()

    def delete_confirmation(self):
        #recycle_items = list(winshell.recycle_bin())
        #items_count=len(recycle_items)
        response = messagebox.askyesno("Confirm Multiple File Delete", "Are you sure you want to delete these items?")
        if response:
            self.clean_bin()
            #messagebox.showinfo("Success", "Recycle Bin Cleaned Successfully")
        else:
            self.win.quit()
            #messagebox.showerror("Error", f"Failed to clean Recycle Bin:{e}")

    def clean_bin(self):
        try:
            os.system("rd /s /q C:\\$Recycle.Bin")
            messagebox.showinfo("Success", "Recycle Bin Cleaned Successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clean Recycle Bin:{e}")

    def temp_delete_confirmation(self):
        response = messagebox.askyesno("Confirm Multiple File Delete", "Are you sure you want to delete these items?")
        if response:
            self.clean_temp_files()
        else:
            self.win.quit()
    def clean_temp_files(self):
        try:
            os.system("del /q/f/s %TEMP%\\*")
            messagebox.showinfo("Success","Temporary Files Cleaned Successfully!")
        except Exception as e:
            messagebox.showerror("Error",f"Failed to clean temp files:{e}")



if __name__ =="__main__":
    clean=Cleanup()











"""
import ctypes
import tkinter as tk
from tkinter import messagebox

# Define constants for SHEmptyRecycleBin
SHERB_NOCONFIRMATION = 0x00000001  # Don't ask for confirmation
SHERB_NOPROGRESSUI = 0x00000002    # No progress dialog
SHERB_NOSOUND = 0x00000004         # Don't make sound

# Function to delete all Recycle Bin items using ctypes
def delete_recycle_bin_items():
    try:
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all items in the Recycle Bin?")
        if confirm:
            # Call SHEmptyRecycleBin from shell32.dll to empty the recycle bin
            result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)
            if result == 0:  # If result is 0, the operation succeeded
                messagebox.showinfo("Success", "All items in the Recycle Bin have been deleted.")
            else:
                messagebox.showerror("Error", f"Failed to empty Recycle Bin. Error code: {result}")
        else:
            messagebox.showinfo("Cancelled", "Recycle Bin cleaning was cancelled.")
    except Exception as e:
        messagebox.showerror("Error", f"Error while emptying Recycle Bin: {e}")

# Set up Tkinter window
root = tk.Tk()
root.title("Recycle Bin Cleaner")
root.geometry("300x200")

# Label for instructions
label = tk.Label(root, text="Delete all Recycle Bin items", font=("Helvetica", 14))
label.pack(pady=20)

# Button to delete Recycle Bin items
btn_delete_items = tk.Button(root, text="Delete All Items", command=delete_recycle_bin_items, bg="red", fg="white")
btn_delete_items.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""
