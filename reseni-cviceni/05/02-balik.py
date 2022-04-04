"""
Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

- Vytvoř třídu CennyBalik, která dědí od třídy Balik. CennyBalik má navíc atribut hodnota, ostatní atributy dědí od třídy Balik.
- Atribut hodnota nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Balik.
- Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.
"""

class Balik():
    def __init__(self, adresa, hmotnost, doruceno=False):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = doruceno
    
    def deliver(self):
        self.doruceno = True
    
    def __str__(self):
        if self.doruceno:
            return f"Balik s adresou {self.adresa} o hmotnosti {self.hmotnost}kg byl dorucen."
        else:
            return f"Balik s adresou {self.adresa} o hmotnosti {self.hmotnost}kg nebyl dorucen."


class CennyBalik(Balik):
    def __init__(self, adresa, hmotnost, hodnota, doruceno=False):
        super().__init__(adresa, hmotnost, doruceno)
        self.hodnota = hodnota

balik = Balik('Strasnicka 10', 10)
print(balik)

cennybalik = CennyBalik('Strasnicka 20', 5, 1000)
print(cennybalik)
print(cennybalik.hodnota)
