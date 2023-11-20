from tkinter import * 
window = Tk()

photo1 = PhotoImage(file = r"C:\Users\jhkim\OneDrive\바탕 화면\컴퓨터 프로그래밍 - 파이썬\기말고사 내용\dog.png")
photo2 = PhotoImage(file = r"C:\Users\jhkim\OneDrive\바탕 화면\컴퓨터 프로그래밍 - 파이썬\기말고사 내용\cell1.png")
label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side = LEFT)
label2.pack()

window.mainloop()