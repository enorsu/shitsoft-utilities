import tkinter as tk
from tkinter import messagebox
import os
import time
from tkinter import ttk
import threading
import random
import sys
import requests

def download_file(url, destination):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(destination, 'wb') as f:
                f.write(response.content)
            print(f"File downloaded successfully to: {destination}")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def checkIfOnWindows():
    return os.name == 'nt'

def checkIfDebugging():
    try:
        if sys.argv[1] == "--debug":
            return True
        else:
            return False
    except:
        return False

def on_minimize():
    pass

def disable_minimize_button(window):
    window.bind("<Unmap>", lambda e: window.deiconify())
    window.protocol("WM_DELETE_WINDOW", on_minimize)

def no():
    messagebox.showerror("", "Error 404")

def window1():
    global root
    root = tk.Tk()
    if isDebugging:
        root.title("BobInstaller(DEBUG)")
    else:
        root.title("BobInstaller")
    if not isDebugging:
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", no)
        root.attributes("-topmost", True)
        disable_minimize_button(root)

    lbl2 = tk.Label(root, text="Do you want to install Bob?", font=("Arial", 20))
    lbl2.grid(column=0, row=1)

    yesbtn = tk.Button(root, text="Install Bob", padx=38, command=startInstallFirstPart, font=("Arial", 14))
    yesbtn.grid(column=0, row=2)

    nobtn = tk.Button(root, text="No, quit", padx=4, command=rickroll, font=("Arial", 7))
    nobtn.grid(column=0, row=3)

    lbl3 = tk.Label(root, text="© ShitSoft All rights reserved to enorsu/Panagiotis3149(discord)", font=("Arial", 5))
    lbl3.grid(column=0, row=4)

    root.mainloop()

def rickroll():
    os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return

def rlyQuitwindow():
    global root1
    root.withdraw()

    root1 = tk.Tk()
    root1.title("")
    root1.resizable(False, False)
    root1.protocol("WM_DELETE_WINDOW", no)
    root1.attributes("-topmost", True)
    disable_minimize_button(root1)

    lbl1 = tk.Label(root1, text="Confirmation?")
    lbl1.grid(column=0, row=0)

    lbl2 = tk.Label(root1, text="Do you want to quit?")
    lbl2.grid(column=0, row=1)

    nobtn = tk.Button(root1, text="No, go back", padx=4, command=quitQuitwindow)
    nobtn.grid(column=0, row=3)

    root1.mainloop()

    root.deiconify()

def quitQuitwindow():
    root.deiconify()
    root1.destroy()

def startInstallFirstPart():
    root.destroy()
    startInstallSecondPart()

def startInstallSecondPart():
    global root, progressbar
    root = tk.Tk()
    root.title("Install Progress")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    lbl1 = tk.Label(root, text="Installing, please wait", font=("System", 20))
    lbl1.grid(column=0, row=0)

    progressbar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
    progressbar.grid(column=0, row=1)

    progress_thread = threading.Thread(target=doProgress)
    progress_thread.start()

    root.mainloop()

def doProgress():
    bobManagerURL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ""  # Replace with actual URL
    bobFileName = "bob.exe"  # Replace with actual file name

    maxi = 100
    randomdownloadtime = random.randint(10, 99)
    for i in range(maxi):
        progressbar["value"] = i / maxi * 100
        root.update_idletasks()

        if i == randomdownloadtime:
            download_file(bobManagerURL, bobFileName)

    end()

def end():
    messagebox.showinfo("Installation Complete", "Thank you for installing Bob.exe")
    sys.exit()

def main():
    global isDebugging
    isDebugging = checkIfDebugging()
    window1()

if __name__ == "__main__":
    if checkIfOnWindows():
        main()
    else:
        messagebox.showerror("Unsupported OS", "This application is designed to run on Windows.")
