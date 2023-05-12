#Libraries Import
from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

#Backend Code
def Send():
    window=Toplevel (root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable (False, False)

    def select_file():
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('file_type','*.txt'),('all files','*.*')))

    def send_file():
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
    #icon
    image_icon1=PhotoImage(file="media/abc.png")
    window.iconphoto (False,image_icon1)

    Sbackground=PhotoImage(file="media/abc.png")
    Label (window, image=Sbackground).place(x=-2,y=0)
    Mbackground=PhotoImage (file="media/abc.png")
    Label (window, image=Mbackground, bg='#f4fdfe').place(x=100,y=260) 

    #Get Hostname
    host=socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white',fg='black').place (x=140,y=290) 


    Button(window,text="+Select File",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=send_file).place(x=300,y=150)

    window.mainloop()

def Receive():
    window=Toplevel (root)
    window.title("Receive")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable (False, False)

    def receiver():
        ID=SendorID.get()
        filename1=Incoming_filename.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("File Received Successfully")


    #icon
    image_icon1=PhotoImage(file="media/abc.png")
    window.iconphoto (False,image_icon1)

    Sbackground=PhotoImage(file="media/abc.png")
    Label (window, image=Sbackground). place (x=-2,y=0)
    Mbackground=PhotoImage (file="media/abc.png")
    Label (window, image=Mbackground, bg='#f4fdfe'). place (x=100,y=250) 

    Label(window,text="Receive",font=('arial',20),bg="#f4fdfe").place(x=100,y=280)

    Label(window,text="Input Sendor ID",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=340)
    SendorID=Entry(window,width=25,fg='black',border=2,bg='white',font=('arial',15))
    SendorID.place(x=20,y=370)
    SendorID.focus()

    Label(window,text="File name for incming file",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=420)
    Incoming_filename=Entry(window,width=25,fg='black',border=2,bg='white',font=('arial',15))
    Incoming_filename.place(x=20,y=450)


    #image_icon1=PhotoImage(file="media/abc.png")
    rr=Button(window,text="Reveive",compound=LEFT,image=image_icon1,width=130,bg='#39c790',font="arial 14 bold")
    rr.place(x=20,y=500)
    



    window.mainloop()


    
#GUI Design

root=Tk()

root.title("DataShuttle")
root.geometry("450x560+500+200")
root.configure(bg='#9F2B68')

# Icon Add 

image_icon=PhotoImage(file="media/abc.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg='#9F2B65').place(x=20,y=30)
Frame(root,width=400,height=2,bg='#9F2A68').place(x=25,y=80)



send_image=PhotoImage(file="media/abc.png")

send=Button(root, image=send_image, bg="#f4fdfe", bd=0,command=Send)

send.place(x=50, y=100)

receive_image=PhotoImage(file="media/abc.png")

receive=Button (root, image=receive_image, bg="#f4fdfe", bd=0,command=Receive)

receive.place(x=600, y=100)

#label

Label (root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65, y=90)

Label (root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=600, y=90)


background=PhotoImage(file="media/abc.png")
Label(root,image=background).place(x=-2,y=400)


root.mainloop()