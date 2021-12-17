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

    <xsl:template match="order|family|bird|habitat">
    <hr /> <xsl:apply-templates />
     <br/>
    </xsl:template>
   
    <xsl:template match="order">
    <p style="color:purple"> Order: <xsl:apply-templates /></p>
     <br/>
    </xsl:template>
 
    <xsl:template match="family">
     <p style="color:green"> Family: <xsl:apply-templates /></p>
     <br/>
    </xsl:template>

    <xsl:template match="bird">
     <p style="color:red"> Bird: <xsl:apply-templates /></p>
     <br/>
    </xsl:template>

    <xsl:template match="habitat">
    <p style="color:blue"> Habitat: <xsl:apply-templates /></p>
     <br/>
    </xsl:template>
   
</xsl:stylesheet>