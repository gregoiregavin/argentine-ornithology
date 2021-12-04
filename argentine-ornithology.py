import re

with open ('files/1_birds.txt', 'r', encoding="utf8") as sourcefile :
    sourcetext = sourcefile.read()

Orders = re.findall('Order [ILVX]*\. [A-Z \Æ]*\.', sourcetext)
print(len(Orders)) # OK -> 18 results
print(Orders)

#Famille = re.findall('Fam\. [IVX]*\. [A-Z \Æ]*', sourcetext)
#print(len(Famille))
#print(Famille)

#NomLatin = re.findall('[0-9]{3}\. [A-Z \Æ]*[, [| /(]', sourcetext)
#print(len(NomLatin))
#print(NomLatin)

# L'idée serait peut être de récupérer le nom latin
# avec le nom du scientifique, puis de le récupérer de la liste
# NomScientifique = re.findall('(?<=[0-9]{3}\.),', sourcetext)
# print(len(NomScientifique))
# print(NomScientifique)

## It's useful to store it in a list
