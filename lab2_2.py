#program zlicza ilosc wystapien danych liter
znaki = {}

with open("tekst.txt") as file:
    for j in file:
        #usuwa ostatni znak z konca
        print(j[:-1])
        for i in j:
            #zmien wszystkie znaki na male
            i = i.lower()
            #jesli znak jest juz w zmiennej
            if i in znaki:
                znaki[i] += 1
                #w przeciwnym wypadku dodaj go
            else:
                znaki[i] = 1

print("Liczba wystapien:", znaki)


