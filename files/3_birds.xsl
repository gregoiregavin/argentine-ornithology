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
                <xsl:for-each select="document/argentine-ornithology/order/family">
                    <span>
                        <xsl:value-of select="bird"/>
                    </span>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>