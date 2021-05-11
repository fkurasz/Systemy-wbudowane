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


stos = []

kalkulator = KalkulatorRPN()

while True:
    dzialanie = input("Podaj wyrazenie: ")
    if dzialanie == 'q':
        break
    wyrazenie = dzialanie.split(' ')
    # podane wyrazenie podzielone przez spacje
    # Podaj wyrazenie: 2 2 + 2 *
    # ['2', '2', '+', '2', '*']

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

            if wyrazenie[x] == '+':
                kalkulator.dodawanie(b, a)
                stos.append(kalkulator.wynik)

            if wyrazenie[x] == '-':
                kalkulator.odejmowanie(b, a)
                stos.append(kalkulator.wynik)
            
            if wyrazenie[x] == '*':
                kalkulator.mnozenie (b, a)
                stos.append(kalkulator.wynik)
            
            if wyrazenie[x] == '/':
                kalkulator.dzielenie (b, a)
                stos.append(kalkulator.wynik)

    if stos:
        if len(stos) > 0:
            print("Wynik: ", stos[-1])
        else:
            print("Blad! Brak wyniku!")
    else:
        print("Blad wyrazenia! Nie mozna podac wyniku!")