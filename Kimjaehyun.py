from tkinter import * 
from tkinter.messagebox import Message

window = Tk()
window.geometry("600x600")
window.title("동물 병원프로그램")
input_List = []

cnt = 0
cnt = int(cnt)

#함수
def ipryuk():
    global cnt
    if (entry1.get() == "") or (entry2.get() == "") or (entry3.get() == "") or (entry4.get() == ""):
        Message(message = "모든 칸을 채워주세요").show()
    else:
        input_List.append(entry1.get() + " " + entry2.get() + " " + entry3.get() + " " + entry4.get())
        textbox.delete(1.0, END)
        for i in range(0, len(input_List)):
            textbox.insert(END, input_List[i])
            textbox.insert(END, "\n")
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
    print(input_List)

def delete():
    for i in range (0, len(input_List)):
        if input_List[i].count(entry6.get()) == 1:
            textbox.delete(1.0, END)
            input_List.pop(i)
            print("delete")
            for i in range(len(input_List)):
                textbox.insert(END, input_List[i])
                textbox.insert(END, "\n")
                print(input_List)

def junchae():
    label111.configure(text = len(input_List))



#코드 구현
label1 = Label(window, text = "이름")
entry1 = Entry(window)
label2 = Label(window, text = "견종")
entry2 = Entry(window)
label3 = Label(window, text = "나이")
entry3 = Entry(window)
label4 = Label(window, text = "몸무게")
entry4 = Entry(window)

button1 = Button(window, text = "입력", command = ipryuk)

button2 = Button(window, text = "전체(몇마리)", command = junchae)
label111 = Label(window, bg = "lightgray", width = 9)

entry6 = Entry(window)
button6 = Button(window, text = "삭제(이름)", command = delete)
entry7 = Entry(window)
button7 = Button(window, text = "검색")
button8 = Button(window, text = "종에 따른 분류")

textbox = Text(window, width = 70)

#화면 구현
label1.place(x = 20, y = 20)
entry1.place(x = 70, y = 20)
label2.place(x = 20, y = 40)
entry2.place(x = 70, y = 40)
label3.place(x = 20, y = 60)
entry3.place(x = 70, y = 60)
label4.place(x = 20, y = 80)
entry4.place(x = 70, y = 80)

button1.place(x = 220, y = 20)

button2.place(x = 220, y = 40)
label111.place(x = 300, y = 40)

entry6.place(x = 20, y = 100)
button6.place(x = 150, y = 100)
entry7.place(x = 220, y = 100)
button7.place(x = 350, y = 100)
button8.place(x = 400, y = 100)

textbox.place(x = 20, y = 120)



window.mainloop()