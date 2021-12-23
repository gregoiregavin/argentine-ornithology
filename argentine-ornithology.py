import os
import re
import fileinput
import lxml.etree as ET
#from utils.utils import checkResults

inputFile = 'files/1_birds.txt'
xmlFile = 'files/2_birds.xml'
xsltFile = 'files/3_birds.xslt'
htmlFile = 'files/4_birds.html'

# Vars for regex results check
#countOrders = 0
#countFamilies = 0
#countBirds = 0
#countHabs = 0

# Create the XML tree that we're going to populate
tree = ET.ElementTree(element = ET.Element('document'))
root = tree.getroot()

# Adding a basic (and kind of fake) TEI header
teiHeader = ET.Element('teiHeader')
root.append(teiHeader)

fileDesc = ET.Element('fileDesc')
teiHeader.append(fileDesc)

titleStmt = ET.Element('titleStmt')
fileDesc.append(titleStmt)

title = ET.Element('title')
title.text = 'Argentine ornithology - Ingénierie documentaire (2021)'
titleStmt.append(title)

respStmt = ET.Element('respStmt')
titleStmt.append(respStmt)

resp = ET.Element('resp')
resp.text = 'compiled by'
respStmt.append(resp)

name = ET.Element('name')
name.text = "Séverine Bochatay, Adrien Coulon, Grégoire Gavin"
respStmt.append(name)

publicationStmt = ET.Element('publicationStmt')
fileDesc.append(publicationStmt)

distributor = ET.Element('distributor')
distributor.text = 'Project Gutenberg'
publicationStmt.append(distributor)

sourceDesc = ET.Element('sourceDesc')
fileDesc.append(sourceDesc)

bibl = ET.Element('bibl')
bibl.text = 'Argentine Ornithology, Volume 2 (of 2) by W. H. Hudson and Philip Lutley Sclater'
sourceDesc.append(bibl)

ornithology = ET.Element('argentine-ornithology')
root.append(ornithology)

# Opens the source file and read it line by line to populate
#for line in fileinput.input(files=inputFile): ## Works on MacOS
for line in fileinput.input(files=inputFile, encoding="UTF-8"): ## Works on Windows  
    # Order match
    m = re.match('Order\s([IVXL]*)\.\s([A-Z \Æ]*)\.', line)
    if m:
        order = ET.SubElement(ornithology, 'order', attrib = {'n': m.group(1)})
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
if os.path.isfile(xmlFile):
    open(xmlFile, 'w').close()

# Write the tree into that well formed XML file
tree.write(xmlFile, encoding='utf-8', xml_declaration = True)

# Parse the XML and XSLT files 
xml = ET.parse(xmlFile)
xslt = ET.parse(xsltFile)

# Transform the XML file with XSLT
transform = ET.XSLT(xslt)
newdom = transform(xml)

# Erase HTML file content if existing
if os.path.isfile(htmlFile):
    open(htmlFile, 'w').close()

# Write the new generated DOM in an HTML file
newdom.write(htmlFile, encoding='utf-8')
