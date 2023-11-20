from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

window = Tk()
window.title("강아지 사진")


photo = PhotoImage(file = r"C:\Users\jhkim\OneDrive\바탕 화면\컴퓨터 프로그래밍 - 파이썬\기말고사 내용\dog.png")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()