# 🖥️ System Utility Application
## 📘 Overview
The System Utility Application is a user-friendly desktop tool built with Python (Tkinter) that helps users enhance system performance, security, and customization — all in one place.
It provides a collection of system management tools such as:

* Cleaning unnecessary files and Recycle Bin
* Managing installed programs
* Protecting and encrypting files
* Customizing Windows settings
* Monitoring and improving system performance. <br><br>
This project aims to make system maintenance faster, more efficient, and secure without the need for multiple third-party applications.

## 🚀 Introduction
In today’s digital world, system performance and data security are crucial.
Over time, systems get cluttered with temporary files, unnecessary software, and performance bottlenecks.

To tackle these issues, System Utility Application acts as an all-in-one solution that helps users:
* Clean and optimize system resources
* Uninstall unwanted applications
* Protect and encrypt important data
* Customize and manage system settings effortlessly.<br><br>
With its intuitive Tkinter-based GUI, even non-technical users can maintain their systems with ease.

## ⚙️ Features
* Login System        :-      Secure login interface with validation and database support (using PyMySQL). 
* Dashboard	Central   :-      control panel to access all system utilities.
* Customize Window	  :-      Manage Explorer, find software, change date/time, etc.
* System Performance  :-      View and uninstall installed programs to boost performance.
* Protect System	    :-      Lock folders and files with passwords for security.
* Additional Tools	  :-      Encrypt and decrypt files using the Cryptography library.
* Clean Up Utility	  :-      Delete temporary files and empty the Recycle Bin safely.
* User-Friendly UI	  :-      Easy navigation, tooltips, and modern layout using Tkinter.

## 🧰 Tech Stack & Libraries

#### Programming Language:
Python 🐍

#### Libraries Used:
* tkinter → For GUI design
* os, subprocess → For system operations
* datetime → For displaying date and time
* pymysql → For user login database
* tkinter.messagebox → For alert and confirmation dialogs
* tkinter.filedialog → For file selection dialogs
* cryptography.fernet → For file encryption/decryption
* winreg → For accessing Windows registry to list installed software.

## 🗂️ Project Structure
System-Utility/ <br>
│<br>
├── login.py                <br>
├── dashboard.py            <br>
├── customize_window.py     <br>
├── system_performance.py   <br>
├── protect_system.py       <br>
├── additional_tools.py     <br>
├── cleanup_window.py       <br>
├── assets/                 <br>
└── README.md               <br>

## 🪟 GUI Modules Overview

#### 🧩 1. Login Interface
* Accepts User ID and Password
* Displays real-time date & time
* Uses messagebox for success/error alerts
* Can connect to a MySQL database for authentication <br>
<img width="741" height="536" alt="Image" src="https://github.com/user-attachments/assets/05f5c514-6de5-431d-ae2b-33e777058650" />

#### 🖥️ 2. Dashboard
* Acts as the main control panel
* Buttons for:
    * Customize Window
    * System Performance
    * Protect System
    * Additional Tools
    * Clean Up Window
    * About & Exit <br>
<img width="749" height="541" alt="Image" src="https://github.com/user-attachments/assets/bdae015d-9093-44ff-b0a8-3f1f4e6f7898" />

#### ⚙️ 3. Customize Window
* Open Windows Explorer
* Find installed software
* Change system Date/Time
* Navigate Back or Exit <br>
<img width="749" height="532" alt="Image" src="https://github.com/user-attachments/assets/4f31cfa5-f57d-4fd4-b3d4-559e983d8a07" />

#### 🚀 4. System Performance
* Displays installed software list
* Transfer selected programs to Uninstall List
* Simulate software removal
* Improve system speed and performance <br>
<img width="745" height="543" alt="Image" src="https://github.com/user-attachments/assets/f28297cc-4101-4af9-86df-fe831ed0972c" />

#### 🔐 5. Protect System
* Lock/unlock folders
* Optional password protection for extra security
* Uses file dialogs for folder selection <br>
<img width="746" height="536" alt="Image" src="https://github.com/user-attachments/assets/541e70c5-073b-42b6-b473-0f61cf4f900a" />

#### 🔒 6. Additional Tools
* Encrypt/Decrypt files using cryptography.fernet
* Browse files easily
* Save encrypted files with .enc extension
* Decrypt files back to original format <br>
<img width="747" height="540" alt="Image" src="https://github.com/user-attachments/assets/35ae3aed-7195-4baf-a9f6-31da4b8bb09a" />

#### 🧹 7. Clean Up Window
* Clear Recycle Bin and Temporary Files
* Confirmation dialogs using askyesno()
* Display results in messageboxes <br>
<img width="748" height="538" alt="Image" src="https://github.com/user-attachments/assets/a77428a7-8c92-4240-8750-1ccb2e1f1070" />

## 🧠 Usage
1. Run the application.
2. Login with your credentials.
3. Explore the Dashboard for all utilities.
4. Use each module as per need:
    * Optimize system
    * Clean files
    * Protect and encrypt data
    * Customize Windows settings
  
## 🏁 Conclusion
The System Utility Application demonstrates how Python can be used to build efficient, secure, and interactive system tools.
It simplifies system management tasks by combining cleanup, performance optimization, and file protection into one intuitive application.

This project is ideal for:
* Students learning GUI development
* Users who want a simple PC optimization tool
* Developers exploring Python-based utilities

## 👨‍💻 Author

#### Kartavya Prakash Badge
📧 Email: kartavyabadge2011@gmail.com<br>
🔗 LinkedIn – Kartavya Badge<br>
📍 Nagpur, Maharashtra, India
