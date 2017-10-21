import os
import socket
import subprocess
import logging

# Create logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

host = "192.168.43.164"
port = 9999

# Set logging application
logger = logging.getLogger('Client')
logger.info('Connecting to host:post - {}:{}'.format(host, port))

s = socket.socket()
s.connect((host, port))

logger.info('Connecting successfully!')

while True:
    data = s.recv(1024)
    if(len(data)>0):
        output_str = str(data,'utf-8')
        logger.info('Word received:  %s' % output_str)
        s.send(str.encode(output_str))

s.close()
logger.info('Connection closed!')
