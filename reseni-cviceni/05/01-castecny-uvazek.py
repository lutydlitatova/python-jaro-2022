"""
Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, pro které bude vytvořena zvláštní třída. Vytvoř novou třídu Brigadnik, která bude dědit od třídy Zamestnanec a bude mít navíc atribut uvazek, který reprezentuje velikost úvazku oproti plnému. Přidej informaci o úvazku k výpisu informací do funkce __str__.
"""

class Zamestnanec:
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 30

    def __str__(self):
        return f"Zaměstnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."

    def cerpej_dovolenou(self, pocet_dni):
        if self.pocet_dni_dovolene >= pocet_dni:
            self.pocet_dni_dovolene -= pocet_dni
            print(f"Přejeme pěknou dovolenou. Zbývá vám {self.pocet_dni_dovolene} dní dovolené.")
        else:
            print(f"Nemáte dost dovolené, maximálně můžete čerpat {self.pocet_dni_dovolene} dní dovolené.")

class Brigadnik(Zamestnanec):
    def __init__(self, jmeno, pozice, uvazek):
        super().__init__(jmeno=jmeno, pozice=pozice)
        self.uvazek = uvazek
    
    def __str__(self):
        return super().__str__() + f" Velikost úvazku: {self.uvazek}."

karel = Brigadnik("Karel K.", "prodavač", 0.4)
print(karel)