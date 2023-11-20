from tkinter import *

window = Tk()
window.title("결제출력창")
window.geometry("600x600")
window.resizable(False, False)
sum_price = 0

def ibryuk():
    global sum_price
    entry4.insert(END, entry1.get() + "  " + entry2.get() + "  " + entry3.get() + "\n")
    sum_price += int(entry3.get())
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def chonghab():
    label4.configure(text = sum_price)



label1 = Label(window, text = "사원코드", )
entry1 = Entry(window)
label2 = Label(window, text = "전자제품")
entry2 = Entry(window)
label3 = Label(window, text = "판매가격")
entry3 = Entry(window)
button1 = Button(window, text = "입력", command = ibryuk)
button2 = Button(window, text = "총판매금액", command = chonghab)
label4 = Label(window, bg = "lightgray", width = 10, height = 2)
label5 = Label(window, text = "●출력창")
entry4 = Text(window, width = 35, height = 5)



label1.place(x = 20, y = 10)
entry1.place(x = 100, y = 10)
label2.place(x = 20, y = 40)
entry2.place(x = 100, y = 40)
label3.place(x = 20, y = 70)
entry3.place(x = 100, y = 70)
button1.place(x = 250, y = 10)
button2.place(x = 300, y = 10)
label4.place(x = 300, y = 40)
label5.place(x = 125, y = 100)
entry4.place(x = 20, y = 120)


window.mainloop()