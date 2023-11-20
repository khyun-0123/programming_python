from tkinter import*
window=Tk()

photo = PhotoImage(file = "C:/Users/jhkim/OneDrive/바탕 화면/CodeCure/05-02_16_20.png")
label1 = Label (window, image = photo)

label1.pack()

window.mainloop()