import pandas

# Pomocí Pandas načti tuto tabulku jako DataFrame.
# Jako index zvol sloupec s názvem 'jméno'.

jmena = pandas.read_csv("jmena.csv")
jmena = jmena.set_index("jméno")
# print(jmena.head())

# 1. Vypište na konzoli informace o jménu Jiří.
print(jmena.loc["Jiří"])


# 2. Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
print(jmena.loc[["Martin", "Zuzana", "Josef"]])


# 3. Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
print(jmena.loc[:"Martin"])


# 4. Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
print(jmena.loc["Martin":"Tereza", "věk"])
print(jmena.loc["Martin":"Tereza"]["věk"])

# 5. Vypište průměrný věk a původ pro všechna jména od Libora dolů.
print(jmena.loc["Libor":, ["věk", "původ"]])
print(jmena.loc["Libor":][["věk", "původ"]])

# 6. Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
print(jmena.loc[:, "věk":"původ"])
