import tkinter, random

window = tkinter.Tk()
window.geometry("500x300")
v = tkinter.IntVar()

def passwordgen(length):
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.sample(char, length))
    entry1.delete(0, tkinter.END)
    entry1.insert(0, password)
def check():
    if v.get() == 8:
        passwordgen(8)
    elif v.get() == 12:
        passwordgen(12)
    elif v.get() == 14:
        passwordgen(14)

label1 = tkinter.Label(window, text = "Password Generator")
label1.pack()

entry1 = tkinter.Entry(window, text = "")
entry1.pack()

button1 = tkinter.Radiobutton(window, text = "Small password", variable = v, value = 8)
button1.pack()
button2 = tkinter.Radiobutton(window, text = "Medium password", variable = v, value = 12)
button2.pack()
button3 = tkinter.Radiobutton(window, text = "Large password", variable = v, value = 14)
button3.pack()

generator = tkinter.Button(window, text = "generate", command = lambda: check())
generator.pack()




window.mainloop()