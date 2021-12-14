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
        <xsl:apply-templates select="order/family"/>
        <xsl:apply-templates select="order/family/bird"/>
        <xsl:apply-templates select="order/family/bird/habitat"/>
        </p>
    </xsl:template>
    
    <xsl:template match="order">
    Order: <span style="color:#ff0000">
    <xsl:value-of select="."/></span>
    <br />
    </xsl:template>

    <xsl:template match="order/family">
    Family: <span style="color:#00ff00">
    <xsl:value-of select="."/></span>
    <br />
    </xsl:template>

    <xsl:template match="order/family/bird">
    Bird: <span style="color:#0000ff">
    <xsl:value-of select="."/></span>
    <br />
    </xsl:template>

    <xsl:template match="order/family/bird/habitat">
    Habitat: <span style="color:#ff0000">
    <xsl:value-of select="."/></span>
    <br />
    </xsl:template>
    

</xsl:stylesheet>