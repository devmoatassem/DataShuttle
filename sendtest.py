from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

filename = ""

def Send():
    window=Tk()
    #window=Toplevel (root)
    
    global filename
    
    window.title("Send")
    window.geometry("401x553+483+109")
    window.configure(bg='#EBDCED')
    window.resizable (False, False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('all files','*.*'),('file_type','*.txt')))
        print(filename)

        selected_file_label.config(text=os.path.basename(filename))

    def send_file():
        global filename
        s=socket.socket() 
        host=socket.gethostname()
        port=8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections....') 
        conn, addr=s.accept()
        file=open(filename, 'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")

    #icon of window
    image_icon1=PhotoImage(file="media/abc.png")
    window.iconphoto (False,image_icon1)

    # background=PhotoImage(file="media/background.png")
    # Label(root,image=background).place(x=-2,y=0)

    # Background image added

    Sbackground=PhotoImage(file="media/background.png")
    Label (window, image=Sbackground).place(x=-2,y=0)
    # Mbackground=PhotoImage (file="media/abc.png")
    # Label (window, image=Mbackground, bg='#f4fdfe').place(x=100,y=260) 

    #Get Hostname
    host=socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white',fg='black').place (x=140,y=290) 
    
    selected_file_label = Label(window, text="", bg='white',fg='black')
    selected_file_label.place(x=140,y=390) 

    sendButton_image=PhotoImage(file="media/SendButton.png")
    send=Button(window, text="Send", image=sendButton_image, bg="#EBDCED",fg="#000", bd=0,command=send_file).place(x=100,y=350)
    Button(window,text="+Select File",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=100,y=300)

    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=send_file).place(x=300,y=150)

    window.mainloop()

Send()
