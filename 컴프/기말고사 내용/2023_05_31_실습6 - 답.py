from tkinter import *
from time import *

##전역 변수 선언 부분##
fnameList = []
for i in range(10):
    fnameList.append('cell' + str(i) + '.png')
photoList = [None] * 9
num = 0

##함수 선언 부분##
def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file = "기말고사 내용/" + fnameList[num])
    label1.configure(text=fnameList[num])

    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file = "기말고사 내용/" + fnameList[num])
    label1.configure(text=fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
    

##메인 코드 부분##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")
btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = "기말고사 내용/" + fnameList[0])
pLabel = Label(window, image = photo)
label1 = Label(window, text = fnameList[num])

x = ((700 - photo.width()) // 2)
y = ((500 - photo.height()) // 2)

pLabel.place(x=x, y=y)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
label1.place (x = 325, y = 10)

window.mainloop()