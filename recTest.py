from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
from tkinter import ttk

filename = ""
window = None
progress_bar = None

global selected_file_label, progress_label

def Receive():
    global filename, window, selected_file_label, progress_bar, progress_label
    window = None
    progress_bar = None
    filename = ""


    window=Tk()
    window.title("Receive")
    window.geometry("401x553+483+109")
    window.configure(bg='#EBDCED')
    window.resizable (False, False)

    # def receiver():
    #     ID=SendorID.get()
    #     filename1=Incoming_filename.get()
    #     print(ID)
    #     s=socket.socket()
    #     port=8080
    #     s.connect(("localhost",port))
    #     file=open(filename1,'wb')
    #     file_data=s.recv(1024)
    #     file.write(file_data)
    #     file.close()
    #     print("File Received Successfully")

    def receive_file():
        
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.connect(("localhost", port))
        print(f"Connected to {host}")
        data = s.recv(1024).decode()
        if data is None:
            messagebox.showerror("Error", "No data received")
            return
        print("Data Recived")
        filename, file_size = data.split(":")
        file_size = int(file_size)
        received = 0
        with open(os.path.basename(filename), "wb") as f:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                f.write(data)
                received += len(data)
                progress = (received / file_size) * 100
                progress_bar['value'] = progress
                progress_label.config(text=f"{progress:.2f}%")
        s.close()
        messagebox.showinfo("Success", "File received successfully")



    #icon
    image_icon1=PhotoImage(file="media/abc.png")
    window.iconphoto (False,image_icon1)


    Sbackground = PhotoImage(file="media/background.png")
    Label(window, image=Sbackground).place(x=-2, y=0)
    

    

    Label(window,text="Input Sendor ID",font=('arial',10,'bold'),bg="#f4fdfe").place(x=60,y=265)
    SendorID=Entry(window,width=25,fg='black',border=2,bg='white',font=('arial',15))
    SendorID.place(x=50,y=295)
    SendorID.focus()

    Label(window,text="File name for incming file",font=('arial',10,'bold'),bg="#f4fdfe").place(x=60,y=335)
    Incoming_filename=Entry(window,width=25,fg='black',border=2,bg='white',font=('arial',15))
    Incoming_filename.place(x=50,y=365)


    
    recivedButton_image = PhotoImage(file="media/saveButton.png")
    recived_button = Button(window, text="Send", image=recivedButton_image, bg="#EBDCED", fg="#000", bd=0, command=receive_file)
    recived_button.place(x=100, y=450)
    
    #progress %
    progress_label = Label(window, text=" 0%", width=4, height=1, font='arial 10 bold', bd=0, bg="#fff", fg="#000")
    progress_label.place(x=300, y=410)

    #progress bar
    progress_bar =ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(x=80, y=410)



    window.mainloop()


Receive()