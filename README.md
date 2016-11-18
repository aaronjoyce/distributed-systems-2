# distributed-systems-2

To execute, do the following: 

1. Clone this repository;
2. Execute chmod +x compile.sh within the repository directory;
3. Run the bash executable, by entering ./compile.sh - this will start the connecttion-accepting server on port 8080. 
4. Establish a client connection by running ```python client.py --host localhost --port 8093 --message Hello```

The message will be echoed back to the client, and output by the accepting thread on the server-side. 
