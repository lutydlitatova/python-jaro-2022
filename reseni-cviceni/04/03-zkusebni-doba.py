"""
U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

- Rozšiř metodu __init__ třídy Zamestnanec o parametr zkusebni_doba, který bude typu bool. Tuto hodnotu ulož jako atribut třídy Zamestnanec.
- Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text "Je ve zkušební době".
"""

class Zamestnanec:
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.zkusebni_doba = zkusebni_doba
        self.pocet_dni_dovolene = 30

    def __str__(self):
        info = f"Zamestnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."
        if self.zkusebni_doba:
            return info + " Zamestnanec je ve zkusebni dobe."
        else:
            return info + " Zamestnanec neni ve zkusebni dobe."

    def cerpej_dovolenou(self, pocet_dni):
        if self.pocet_dni_dovolene >= pocet_dni:
            self.pocet_dni_dovolene -= pocet_dni
            print(f"Prejeme peknou dovolenou. Zbyva vam {self.pocet_dni_dovolene} dni dovolene")
        else:
            print(f"Nemate dost dovolene, maximalne muzete cerpat {self.pocet_dni_dovolene} dni dovolene.")


frantisek = Zamestnanec('Frantisek Novak', 'konstrukter', True)
print(frantisek)