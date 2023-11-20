from tkinter import *
window = Tk()

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 2
    photo = PhotoImage(file = "기말고사 내용\gif\dog%d.gif" % num)
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickNext():
    global num
    num += 1
    if num > 2:
        num = 0
    photo = PhotoImage(file = "기말고사 내용/dog.png")
    pLabel.configure(image = photo)
    pLabel.image = photo

btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnNext = Button(window, text = "다음>>", command = clickNext)

photo = PhotoImage(file = "기말고사 내용\dog.png")
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLable = Label(window, image = photo)

window.mainloop()