import socket
import urllib
import sys
from worker_pool import WorkerPool


def main():
	worker_pool = WorkerPool('localhost', 8080)
	worker_pool.run()

if __name__ == "__main__":
    main()