from tkinter import *
from time import *

##전역 변수 선언 부분##
btnList = [None] * 9
frameList = []
for i in range(10):
    frameList.append('cell' + str(i))
photoList = [None] * 9
num = 0

##함수 선언 부분##
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = "C:/Users/jhkim/OneDrive/바탕 화면/컴퓨터 프로그래밍 - 파이썬/기말고사 내용/" + frameList[num] + ".png")
    pLabel.configure(image = photo)
    pLabel.image = photo
    label1.configure(text = frameList[num] + ".png")


def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="C:/Users/jhkim/OneDrive/바탕 화면/컴퓨터 프로그래밍 - 파이썬/기말고사 내용/" + frameList[num] + ".png")
    pLabel.configure(image = photo)
    pLabel.image = photo
    label1.configure(text = frameList[num] + ".png")


##메인 코드 부분##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")
btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnNext = Button(window, text = "다음>>", command = clickNext)
label1 = Label(window, text = frameList[num] + ".png")

photo = PhotoImage(file = "C:/Users/jhkim/OneDrive/바탕 화면/컴퓨터 프로그래밍 - 파이썬/기말고사 내용/" + frameList[num] + ".png")
pLabel = Label(window, image = photo)

x = ((700 - photo.width()) // 2)
y = ((500 - photo.height()) // 2)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = x, y = y)
label1.pack(side = TOP, pady = 10)

window.mainloop()