import os
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("A")
client.connect(("localhost", 9999))
file = open("media/abc.png", "rb") 
print("READ")
file_size = os.path.getsize("media/abc.png")
print(file_size)
client.send("media/abc.png".encode()) 
client.send(str(file_size).encode())
print("SEND")
data = file.read() 
client.sendall(data) 
client.send(b"<END>")
print("DONE")
file.close()
client.close()


# import os, socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("localhost", 9999))

# filename = "media/abc.png"

# with open(filename, "rb") as file:
#     file_size = os.path.getsize(filename)
#     # protocol <filename>\n<size>\n<data>
#     client.sendall(filename)
#     client.sendall(b"\n")
#     client.sendall(str(file_size))
#     client.sendall(b"\n")
#     data = file.read()
#     client.sendall(data)
#     client.close()