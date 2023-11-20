from tkinter import *
from tkinter import messagebox
window = Tk()

def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크 버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", "체크 버튼이 켜졌어요.")
    
chk = IntVar() #체크여부를 chk에 담음. 0이면 꺼짐, 1이면 켜짐
cb1 = Checkbutton(window, text = "클릭하세요", variable = IntVar(), command = myFunc)

cb1.pack()

window.mainloop()