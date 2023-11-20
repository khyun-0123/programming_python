from tkinter import *

window = Tk()
window.geometry("600x600")
window.resizable(False, False)
textList = []
y = 100 

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
    cb1.place(x = 100, y = y)
    y += 20        

entry1 = Entry(window)
button1 = Button(window, text = "입력", command = ipryuk)
textbox = Text(window)

entry1.grid(row=0, column=0)
button1.grid(row=0, column=1)
textbox.grid(row=1, column=0, columnspan=2)

window.mainloop()