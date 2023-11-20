from tkinter import *
from math import *
window = Tk()
window.title("엔트리")
window.geometry("400x400")
window.resizable(False, False)

def cal():
    label.configure(text = (eval(entry1.get()) + eval(entry2.get())))

label1 = Label(window, text = "숫자1")
entry1 = Entry(window)
label2 = Label(window, text = "숫자2")
entry2 = Entry(window)

# label1.pack()
label1.place(x = 20, y = 10)
entry1.pack()
label2.pack()
entry2.pack()
#place 함수 사용도 가능

button = Button(window, text = "더하기", command = cal, width = 10, height = 2)
button.pack()

label = Label(window)
label.pack()

window.mainloop()