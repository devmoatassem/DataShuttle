#Libraries Import
import threading
from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
from tkinter import ttk

#Backend Code

# Receive Function

def Receive():
    global filename, window, selected_file_label, progress_label_rec ,progress_bar_rec
    window = None
    progress_bar_rec = None
    filename = ""
    window=Toplevel (root)
    window.title("Receive")
    window.geometry("401x553+483+109")
    window.configure(bg='#EBDCED')
    window.resizable (False, False)

    def receive_file():
        s = socket.socket()
        host = socket.gethostname()
        ID=SendorID.get()
        print(socket.gethostbyname(ID))
        
        port = 8088
        s.connect((ID, port))
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
                progress_bar_rec['value'] = progress
                progress_bar_rec.config(text=f"{progress:.2f}%")
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
    progress_label_rec = Label(window, text=" 0%", width=4, height=1, font='arial 10 bold', bd=0, bg="#fff", fg="#000")
    progress_label_rec.place(x=300, y=410)
    #progress bar
    progress_bar_rec =ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar_rec.place(x=80, y=410)
    window.mainloop()

def Send():
    # 
    global filename, window, selected_file_label, progress_bar, progress_label
    window = None
    progress_bar = None
    filename = ""
    window=Toplevel (root)
    host = socket.gethostname()
    print(socket.gethostbyname(host))
    
    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', 
                                              filetypes=(('all files', '*.*'), ('file_type', '*.txt')))
        print(filename)

        selected_file_label.config(text=os.path.basename(filename))
        
    def send_file():
        global filename
        s = socket.socket()
        host = socket.gethostname()        
        port = 8088
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections....')
        conn, addr = s.accept()
        print('connection scceeded')
        file_size = os.stat(filename).st_size
        print(file_size)
        print(filename)
        conn.send(f"{os.path.basename(filename)}:{file_size}".encode())       
        sent = 0    #variable to determine amount of datasent for progress indicator
        with open(filename, 'rb') as f:
            print(filename)
            while True:
                data = f.read(1024)
                
                if not data:
                    break
                print("Reading and Sending Data")
                conn.send(data)
                sent += len(data)
                progress = (sent / file_size) * 100
                progress_bar['value'] = progress
                progress_label.config(text=f"{progress:.2f}%")
        conn.close()
        print("Done")
        messagebox.showinfo("Success", "File sent successfully")

    def send_file_thread():
        send_thread = threading.Thread(target=send_file)
        send_thread.start()


    
    window.title("Send")
    window.geometry("401x553+483+109")
    window.configure(bg='#EBDCED')
    window.resizable(False, False)
    # icon of window
    image_icon1 = PhotoImage(file="media/abc.png")
    window.iconphoto(False, image_icon1)
    # Background image added
    Sbackground = PhotoImage(file="media/background.png")
    Label(window, image=Sbackground).place(x=-2, y=0)
    # Get Hostname
    host = socket.gethostname()
    Label(window, text=f'ID: {host}', width=30, height=2, font='arial 10 bold',bd=0, bg='white', fg='black').place(x=80, y=280)
    #Show Filename Label
    selected_file_label = Label(window, text="File Name", width=23, height=2, font='arial 10 bold',bd=0, bg="#fff", fg="#000")
    selected_file_label.place(x=50, y=330)
    #Select File Button
    select_file_button = Button(window, text="+ Select File", width=12, height=2, font='arial 10 bold', bd=0, bg="#fff", fg="#000", command=select_file)
    select_file_button.place(x=250, y=330)
    # Send Button
    sendButton_image = PhotoImage(file="media/SendButton.png")
    send_button = Button(window, text="Send", image=sendButton_image, bg="#EBDCED", fg="#000", bd=0, command=send_file_thread)
    send_button.place(x=100, y=450)
    #progress %
    progress_label = Label(window, text=" 0%", width=8, height=1, font='arial 10 bold', bd=0, bg="#fff", fg="#000")
    progress_label.place(x=300, y=400)
    #progress bar
    progress_bar =ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(x=80, y=400)
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
background=PhotoImage(file="media/background.png")
Label(root,image=background).place(x=-2,y=0)
send_image=PhotoImage(file="media/send.png")
send=Button(root, text="Send", image=send_image, bg="#EBDCED",fg="#000", bd=0,command=Send)
send.place(x=100, y=303)
receive_image=PhotoImage(file="media/receive.png")
receive=Button (root,text="Send", image=receive_image, bg="#EBDCED",fg="#000", bd=0,command=Receive)
receive.place(x=100, y=403)
root.mainloop()