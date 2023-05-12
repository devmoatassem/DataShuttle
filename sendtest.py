from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

filename = ""

def Send():
    window=Tk()
    
    global filename
    
    window.title("Send")
    window.geometry("401x553+483+109")
    window.configure(bg='#EBDCED')
    window.resizable (False, False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('file_type','*.txt'),('all files','*.*')))
        print(filename)
        filename_label.config(text=os.path.basename(filename))

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

    # Background image added
    Sbackground=PhotoImage(file="media/background.png")
    Label (window, image=Sbackground).place(x=-2,y=0)
    
    #Get Hostname
    host=socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white',fg='black').place (x=140,y=290) 
    
    # Show selected filename
    filename_label = Label(window, text='', bg='white', fg='black', anchor=W, wraplength=350)
    filename_label.place (x=25,y=390)
    
    # def update_filename_label():
    #     global filename
        
    
    Button(window,text="+Select File",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=100,y=300)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=send_file).place(x=300,y=150)
    # Button(window,text="Update Filename",width=14,height=1,font='arial 12',bg="#fff",fg="#000",command=update_filename_label).place(x=230,y=385)

    window.mainloop()

Send()
