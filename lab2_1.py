#program zlicza ilosc wystapien danych liter

napis = input("Wprowadz dowolny ciag znakow: ")
znaki = {}

for i in napis:
    #zmien wszystkie znaki na male
    i = i.lower()
        #jesli znak jest juz w zmiennej
    if i in znaki:
        znaki[i] += 1
        #w przeciwnym wypadku dodaj go
    else:
        znaki[i] = 1

print("Liczba wystapien:", znaki)

