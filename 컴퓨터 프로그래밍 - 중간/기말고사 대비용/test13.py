from tkinter import *
# from math import *
window = Tk()
window.title("엔트리")
window.geometry("400x400")
window.resizable(False, False)
num = 0

def save():
    global num
    entry4.insert(END, "사원" + str(num) + "   " + entry1.get() + "   " + entry2.get() + "   " + entry3.get() + "\n")
    num += 1
                     
label1 = Label(window, text = "사번")
entry1 = Entry(window)
label2 = Label(window, text = "이름")
entry2 = Entry(window)
label3 = Label(window, text = "전화번호")
entry3 = Entry(window)


#pack 함수 사용도 가능
# label1.pack()
# entry1.pack()
# label2.pack()
# entry2.pack()

label1.place(x = 20, y = 10)
entry1.place(x = 70, y = 10)
label2.place(x = 20, y = 30)
entry2.place(x = 70, y = 30)
label3.place(x = 20, y = 50)
entry3.place(x = 70, y = 50)

button1 = Button(window, text = "입력", command = save, width =8, height = 2)
button1.place(x = 110, y = 72)

entry4 = Text(window, width = 35, height = 5)
entry4.place(x = 20, y = 120)

window.mainloop()