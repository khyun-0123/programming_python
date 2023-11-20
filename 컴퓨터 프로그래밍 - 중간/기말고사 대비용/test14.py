from tkinter import *

window = Tk()
window.title("결제출력창")
window.geometry("600x600")
chonghap_num = 0

#함수
def ipryuk():
    global chonghap_num
    textbox.insert(END, entry1.get() + " " + entry2.get() + " " + entry3.get() + "\n")
    chonghap_num += int(entry3.get())
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def chonghap():
    label4.configure(text = chonghap_num)

def delete():
    global chonghap_num
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    textbox.delete(1.0. END)
    chonghap_num = 0
    label4.configure(text = "")


#화면 구성요소
label1 = Label(window, text = "사원코드")
entry1 = Entry(window)
label2 = Label(window, text = "전자제품")
entry2 = Entry(window)
label3 = Label(window, text = "가격")
entry3 = Entry(window)

button1 = Button(window, text = "입력", command = ipryuk)
button2 = Button(window, text = "총판매금액", command = chonghap)
button3 = Button(window, text = "삭제", command = delete)

label4 = Label(window, bg = "lightgray", width = 15)

label5 = Label(window, text = "출력창")

textbox = Text(window)

#화면 출력
label1.place(x = 20, y = 10)
entry1.place(x = 100, y = 10)
label2.place(x = 20, y = 40)
entry2.place(x = 100, y = 40)
label3.place(x = 20, y = 70)
entry3.place(x = 100, y = 70)

button1.place(x = 250, y = 10)
button2.place(x = 250, y = 40)
button3.place(x = 250, y = 70)

label4.place(x = 350, y = 40)

label5.place(x = 70, y = 100)
textbox.place(x = 20, y = 100)

window.mainloop()