import tkinter
window=tkinter.Tk()
button=tkinter.Button(window, text="do not press this", width=40)
button.pack(padx=10, pady=10)
clickCount=0
def onClick(event):
    global clickCount
    clickCount=clickCount+1
    if clickCount==1:
        button.configure(text="seriously?")
    elif clickCount==2:
        button.configure(text="next time, no more button.")
    elif clickCount==3:
        button.configure(text="wait was that THE NUCELAR LAUNCH BUTTON OH NOO")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()