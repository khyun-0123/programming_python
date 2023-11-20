from tkinter import *
import random

##전역 변수 선언 부분##
btnList = [None] * 9
frameList = []
for i in range(10):
    frameList.append('cell' + str(i))
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

##메인 코드 부분##
window = Tk()
window.geometry("210x210")

for i in range(0, 9) :
    random_num = random.randint(0, 9)
    photoList[i] = PhotoImage(file = "C:/Users/jhkim/OneDrive/바탕 화면/컴퓨터 프로그래밍 - 파이썬/기말고사 내용/" + frameList[random_num] + ".png")
    btnList[i] = Button(window, image = photoList[i])

for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()