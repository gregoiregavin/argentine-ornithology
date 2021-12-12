import re
import fileinput

with open ('files/1_birds.txt', 'r', encoding="utf8") as sourcefile :
    sourcetext = sourcefile.read()
import xml.etree.ElementTree as ET

# Create the XML tree that we're going to populate
tree = ET.ElementTree(element = ET.Element('document'))
root = tree.getroot()

for line in fileinput.input(encoding='utf-8'):
    m = re.match(r'^Order\s([IVXL]+)\.', line)
    if m:
        print(line)
        order = ET.SubElement(root, 'order', attrib = {'n': m.group(1)})

    m = re.match(r'^Fam\.\s([IVXL]+)\. (.+)$', line)
    if m:
        print(line)
        family = ET.SubElement(order, 'family', attrib = {'n': m.group(1)})
        family.text = m.group(2)
        
    m = re.match(r'(?m)^([0-9]{3}\. .*)$', line)
    if m:
        print(line)
        family = ET.SubElement(order, 'nom', attrib = {'n': m.group(1)})
        family.text = m.group(3)
        
    m = re.match(r'(?m)^(_Hab\._ .*)$', line)
    if m:
        print(line)
        family = ET.SubElement(order, 'habitat', attrib = {'n': m.group(1)})
        family.text = m.group(4)

# Make the output readable
ET.indent(tree)

# Write the XML tree to a file
tree.write('output.xml', encoding = 'utf-8')

#hello


# TEST 1
# for order in (orders):
#    families = re.findall('('+order+')*(Fam\.\s[IVXL]*\.\s[A-Z \Æ]*)', sourcetext)
#    print("\n================================\n"+order+"\n"+"================================\n")
#    for family in (families):
#        print(family)

# TEST PIOTROWSKI   
#for order in fileinput.input(files=('files/1_birds.txt'), encoding='utf-8'):
   # if re.match('Order\s[IVXL]*\.\s[A-Z \Æ]*\.', order):
        #families = re.findall('(Fam\.\s[IVXL]*\.\s[A-Z \Æ]*)', sourcetext)
       # print("\n================================\n"+order+"\n"+"================================\n")
       # for family in (families):
           # print(family)

        

# test commentaire 

#Orders = re.findall('Order\s[IVXL]*\.\s[A-Z \Æ]*\.', sourcetext)
#print(len(Orders)) # OK -> 18 orders
#print(Orders)

#Families = re.findall('Fam\.\s[IVXL]*\.\s[A-Z \Æ]*', sourcetext)
#print(len(Families)) # OK -> 35 families
#print(Families)

#ScientificName = re.findall('[0-9]{3}\.\s[A-Z \Æ]{7,}', sourcetext)
#print(len(ScientificName)) # OK -> 202 birds
#print(ScientificName)

# L'idée serait peut être de récupérer le nom latin
# avec le nom du scientifique, puis de le récupérer de la liste
# NomScientifique = re.findall('(?<=[0-9]{3}\.),', sourcetext)
# print(len(NomScientifique))
# print(NomScientifique)

## It's useful to store it in a list

# Order((.|\n)*)

