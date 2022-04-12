import re

uzivatelske_jmeno = input("Zadejte uzivatelske jmeno: ")

uzviatelske_jmeno_re = re.compile("\w{1,8}")
if uzviatelske_jmeno_re.fullmatch(uzivatelske_jmeno):
    print("Uživatelské jméno je v pořádku.")
else:
    print("Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé.")