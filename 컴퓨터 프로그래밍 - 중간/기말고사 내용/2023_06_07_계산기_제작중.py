from tkinter import *

#전역변수 선언 부분
btnList = [None] * 20
frameList = ["CE", "C", "<-", "÷", 7, 8, 9, "x", 4, 5, 6, "-", 1, 2, 3, "+", "+/-", 0, ".", "="]
i, k = 0, 0
xPos, yPos = 0, 20
num = 0

#함수
def del_pressed(value):
    numEntry.delete()

def enter_pressed():
    Entry.get()
    return


#메인 코드 부분
window = Tk()
window.geometry("206x296")
window.resizable(FALSE, FALSE)
window.title("Calculator")
entry_value = StringVar(window, value='')
numEntry = Entry(window, textvariable=entry_value, bg="white", width="29")

window.mainloop()