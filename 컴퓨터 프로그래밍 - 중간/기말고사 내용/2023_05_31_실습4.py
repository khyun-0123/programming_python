from tkinter import *

##전역 변수 선언 부분##
btnList = [None] * 9
buttons = []
for i in range(10):
    buttons.append('button' + str(i))
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

##메인 코드 부분##
window = Tk()
window.geometry("210x210")

for i in range(0, 9) :
    btnList[i] = Button(window)

for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()