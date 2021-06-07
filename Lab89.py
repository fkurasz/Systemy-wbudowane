import socket

def html(stan):
    strona = "HTTP/1.1\r\nContent-Type: text/html; charset = utf-8\r\n\r\n"
    if stan == "ON":
        zmien = "OFF"
        strona += "<html><body> Stan monitora: " + stan + "<br><a href =/" + zmien + ">Wylacz" + "</a></body></html>"
    else :
        zmien = "ON"
        strona += "<html><body> Stan monitora: " + stan + "<br><a href =/" + zmien + ">Wlacz" + "</a></body></html>"
    
    return strona

server = socket.socket()

try:
    server.bind(('localhost', 8080))
    server.listen(1)
    print("Nawiazywanie polaczenia...")
    while True:
        connection, client = server.accept()
        get = connection.recv(1024).decode()

        print(get)
        if "/ON" in get:
            with open("monitor.txt", "w") as plik:
                plik.write("ON")
        elif "/OFF" in get:
            with open("monitor.txt", "w") as plik:
                plik.write("OFF")
        with open("monitor.txt", "r") as plik:
            data = html(plik.read())
        connection.sendall(data.encode())
        connection.shutdown(socket.SHUT_WR)
except Exception as e:
    print ("Error: ", e)

server.close()