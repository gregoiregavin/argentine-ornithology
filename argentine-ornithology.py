import re

with open ('files/1_birds.txt', 'r', encoding="utf8") as sourcefile :
    sourcetext = sourcefile.read()

#Orders = re.findall('Order\s[IVXL]*\.\s[A-Z \Æ]*\.', sourcetext)
#print(len(Orders)) # OK -> 18 orders
#print(Orders)

#Families = re.findall('Fam\.\s[IVXL]*\.\s[A-Z \Æ]*', sourcetext)
#print(len(Families)) # OK -> 35 families
#print(Families)

ScientificName = re.findall('[0-9]{3}\.\s[A-Z \Æ]{7,}', sourcetext)
print(len(ScientificName)) # OK -> 202 birds
print(ScientificName)

# L'idée serait peut être de récupérer le nom latin
# avec le nom du scientifique, puis de le récupérer de la liste
# NomScientifique = re.findall('(?<=[0-9]{3}\.),', sourcetext)
# print(len(NomScientifique))
# print(NomScientifique)

## It's useful to store it in a list

# Order((.|\n)*)
