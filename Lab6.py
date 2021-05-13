import socket

PORT = 80
WWW = "www.google.com"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((WWW, PORT))
    client.sendall("GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")
    response = str(client.recv(4096),'utf-8')
    client.close()

print(response)
plik = open("wynik.txt", "w")
plik.write(response)
plik.close