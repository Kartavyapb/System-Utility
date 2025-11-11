import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin():
        # Run the main part of your script here
        print("Running with administrative privileges!")
    else:
        # Re-run the script with admin rights
        print("Re-running script as administrator...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
