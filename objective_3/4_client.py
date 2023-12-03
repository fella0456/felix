'''
creating a simple client

'''
import socket

#create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#set up a server address and port
host = "127.0.0.1"
port = 12345

#bind the client to server address and port

client_socket.connect((host, port))
message = "hello, server! how are you?"
client_socket.send(message.encode('utf-8'))

#recieve the response
response = client_socket.recv(1024)
print(f"server response : {response.decode('utf_8')}")

#close connection
client_socket.close()

