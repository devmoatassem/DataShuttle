from tkinter import *

root = Tk()

# First screen with image1
frame1 = Frame(root)
image1 = PhotoImage(file="media/receive.png")
label1 = Label(frame1, image=image1)
label1.pack()
frame1.pack()

# Second screen with image2
frame2 = Frame(root)
image2 = PhotoImage(file="media/send.png")
label2 = Label(frame2, image=image2)
label2.pack()
frame2.pack()
frame2.lower() # Hide this frame initially

# Switch to screen 1
def show_frame1():
    frame2.lower()
    frame1.lift()

# Switch to screen 2
def show_frame2():
    frame1.lower()
    frame2.lift()

# Add buttons to switch between screens
button1 = Button(root, text="Screen 1", command=show_frame1)
button2 = Button(root, text="Screen 2", command=show_frame2)
button1.pack(side=LEFT)
button2.pack(side=RIGHT)

root.mainloop()
