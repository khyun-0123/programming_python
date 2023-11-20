#tkinter 활용해서 계산기 만들기

from tkinter import *

window = Tk()
window.geometry("600x600")
window.resizable(False, False)
textList = []
y = 45

def ipryuk():
    global y
    textbox.delete(1.0, END)
    text = entry1.get()
    textList.append(text)
    for i in range(len(textList)):
        textbox.insert(END, textList[i])
        textbox.insert(END, "\n")
    entry1.delete(0, END)
    print(textList)
    chk = IntVar()
    cb1 = Checkbutton(window, variable = chk)
    cb1.pack()

entry1 = Entry(window)
button1 = Button(window, text = "입력", command = ipryuk)
textbox = Text(window, width = 50)

entry1.pack()
button1.pack()
textbox.pack()

window.mainloop()