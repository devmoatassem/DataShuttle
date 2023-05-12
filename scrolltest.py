from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
import threading
from tkinter import ttk

    ##############################
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print("A")
    # client.connect(("localhost", 9999))
    # file = open("media/abc.png", "rb") 
    # print("READ")
    # file_size = os.path.getsize("media/abc.png")
    # print(file_size)
    # client.send("received_image.png".encode()) 
    # client.send(str(file_size).encode())
    # print("SEND")
    # data = file.read() 
    # client.sendall(data) 
    # client.send(b"<END>")
    # print("DONE")
    # file.close()
    # client.close()
    ################################






def Send():
    # 
    global filename, window, selected_file_label, progress_bar, progress_label
    window = None
    progress_bar = None
    filename = ""

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('all files', '*.*'), ('file_type', '*.txt')))
        print(filename)

        selected_file_label.config(text=os.path.basename(filename))

    def send_file():
        global filename
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind(("localhost", port))
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


    window = Tk()

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


Send()
