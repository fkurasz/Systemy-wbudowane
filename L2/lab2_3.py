
# W liście liczb znajdź liczbę najmniejszą oraz jej pozycję.
# listy, enum

lista = [46, 53, 62, 8, 36, 45, 10, 90, 18, 26]

enum = enumerate(lista)

# wyswietla liste
for i in enum:
    print(i)

print("Indeks: ",lista.index(min(lista))," Wartosc: ",min(lista))


