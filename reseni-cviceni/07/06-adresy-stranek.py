import re

rady = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org nabízí tutoriál i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky, rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů víceméně nemá konkurenci. 
Určitě ale sleduj i web https://www.czechitas.cz a přihlašuj se na naše kurzy!
"""


regex_email = re.compile(r"https?://(?:w{3}\.)?(?:[a-z]+\.)+(?:com|org|cz)")
emaily = [email + '\n' for email in regex_email.findall(rady)]

with open('adresy.txt', 'w') as vystup:
    vystup.writelines(emaily)