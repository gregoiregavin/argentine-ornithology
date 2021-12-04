import re

with open ('files/1_birds.txt', 'r', encoding="utf8") as ca :
    text = ca.read()

Order = re.findall('Order [ILVX]*\. [A-Z ]*\.', text)
print(len(Order))
print(Order)

Famille = re.findall('Fam\. [IVX]*\. [A-Z \Æ]*', text)
print(len(Famille))
print(Famille)

NomLatin = re.findall('[0-9]{3}\. [A-Z \Æ]*[, [| /(]', text)
print(len(NomLatin))
print(NomLatin)

# L'idée serait peut être de récupérer le nom latin
# avec le nom du scientifique, puis de le récupérer de la liste
# NomScientifique = re.findall('(?<=[0-9]{3}\.),', text)
# print(len(NomScientifique))
# print(NomScientifique)

## It's useful to store it in a list
