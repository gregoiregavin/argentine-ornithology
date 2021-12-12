import re
import fileinput
from utils.utils import checkResults

with open ('files/1_birds.txt', 'r', encoding="utf8") as sourcefile :
    sourcetext = sourcefile.read()
import xml.etree.ElementTree as ET

# For regex results check
countOrders = 0
countFamilies = 0
countBirds = 0

# Create the XML tree that we're going to populate
tree = ET.ElementTree(element = ET.Element('document'))
root = tree.getroot()


for line in fileinput.input(files='files/1_birds.txt', encoding='utf-8'):
    
    m = re.match('Order\s[IVXL]*\.\s[A-Z \Æ]*\.', line)
    if m:
        order = ET.SubElement(root, 'order', attrib = {'n': m.group()})
        countOrders+=1

    m = re.match('Fam\.\s[IVXL]*\.\s[A-Z \Æ]*', line)
    if m:
        family = ET.SubElement(order, 'family', attrib = {'n': m.group()})
        family.text = m.group()
        countFamilies+=1
        
    m = re.match(r'(?m)^([0-9]{3}\. .*)$', line)
    if m:
        print(line)
        nom = ET.SubElement(family, 'nom', attrib = {'n': m.group()})
        nom.text = m.group()
        
    m = re.match(r'(?m)^(_Hab\._ .*)$', line)
    if m:
        print(line)
        habitat = ET.SubElement(nom, 'habitat', attrib = {'n': m.group()})
        habitat.text = m.group()

# Check the result and print errors
checkResults(countOrders, countFamilies, countBirds)

# Make the output readable
ET.indent(tree)

# Write the XML tree to a file
tree.write('output.xml', encoding = 'utf-8')

#Orders = re.findall('Order\s[IVXL]*\.\s[A-Z \Æ]*\.', sourcetext)
#print(len(Orders)) # OK -> 18 orders
#print(Orders)

#Families = re.findall('Fam\.\s[IVXL]*\.\s[A-Z \Æ]*', sourcetext)
#print(len(Families)) # OK -> 35 families
#print(Families)

#ScientificName = re.findall('[0-9]{3}\.\s[A-Z \Æ]{7,}', sourcetext)
#print(len(ScientificName)) # OK -> 202 birds
#print(ScientificName)

