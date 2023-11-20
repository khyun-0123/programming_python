from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("파일창 제목")
hap_num = 0

def ipryuk():
    global hap_num
    textbox.insert(END, entry1.get() + " " + entry2.get() + " " + entry3.get() + "\n")
    hap_num += int(entry3.get())
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def chonghap():
    label4.configure(text = hap_num)


def delete():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    textbox.delete(1.0, END)
    label4.configure(text = "")


label1 = Label(window, text = "사원코드")
entry1 = Entry(window)
label2 = Label(window, text = "전자제품")
entry2 = Entry(window)
label3 = Label(window, text = "판매가격")
entry3 = Entry(window)
button1 = Button(window, text = "입력", command = ipryuk)
button2 = Button(window, text = "총판매금액", command = chonghap)
button3 = Button(window, text = "삭제", command = delete)
label4 = Label(window, bg = "lightgray", width = 9)
label5 = Label(window, text = "●출력창")
textbox = Text(window, width = 70)

label1.place(x = 20, y = 20)
entry1.place(x = 100, y = 20)
label2.place(x = 20, y = 50)
entry2.place(x = 100, y = 50)
label3.place(x = 20, y = 80)
entry3.place(x = 100, y = 80)
button1.place(x = 250, y = 20)
button2.place(x = 300, y = 20)
button3.place(x = 250, y = 50)
label4.place(x = 300, y = 50)
label5.place(x = 50, y = 100)
textbox.place(x = 20, y = 120)


window.mainloop()