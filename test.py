import tkinter as tk

class MyApp:
    def __init__(self, parent):
        
        self.parent = parent
        self.parent.title("DataShuttle")
        self.parent.geometry("401x553+483+109")
        self.parent.resizable(width=False, height=False)
        self.parent.configure(bg='#EBDCED')
        image_icon=tk.PhotoImage(file="media/abc.png")
        self.parent.iconphoto(False,image_icon)

        # 
        # Create the frames
        self.Home=tk.Frame(self.parent)
        self.frame1 = tk.Frame(self.parent)
        self.frame2 = tk.Frame(self.parent)

        # Create the widgets for Home Screen


        send_image=tk.PhotoImage(file="media/send.png")

        self.send=tk.Button(self.frame1,image=send_image, bg="#EBDCED",fg="#000", bd=0).place(x=100, y=303)

        # send

        receive_image=tk.PhotoImage(file="media/receive.png")

        receive=tk.Button (self.frame1,image=receive_image, bg="#EBDCED",fg="#000", bd=0)
        # image=receive_image,
        receive.place(x=100, y=403)

        #label

        # Label (frame1, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=30, y=90)

        # Label (frame1, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=270, y=90)


        background=tk.PhotoImage(file="media/background.png")
        
        # self.label1 = tk.Label(self.frame1,image=background).place(x=-2,y=0)
        self.label1 = tk.Label(self.frame1, text="Welcome to Screen 1!")
        self.button1 = tk.Button(self.frame1, text="Go to Screen 2", command=self.show_frame2)


        self.label2 = tk.Label(self.frame2, text="Welcome to Screen 2!")
        self.button2 = tk.Button(self.frame2, text="Go to Screen 1", command=self.show_frame1)


        # Pack the widgets in each frame
        self.label1.pack()
        self.send.pack()
        self.label2.pack()
        self.button2.pack()

        # Show the first frame
        self.show_frame1()

    
    def show_frame1(self):
        # Show the first frame and hide the second frame
        self.frame1.pack()
        self.frame2.pack_forget()

    def show_frame2(self):
        # Show the second frame and hide the first frame
        self.frame2.pack()
        self.frame1.pack_forget()

# Create the main window
root = tk.Tk()

# Create the app object
app = MyApp(root)

# Run the main event loop
root.mainloop()