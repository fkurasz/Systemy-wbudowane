import socket

class KalkulatorRPN:
    def __init__(self):
        self.wynik = 0

    def dodawanie (self , wyrazenie1 , wyrazenie2 ):
        self.wynik = 0
        self.wynik = wyrazenie1 + wyrazenie2
    def odejmowanie (self , wyrazenie1 , wyrazenie2 ):
        self.wynik = 0
        self.wynik = wyrazenie1 - wyrazenie2
    def mnozenie (self , wyrazenie1 , wyrazenie2 ):
        self.wynik = 0
        self.wynik = wyrazenie1 * wyrazenie2
    def dzielenie (self , wyrazenie1 , wyrazenie2 ):
        self.wynik = 0
        self.wynik = wyrazenie1 / wyrazenie2
    def wynik_operacji(self):
        return self.wynik

kalkulator = KalkulatorRPN()

def kalkulatorFunc(dzialanie):
    stos = []
    wyrazenie = dzialanie.split(' ')
    
    # podane wyrazenie podzielone przez spacje
    # Podaj wyrazenie: 2 2 + 2 *
    # ['2', '2', '+', '2', '*']
    if 'q' in wyrazenie:
        return

    for x in range(len(wyrazenie)):

        if wyrazenie[x].isnumeric():
            stos.append(wyrazenie[x])

        else:
            if not stos:
                break
            else:
                a = int(stos.pop())
            if not stos:
                break
            else:
                b = int(stos.pop())

            if wyrazenie[x] == '+' or wyrazenie[x] == '+\r\n':
                kalkulator.dodawanie(b, a)
                stos.append(kalkulator.wynik)

            if wyrazenie[x] == '-' or wyrazenie[x] == '-\r\n':
                kalkulator.odejmowanie(b, a)
                stos.append(kalkulator.wynik)
                    
            if wyrazenie[x] == '*' or wyrazenie[x] == '*\r\n':
                kalkulator.mnozenie (b, a)
                stos.append(kalkulator.wynik)
                    
            if wyrazenie[x] == '/' or wyrazenie[x] == '/\r\n':
                kalkulator.dzielenie (b, a)
                stos.append(kalkulator.wynik)

    if stos:
        if len(stos) > 0:
            connection.send(b"Wynik: ")
            connection.send(str(stos[-1]).encode())
            connection.send(b"\n")
        else:
            connection.send(b"Blad! Brak wyniku!\n")
    else:
        connection.send(b"Blad wyrazenia! Nie mozna podac wyniku!\n")


ADDRESS = "localhost"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((ADDRESS,PORT))
client.listen(1)

connection, address = client.accept()
connection.send(b"==============KALKULATOR RPN==============\n")

while True:
    connection.send(b"Podaj wyrazenie: ")
    data = connection.recv(256)

    data_str = str(data.decode())

    if "q" in data_str:
        connection.close()
        connection, address = client.accept()
    else:
        kalkulatorFunc(str(data.decode()))


