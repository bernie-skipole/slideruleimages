"""
This provides two functions to draw a vertical line, and to place text
"""

import xml.etree.ElementTree as ET


def line(doc, length, xpos, ybot, col="black"):
    """Creates a vertical line
       doc is the scale element to which this line will be inserted
       length is the length of the vertical line
       ybot is the ending y position
       xpos is the x position
       col is the colour of the line"""
    if length:
        # get xpos to the nearest .25
        xpos = round(xpos*4)/4.0
        vline = {"x1":str(xpos), "y1":str(ybot), "x2":str(xpos), "y2":str(ybot-length), "style":f"stroke:{col};stroke-width:1"}
        ET.SubElement(doc, 'line', vline)


def text(doc, textstr, xpos, texty, fontsize):
    "Adds text"
    if textstr:
        if len(textstr) == 1:
            textpos = round(xpos - 4)    #  textpos This is in pixels
        else:
            textpos = round(xpos - 6)    # three characters, such as 1.5
        
        tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
        tel.text = textstr

