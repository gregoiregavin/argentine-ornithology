<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     <xsl:template match="/">
        <html>
            <head>
                <title>Argentine ornithology</title>
            </head>
            <body>
                <h1>Argentine ornithology</h1>
                <h2>Authors : Séverine Bochatay, Adrien Coulon, Grégoire Gavin</h2>
                 <xsl:apply-templates/>  
            </body>
        </html>
    </xsl:template>

    <xsl:template match="argentine-ornithology">
    <p>
    <xsl:apply-templates select="order"/>  
    <xsl:apply-templates select="family"/>
    <xsl:apply-templates select="bird"/>
    <xsl:apply-templates select="habitat"/>
    </p>
    </xsl:template>

    <xsl:template match="order">
    Order: <span style="color:#00ff00">
    <xsl:value-of select="."/></span>
    <br />
    </xsl:template>

    <xsl:template match="family">
    Family: <span style="color:#ff0000">
    <xsl:value-of select="."/></span>
    <br />
    </xsl:template>

    <xsl:template match="bird">
    Bird: <span style="color:green">
    <xsl:value-of select="."/></span>
    <br />
    </xsl:template>

    <xsl:template match="habitat">
    Habitat: <span style="color:purple">
    <xsl:value-of select="."/></span>
    <br />
    </xsl:template>

</xsl:stylesheet>