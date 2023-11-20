from tkinter import *

window = Tk()
window.geometry("285x280")
btnList = []
xPos, yPos = 0, 0
num = 0

for i in range(10):
    btnList.append('button' + str(i))

for i in range(0, 9) :
    btnList[i] = Button(window, text = i+1, bg = "gray", font = ('arial', 20), width = 5, height = 2)

for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 95
    xPos = 0
    yPos += 93

window.mainloop()