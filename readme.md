Argentine ornithology (vol. II)
===============================

**Authors**
- Séverine Bochatay
- Adrien Coulon
- Grégoire Gavin

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

**Input** : 0_birds.txt

**Output** : 1_birds.txt

## 2. Data recovery
...

## 3. XML generation
...

## 4. XSLT transformation
...