from tkinter import *
from math import *
window = Tk()
window.title("엔트리")
window.geometry("400x400")
window.resizable(False, False)

def plus():
    label.configure(text = (eval(entry1.get()) + eval(entry2.get())))
def minus():
    label.configure(text = (eval(entry1.get()) - eval(entry2.get())))
def gob():
    label.configure(text = (eval(entry1.get()) * eval(entry2.get())))
def na():
    label.configure(text = (eval(entry1.get()) / eval(entry2.get())))

label1 = Label(window, text = "숫자1")
entry1 = Entry(window)
label2 = Label(window, text = "숫자2")
entry2 = Entry(window)

#pack 함수 사용도 가능
# label1.pack()
# entry1.pack()
# label2.pack()
# entry2.pack()

label1.place(x = 20, y = 10)
entry1.place(x = 70, y = 10)
label2.place(x = 20, y = 30)
entry2.place(x = 70, y = 30)

button1 = Button(window, text = "더하기", command = plus, width =4, height = 2)
button2 = Button(window, text = "빼기", command = minus, width =4, height = 2)
button3 = Button(window, text = "곱하기", command = gob, width =4, height = 2)
button4 = Button(window, text = "나누기", command = na, width =4, height = 2)

button1.place(x = 50, y = 60)
button2.place(x = 90, y = 60)
button3.place(x = 130, y = 60)
button4.place(x = 170, y = 60)


label = Label(window)
label.place(x = 50, y = 100)

window.mainloop()