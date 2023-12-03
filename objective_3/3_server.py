'''
how to create a simple server
'''
import socket
#create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server set up - specify the server address and port
host = "127.0.0.1"
port = 12345


#bind the server address and the port

server_socket.bind((host, port))

#listening for incoming connections
server_socket.listen()
print(f"server listening on {host} : {port}")

#Accept connections and handle data
while True:

    client_socket, client_address = server_socket.accept()
    print(f"accepted connections from {client_address}")

    #recieve data and send data
    data = client_socket.recv(1024)

    #send a response to the client
    response = "Hello, client! Thanks for connecting"
    client_socket.send(response.encode('utf-8'))

    #close the connection
    client_socket.close()
