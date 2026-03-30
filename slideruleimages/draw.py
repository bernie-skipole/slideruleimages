"""
This provides two functions to draw a vertical line, and to place text
"""

import xml.etree.ElementTree as ET


def line(doc, length, xpos, zero, col="black"):
    """Creates a vertical line
       doc is the scale element to which this line will be inserted
       length is the length of the vertical line
       xpos is the x position
       zero is True if line starts at top of scale
       col is the colour of the line"""
    if not length:
        return

    if zero:
        y1 = '0'
        y2 = str(length)
    else:
        y1 = str(100-length)
        y2 = '100'

    # get xpos to the nearest .25
    xpos = str( round(xpos*4)/4.0 )
    vline = {"x1":xpos, "y1":y1, "x2":xpos, "y2":y2, "style":f"stroke:{col};stroke-width:1"}
    ET.SubElement(doc, 'line', vline)


def text(doc, textstr, xpos, zero, y0, y1, fontsize, col='black'):
    "Adds text"
    if not textstr:
        return

    if len(textstr) == 1:
        textpos = round(xpos - 4)    #  textpos This is in pixels
    else:
        textpos = round(xpos - 6)    # three characters, such as 1.5

    if zero:
        texty = y0
    else:
        texty = 100-y1
    
    tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":col, "font-size":str(fontsize)})
    tel.text = textstr

