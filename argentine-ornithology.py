import os
import re
import fileinput
import xml.etree.ElementTree as ET
from utils.utils import checkResults

# Vars for regex results check
#countOrders = 0
#countFamilies = 0
#countBirds = 0
#countHabs = 0

# Create the XML tree that we're going to populate
tree = ET.ElementTree(element = ET.Element('document'))
root = tree.getroot()

# Opens the source file and read it line by line
for line in fileinput.input(files='files/1_birds.txt', encoding='utf-8'):
    
    # Order match
    m = re.match('Order\s([IVXL]*)\.\s([A-Z \Æ]*)\.', line)
    if m:
        order = ET.SubElement(root, 'order', attrib = {'n': m.group(1)})
        order.text = m.group(2)
        #countOrders+=1

    # Family match
    m = re.match('^Fam\.\s([IVXL]+)\. (.+)$', line)
    if m:
        family = ET.SubElement(order, 'family', attrib = {'n': m.group(1)})
        family.text = m.group(2)
        #countFamilies+=1
    
    # Bird match
    m = re.match('(?m)^(([0-9]{3})\. (.*))$', line)
    if m:
        nom = ET.SubElement(family, 'bird', attrib = {'n': m.group(2)})
        nom.text = m.group(3)
        #countBirds+=1
    
    # Habitat match
    m = re.match('(?m)^(_Hab\._ (.*))$', line)
    if m:
        habitat = ET.SubElement(nom, 'habitat')
        habitat.text = m.group(2)
        #countHabs+=1

# Check the results and print errors
#checkResults(countOrders, countFamilies, countBirds, countHabs)

# Make the output readable
ET.indent(tree)

# Erase XML file content if existing
if os.path.isfile('files/3_birds.xml'):
    open('files/3_birds.xml', 'w').close()

# Write the tree into that well formed XML file
tree.write('files/3_birds.xml', encoding='utf-8', xml_declaration = True)