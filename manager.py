import tkinter as tk
import os
import time
import sys
import tkinter.ttk as ttk
from PIL import Image
import threading


def loginWindow():
    global root
    root = tk.Tk()
    root.title("")
    root.resizable(False,False)

    global usernameVariable
    global passwordVariable

    usernameVariable = tk.StringVar()
    passwordVariable = tk.StringVar()

    lbl1 = tk.Label(root, text="Login to Shitsoft", font=("System", 22))
    lbl1.grid()

    lbl2 = tk.Label(root, text="username:")
    lbl2.grid(column=0, row=1)

    userentry = ttk.Entry(root, textvariable=usernameVariable)
    userentry.grid(column=0, row=2)

    lbl2 = tk.Label(root, text="password:")
    lbl2.grid(column=0, row=3)


    passentry = ttk.Entry(root, textvariable=passwordVariable, show="*")
    passentry.grid(column=0, row=4)


    submitBtn = tk.Button(root, text="login", font=("System", 10), cursor="hand2", command=dontReallyLogin)
    submitBtn.grid(column=0, row=5)


    root.mainloop()


def dontReallyLogin():
    if usernameVariable.get() == "bob_from_alibaba" and passwordVariable.get() == "Silly_elephant_guy":
        root.destroy()

        threads = [threading.Thread(target=showImages) for _ in range(5)]

        for thread in threads:
            thread.start()

def showImages():
    for i in range(25):
        bob = Image.open("bob.png")
        bob.show()
        bob.close()


if __name__ == "__main__":
    loginWindow()
