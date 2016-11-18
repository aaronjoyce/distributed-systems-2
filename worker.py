import threading
import socket

class Worker(threading.Thread):
	def __init__(self, host, port, socket, buffer_size=1024, chat_room=None):
		threading.Thread.__init__(self, target=self.run)
		self.host = host
 		self.port = port
		self.socket = socket
		self.exit = False
		self.buffer_size = buffer_size

	def run(self):
   		while not self.exit:
		  	received = self.socket.recv(self.buffer_size)
		 	if not received:
		 		break
		   	else:
		   		if received.strip() == "HELO text":
		   			self.socket.sendall("HELO text\nIP:{0}\nPort:{1}\nStudentID:{2}\n".format(self.host, self.port, 12326755))
    		# Wait for communication
