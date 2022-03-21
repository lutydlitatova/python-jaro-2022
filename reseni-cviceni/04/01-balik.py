"""
Uvažuj, že navrhuješ software pro zásilkovou společnost.

- Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno. První dva atributy nastav pomocí parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.
- Připoj ke třídě funkci deliver, která změní hodnotu parametru doruceno na True.
- Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
- Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.
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
    

balik = Balik('Strasnicka 100, Praha 10', 10)
balik.deliver()
print(balik)
