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
    window.geometry("401x553+483+109")
    window.configure(bg='#EBDCED')
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
    #icon of window
    image_icon1=PhotoImage(file="media/abc.png")
    window.iconphoto (False,image_icon1)

    # background=PhotoImage(file="media/background.png")
    # Label(root,image=background).place(x=-2,y=0)
    Sbackground=PhotoImage(file="media/background.png")
    Label (window, image=Sbackground).place(x=-2,y=0)
    # Mbackground=PhotoImage (file="media/abc.png")
    # Label (window, image=Mbackground, bg='#f4fdfe').place(x=100,y=260) 

    #Get Hostname
    host=socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white',fg='black').place (x=140,y=290) 


    Button(window,text="+Select File",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=send_file).place(x=300,y=150)

    window.mainloop()

def Receive():
    window=Toplevel (root)
    window.title("Receive")
    window.geometry("401x553+483+109")
    window.configure(bg='#EBDCED')
    window.resizable (False, False)

    def receiver():
        ID=SendorID.get()
        filename1=Incoming_filename.get()
        print(ID)
        s=socket.socket()
        port=8080
        s.connect(("localhost",port))
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
    rr=Button(window,text="Reveive",compound=LEFT,image=image_icon1,width=130,bg='#39c790',font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)
    



    window.mainloop()






##################################################################################################
# Home Screen
# ################################################################################################    
#GUI Design

root=Tk()

root.title("DataShuttle")
root.geometry("401x553+483+109")
root.configure(bg='#EBDCED')
root.resizable (False, False)
# Icon Add 

image_icon=PhotoImage(file="media/abc.png")
root.iconphoto(False,image_icon)

# Label(root,text="Let's Shuttle Your Data!",font=('Formata',15,'bold'),bg='#EBDCED').place(x=20,y=30)
# Frame(root,width=400,height=2,bg='#9F2A68').place(x=150,y=80)

background=PhotoImage(file="media/background.png")
Label(root,image=background).place(x=-2,y=0)


send_image=PhotoImage(file="media/send.png")

send=Button(root, text="Send", image=send_image, bg="#EBDCED",fg="#000", bd=0,command=Send)

send.place(x=100, y=303)

receive_image=PhotoImage(file="media/receive.png")

receive=Button (root,text="Send", image=receive_image, bg="#EBDCED",fg="#000", bd=0,command=Receive)
# image=receive_image,
receive.place(x=100, y=403)

#background image
# bg_image = PhotoImage(file="media/background.png")

# # Set the background of the window to the photo image
# background_label = Label(root, image=bg_image)
# background_label.place(relwidth=1, relheight=1)

#label

# Label (root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=30, y=90)

# Label (root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=270, y=90)





root.mainloop()