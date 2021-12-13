<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Argentine ornithology</h2>  
  <xsl:apply-templates/>  
  </body>
  </html>
</xsl:template>

<xsl:template match="order">
  <p>
    <xsl:apply-templates select="family"/>  
  </p>
</xsl:template>

<xsl:template match="family">
  <p>
    <xsl:apply-templates select="bird"/>  
  </p>
</xsl:template>

<xsl:template match="bird">
  <p>
    <xsl:apply-templates select="habitat"/>  
  </p>
</xsl:template>

<xsl:template match="order">
  Order: <span style="color:#ff0000">
  <xsl:value-of select="."/></span>
  <br />
</xsl:template>

<xsl:template match="family">
  Family: <span style="color:#ff0000">
  <xsl:value-of select="."/></span>
  <br />
</xsl:template>

<xsl:template match="bird">
  Bird: <span style="color:#00ff00">
  <xsl:value-of select="."/></span>
  <br />
</xsl:template>

<xsl:template match="Habitat">
  Habitat: <span style="color:#ff0000">
  <xsl:value-of select="."/></span>
  <br />
</xsl:template>

</xsl:stylesheet>
