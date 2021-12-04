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
1. Clean-up of the source data
2. Data recovery with regex 
3. Creation of a well structured XML file
4. XSLT transformation to a clean HTML file

**Source** : https://www.gutenberg.org/ebooks/38957

**Dependencies** :
- [re - Regular expresion operations](https://docs.python.org/3/library/re.html)
- ...

## 1. Clean-up
The source file contains some metadata, notes and preface which are out of the scope of this project. The document also contains a table of content which would result to duplicates elements when extracting data with regular expressions. To avoid the duplicates, we **manually** remove all those elements and the table of content.

**Input** : [0_birds.txt](files/0_birds.txt)

**Output** : [1_birds.txt](files/1_birds.txt)

## 2. Data recovery

**Data structure**
Birds belongs to a Family, and Families belongs to an Order.

Each Bird has a scientific name (in latin), a common name, the name of the scientist(s) who discovered it and an habitat.

**Expected results**
As the table of content of the original document is humanly readable and accessible, we can predict the regex should return :
- 18 Orders
- 35 Families
- 204 Birds


## 3. XML generation
...

## 4. XSLT transformation
...