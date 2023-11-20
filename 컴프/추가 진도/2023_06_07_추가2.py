from tkinter import *
from tkinter import messagebox

##함수 선언 부분##
def clickimage(event) :
    messagebox.showinfo("마우스", "명화에 마우스가 클릭")

##메인 코드 부분##
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = r"C:\Users\jhkim\OneDrive\바탕 화면\컴퓨터 프로그래밍 - 파이썬\기말고사 내용\dog.png")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickimage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()