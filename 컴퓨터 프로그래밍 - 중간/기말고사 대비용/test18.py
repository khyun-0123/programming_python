from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("창 제목")
window.resizable(False, False)

#함수 정의
def delete():
    textbox.delete(1.0, END)
    entry1.delete(0, END)
    label1.configure(text = " ")

#코드 정의
label1 = Label(window, text = " ")
entry1 = Entry(window)
textbox = Text(window)

#화면 구현
label1.place(x = 20, y = 20)




window.mainloop()