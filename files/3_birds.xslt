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
                <table border="1">
                    <tr bgcolor="#9acd32">
                        <th>Order:</th>
                        <th>Family:</th>
                        <th>Bird:</th>
                        <th>Habitat:</th>
                    </tr>
                    <xsl:for-each select="document/argentine-ornithology/order/family/bird/habitat">
                    <tr>
                        <td><xsl:value-of select="order"/></td>
                        <td><xsl:value-of select="family"/></td>
                        <td><xsl:value-of select="bird"/></td>
                        <td><xsl:value-of select="habitat"/></td>
                    </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>