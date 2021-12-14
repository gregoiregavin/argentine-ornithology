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
    Order: <p style="color:purple"><xsl:apply-templates /></p>
     <br/>
    </xsl:template>
 
    <xsl:template match="order/family">
    Family: <p style="color:green"><xsl:apply-templates /></p>
     <br/>
    </xsl:template>

    <xsl:template match="order/family/bird">
    Bird: <p style="color:red"><xsl:apply-templates /></p>
     <br/>
    </xsl:template>

    <xsl:template match="order/family/bird/habitat">
    Habitat: <p style="color:blue"><xsl:apply-templates /></p>
     <br/>
    </xsl:template>
   
</xsl:stylesheet>