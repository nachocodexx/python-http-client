import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('www.google.com', 80)
client_socket.connect(server_address)

request_header = 'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'.encode()
client_socket.send(request_header)

response = ''
while True:
    recv = client_socket.recv(1024)
    if not recv:
        break
    response += str(recv)

print(response)
client_socket.close()

