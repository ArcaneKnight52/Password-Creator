from tkinter import *
import pyperclip,random
rm=random.SystemRandom()
root=Tk()
root.title("Password Creator")
root.geometry("400x400")
s=StringVar()
len=IntVar()
len.set(0)
def pwd():
    l1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']
    p=""
    for x in range(len.get()):
        p+=rm.choice(l1)
    s.set(p)
def clipboard():
    rp=s.get()
    pyperclip.copy(rp)
Label(root,text="Password Creator", font="arial 20 bold").pack()
Label(root,text="Enter desired password length").pack(pady=3)
Entry(root,textvariable=len).pack(pady=3)
Button(root,text="Create Password",command=pwd).pack(pady=7)
Entry(root,textvariable=s).pack(pady=3)
Button(root,text="Copy to clipboard",command=clipboard).pack()
Button(root,text="Exit program",command=root.destroy).pack()
root.mainloop()