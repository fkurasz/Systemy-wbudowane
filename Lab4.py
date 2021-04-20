

class Drukarka:
    nazwa = "Drukarka PRO2021"
    stan = False

    def Wlacz(self):
        print("Wlaczono ",self.nazwa)
        self.stan = True

    def Wylacz(self):
        print("Wylaczono ",self.nazwa)
        self.stan = False

    def Drukuj(self):
        print("Drukuje...")



obiekt = Drukarka()

obiekt.Wlacz()
obiekt.Drukuj()
obiekt.Wylacz()

