import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Do not press this button.", width=40, background="tomato")
button.pack(padx=10, pady=10)
clickCount = 0
def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="Seriously? listen.I SAID DO NOT PRESS IT!")
    elif clickCount == 2:
        button.configure(text="I am serious. Next time NO MORE BUTTON!")
    else:
        button.pack_forget()
button.bind("<ButtonRelease->", onClick)
window.mainloop()