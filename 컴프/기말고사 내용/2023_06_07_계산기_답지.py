from tkinter import *

#전역변수 선언 부분
btnList = [None]*20
frameList = ["Num\nLock", "/", "*", "-", 7, 8, 9, "+", 4, 5, 6, None, 1, 2, 3, "Enter", 0, None, "del", None]
i, k = 0, 0
xPos, yPos = 0, 20
num = 0
isNumLockPressed = 1

#함수
def button_pressed(value):
    numEntry.insert("end", value)

def del_pressed(value):
    numEntry.delete(0,"end")

def enter_pressed(value):
    result = eval(numEntry.get())
    numEntry.delete(0, "end")
    numEntry.insert("end", result)

def numlock():
    global isNumLockPressed
    if isNumLockPressed == 1:
        numEntry.config(state="disabled")
        btnList[0].config(bg="gray")
        isNumLockPressed *= -1
    else:
        numEntry.config(state="normal")
        btnList[0].config(bg="light gray")
        isNumLockPressed *= -1

#메인 코드 부분

window = Tk()
window.geometry("206x296")
window.resizable(FALSE, FALSE)
window.title("Calculator")
entry_value = StringVar(window, value='')
numEntry = Entry(window, textvariable=entry_value, bg="white", width="29")
numEntry.place(x=0, y=0)

for i in range(20):
    if i != 7 and i!= 15 and i!= 16 and i!=18:
        if i != 0:
            btnList[i] = Button(window, text=frameList[i], width=5, height=3, padx=5, command = lambda value=i :button_pressed(frameList[value]))
        else:
            btnList[0] = Button(window, text=frameList[0], width=5, height=3, padx=5, bg="light gray", fg="blue", command = numlock)
    else:
        btnList[7] = Button(window, text=frameList[7], width=5, height=6, padx=5, pady=6, command = lambda:button_pressed(frameList[7]))
        btnList[15] = Button(window, text=frameList[15], width=5, height=6, padx=5, pady=6, fg="red", command = lambda:enter_pressed(frameList[15]))
        btnList[16] = Button(window, text=frameList[16], width=12, height=3, padx=6, command = lambda:button_pressed(frameList[16]))
        btnList[18] = Button(window, text=frameList[18], width=5, height=3, padx=5, command = lambda:del_pressed(frameList[i]))

for i in range(5):
    for k in range(4):
        if frameList[num] == "del":
            btnList[num].place(x=102, y=240)
            xPos += 51   
        else:
            btnList[num].place(x=xPos, y=yPos)
            num += 1
            xPos += 51
    xPos = 0
    yPos += 55

window.mainloop()