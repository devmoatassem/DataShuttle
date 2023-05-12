from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
import threading
from tkinter import ttk

filename = ""
window = None
progress_bar = None

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
    s.bind((host, port))
    s.listen(1)
    print(host)
    print('waiting for any incoming connections....')
    conn, addr = s.accept()
    file_size = os.stat(filename).st_size
    conn.send(f"{os.path.basename(filename)}:{file_size}".encode())
    sent = 0
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            conn.send(data)
            sent += len(data)
            progress = (sent / file_size) * 100
            progress_bar['value'] = progress
            progress_label.config(text=f"{progress:.2f}%")
    conn.close()
    messagebox.showinfo("Success", "File sent successfully")

def send_file_thread():
    send_thread = threading.Thread(target=send_file)
    send_thread.start()

def Send():
    global window, selected_file_label, progress_bar, progress_label

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
    Label(window, text=f'ID: {host}', bg='white', fg='black').place(x=140, y=290)

    selected_file_label = Label(window, text="", bg='white', fg='black')
    selected_file_label.place(x=140, y=390)

    sendButton_image = PhotoImage(file="media/SendButton.png")
    send_button = Button(window, text="Send", image=sendButton_image, bg="#EBDCED", fg="#000", bd=0, command=send_file_thread)
    send_button.place(x=100, y=350)

    select_file_button = Button(window, text="+Select File", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=select_file)
    select_file_button.place(x=100, y=300)

    progress_label = Label(window, text="", bg='white', fg='black')
    progress_label.place(x=140, y=440)

    progress_bar =ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(x=100, y=480)

    window.mainloop()


Send()
