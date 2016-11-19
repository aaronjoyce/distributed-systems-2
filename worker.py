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
			print "received: " + received
		 	if not received:
		 		break
		   	else:
		   		if "helo" in received.strip().lower():
		   			self.socket.sendall("{0}\nIP:{1}\nPort:{2}\nStudentID:{3}\n".format(received.strip(), self.host, self.port, 12326755))
				elif "kill_service" in received.strip().lower():
					self.socket.close()
					self.exit = True
    		# Wait for communication
