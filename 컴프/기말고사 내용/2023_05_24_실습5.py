from tkinter import*
window=Tk()

button1 = Button(window, text = "COOKBOOK~~Python을")
button2 = Button(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
button3 = Button(window, text = "공부 중입니다", bg = "magenta", width = 20, height = 5, anchor = SE)

button1.pack()
button2.pack()
button3.pack()

window.mainloop()