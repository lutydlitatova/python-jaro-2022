import pandas

# Načti soubor tak, aby Pandas vyrobil číselný index.
jmena = pandas.read_csv("jmena.csv")

# 1. Vypiš všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
print(jmena[jmena["věk"] > 60])
# 2. Vypiš pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
print(jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)])
# 3. Vypiš jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
print(jmena[jmena["původ"].isin(["slovanský", "hebrejský"])])  # počet například pomocí .shape
# 4. Vypiš všechna jména, která mají svátek první 3 dny v prosinci.
print(jmena[jmena["svátek"].isin(["1.12", "2.12", "3.12"])])
