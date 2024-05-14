import tkinter as tk
import os
import time
import sys
import tkinter.ttk as ttk




def loginWindow():

    root = tk.Tk()
    root.title("")
    root.resizable(False,False)

    usernameVariable = tk.StringVar()
    passwordVariable = tk.StringVar()

    lbl1 = tk.Label(root, text="Login to Shitsoft", font=("Arial", 18))
    lbl1.grid()

    lbl2 = tk.Label(root, text="username:")
    lbl2.grid(column=0, row=1)

    userentry = ttk.Entry(root, textvariable=usernameVariable)
    userentry.grid(column=0, row=2)

    lbl2 = tk.Label(root, text="password:")
    lbl2.grid(column=0, row=3)


    passentry = ttk.Entry(root, textvariable=passwordVariable, show="*")
    passentry.grid(column=0, row=4)


    submitBtn = tk.Button(root, text="login", font=("Arial", 10), cursor="hand2")
    submitBtn.grid(column=0, row=5)


    root.mainloop()



if __name__ == "__main__":
    loginWindow()