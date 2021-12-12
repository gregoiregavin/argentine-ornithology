Argentine ornithology (vol. II)
===============================

**Authors** : Séverine Bochatay, Adrien Coulon, Grégoire Gavin

_December 2021_

<figure>
    <img src="https://www.gutenberg.org/cache/epub/38957/images/plt11_lg.jpg" alt="CHÆTOCERCUS BURMEISTERI." width="350" />
    <figcaption>CHÆTOCERCUS BURMEISTERI (Burmeister's hummingbird)</figcaption>
</figure>


## Description
This project aims to collect some data from a simple TXT file and render them to a clean HTML file.
The following steps allows us to accomplish this :
1. [Clean-up of the source data](#1-clean-up)
2. [Data recovery with regex](#2-data-recovery)
3. [Creation of a well structured XML file](#3-xml-generation)
4. [XSLT transformation to a clean HTML file](#4-xslt-transformation)

**Source** : https://www.gutenberg.org/ebooks/38957

**Dependencies** :
- [re - Regular expresion operations](https://docs.python.org/3/library/re.html)
- [os](https://docs.python.org/3/library/os.html)
- [fileinput](https://docs.python.org/3/library/fileinput.html)
- [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)

## 1. Clean-up
The source file contains some metadata, notes, preface, and index which won't be used in the scope of this project. The document also contains a table of content which would result to duplicates elements when extracting data with regular expressions. To avoid the duplicates, we **manually** remove all those elements and the table of content.

**Input** : [0_birds.txt](files/0_birds.txt)

**Output** : [1_birds.txt](files/1_birds.txt)

## 2. Data recovery

### 2.1 Data structure

Birds belongs to a Family, and Families belongs to an Order.

Each Bird has a scientific name (in latin), a common name, the name of the scientist(s) who discovered it and an habitat.

### 2.2 Expected results

As the table of content of the original document is humanly readable and accessible, we can predict the regex should return :
- 18 Orders
- 35 Families
- 204 Birds

### 2.3 Test regex
From here, we're able to create and text the regular expressions to find our data. We checked the results with the [checkResults function](utils/utils.py) and found the following regex :

 - Get Orders : ```Order\s([IVXL]*)\.\s([A-Z \Æ]*)\.```
 - Get Families : ```^Fam\.\s([IVXL]+)\. (.+)$```
 - Get Birds : ```(?m)^(([0-9]{3})\. (.*))$``` (and scientific abbr. name)
 - Get Habitats : ```(?m)^(_Hab\._ (.*))$```

 _For some reason, it seems we find 205 birds instead of 204. No information is missing still._

## 3. XML structuration and generation
As the base document is well structured, we use [fileinput library](https://docs.python.org/3/library/fileinput.html) to go through the document line per line. Each time a match is found, we create the relative xml tag using [ElementTree API](https://docs.python.org/3/library/xml.etree.elementtree.html).

Also, we add a basic TEI header by creating ElementTree Elements using the [append()](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.append) function.

**Input** : [1_birds.txt](files/1_birds.txt)

**Output** : [3_birds.xml](files/3_birds.xml)

## 4. XSLT transformation
...
