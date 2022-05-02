
opery = [
    "Figarova svatba", 
    "Don Giovanni", 
    "La Traviata",
    "Kouzelná flétna"
]


# * Pomocí chroustání seznamů (list comprehension) 
#   * Vytvoř seznam, který obsahuje počet znaků (včetně mezer) každého názvu opery.
print([len(nazev) for nazev in opery])

#   * Vytvoř seznam, který obsahuje počet slov (ta jsou oddělená mezerami) každého názvu opery.
print([len(nazev.split()) for nazev in opery])


autori = [
    "Mozart", 
    "Mozart", 
    "Verdi",
    "Mozart"
]


# * Přibyl nám seznam autorů oper. Jejich pozice odpovídá pozici názvů opery v proměnné `opery`. 
#   * Pomocí chroustání seznamů (list comprehension) vytvoř seznam, který bude obsahovat seznamy o dvou prvcích: `[nazev, autor]`. Prvek na pozici 0 by tak byl `["Figarova svatba", "Mozart"]`
  
print([[opery[i], autori[i]] for i in range(len(opery))])

#   * Pomocí chroustání slovníků (dict comprehension) vytvoř slovník, který bude obsahovat název opery jako klíč a autora jako hodnotu. Jeden ze záznamů by tak byl třeba `"Kouzelná flétna": "Mozart"`.

print({opery[i]:autori[i] for i in range(len(opery))})

#   * (Vyšší obtížnost) Vytvoř slovník, který bude obsahovat autory oper jako klíče a jejich díla jako hodnoty. Slovník bude mít dva klíče, a jejich hodnota bude vždy seznam řetězců (názvů děl):

vysledek = {}

for i in range(len(opery)):
    if autori[i] in vysledek:
        vysledek[autori[i]].append(opery[i])
    else:
        vysledek[autori[i]] = [opery[i]]

print(vysledek)
  
#   * (Vyšší obtížnost) Je možné, že v předchozí úloze bylo potřeba kontrolovat, jestli se ve slovníku klíč už nachází, anebo ne. Abychom se podmínce vyhli, můžeme použít `defaultdict` z modulu `collections`. Pomocí [dokumentace](https://docs.python.org/3/library/collections.html#defaultdict-objects) a [příkladu použití](https://docs.python.org/3/library/collections.html#defaultdict-examples) zkus upravit předchozí úlohu tak, abychom využili `defaultdict`.

from collections import defaultdict
vysledek = defaultdict(list)

for i in range(len(opery)):
    vysledek[autori[i]].append(opery[i])
    
print(vysledek)