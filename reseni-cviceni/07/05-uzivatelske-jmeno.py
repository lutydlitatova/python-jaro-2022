import re

uzivatelske_jmeno = input("Zadejte uzivatelske jmeno: ")

uzivatelske_jmeno_re = re.compile("\w{1,8}")  # Nebo ještě přesněji, re.compile("[a-z]{1,8}")
if uzivatelske_jmeno_re.fullmatch(uzivatelske_jmeno):
    print("Uživatelské jméno je v pořádku.")
else:
    print("Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé.")