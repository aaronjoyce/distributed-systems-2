import threading
import socket
from worker import Worker

class WorkerPool:

	def __init__(self, host, port, thread_pool_size=20, buffer_size=1024):
		self.host = host 
		self.port = port 
		self.thread_pool_size = thread_pool_size
		self.buffer_size = buffer_size
		self.listener = None
		self.thread_pool = []

	def run(self):
		self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.listener.bind((self.host, self.port))
		self.listener.listen(1)

		while True:
			conn, addr = self.listener.accept()
			if (len(self.thread_pool) < self.thread_pool_size):
				# Then, accept the connection. 
				# Otherwise, return a full-capacity
				# message to the client attempting to 
				# connect.
				# At this point, we receive the data, getting
				# the name of the chatroom specified
				worker = Worker(addr[0], addr[1], conn)
				worker.start()
				self.thread_pool.append(worker)
			else:
				print 'Oops, busy', addr

		return True