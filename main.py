import socket

HOST = 'www.google.com'
PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
client_socket.connect(server_address)


request_header = b'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
client_socket.sendall(request_header)

response = ''

while True:
    recv = client_socket.recv(1024)
    if not recv:
        break
    response += recv.decode('utf-8', errors='ignore')
    
print(response)
client_socket.close()

    