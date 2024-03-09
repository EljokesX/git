import threading
import socket
import time

PORT = 6060 
FORMAT = "utf-8" #type of write
D = "DES"
HEADER = 64 #size of message
SERVER = "192.168.174.1" #ip adderss of server
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    MSG = msg.encode(FORMAT)
    msg_len = len(MSG)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(MSG)
    

x = ''
input (x)
while x != D:
    send(x)

send(D)
