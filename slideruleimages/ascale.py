import xml.etree.ElementTree as ET

import math


def _vertical(length, xpos, ybot, col="black") -> dict:
    """length is the length of the vertical line
       ybot is the ending y position
       xpos is the x position
       col is the colour of the line"""
    # get xpos to the nearest .25
    xpos = round(xpos*4)/4.0
    return {"x1":str(xpos), "y1":str(ybot), "x2":str(xpos), "y2":str(ybot-length), "style":f"stroke:{col};stroke-width:1"}


def addAscale(rl, rightmove):
    "Adds the A scale to the rule, returns the scale element"

    ybot = 100 # y value of bot of scale

    doc = ET.Element('g')

    # A mark
    Amark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":str(ybot-30), "fill":"black", "font-size":"24"})
    Amark.text = "A"

    # scaling with y = mx+c for first half of scale
    m = rl.scalewidth/2.0
    c = rightmove + rl.leftmargin

    # Pi mark
    xpos = m*math.log10(math.pi) + c
    xpos = round(xpos*4)/4.0
    Pimark = ET.SubElement(doc, 'text', {"x":str(xpos-4), "y":str(ybot-47), "fill":"black", "font-size":"16"})
    Pimark.text = "\u03C0"
    ET.SubElement(doc, 'line', _vertical(40, xpos, ybot))

    # x mark
    xmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 12), "y":str(ybot-32),"fill":"black", "font-size":"16"})
    xmark.text = "x"
    x2mark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 20), "y":str(ybot-44),"fill":"black", "font-size":"12"})
    x2mark.text = "2"

    for r in range(10000, 100000+1):
        # r is 10000 to 100000   - this is along rule length
        # x is 1 to 10 inclusive
        x = r/10000
        xpos = m*math.log10(x)+c
        length = 0
        textstr = ''
        fontsize = 16
        texty = ybot-80
        if r == 100000:            # at x == 10, r = 100000
            length = 70
            textstr = "10"
            fontsize = 18
        elif r % 10000 == 0:         # at x = 1, 2, 3, etc 
            length = 60
            textstr = str(round(x))
            fontsize = 18
            texty = ybot-66
        elif r % 5000 == 0:         # at x = 1.5, 2.5, 3.5, etc 
            length = 50
            if r < 50000:
                textstr = str(x)
                fontsize = 14
                texty = ybot-55
        elif r % 1000 == 0 and r < 40000:         # at x = 1.1, 1.2, etc
            length = 30
        elif r % 500 == 0 and r < 20000:
            length = 20

        if length:
            vline = _vertical(length, xpos, ybot, col="black")
            ET.SubElement(doc, 'line', vline)
        if textstr:
            if len(textstr) == 1:
                textpos = round(xpos - 4)    #  textpos This is in pixels
            else:
                textpos = (xpos - 6)    # three characters, such as 1.5
            tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
            tel.text = textstr

    c = rightmove + rl.leftmargin + rl.scalewidth/2.0

    # Pi mark
    xpos = m*math.log10(math.pi) + c
    xpos = round(xpos*4)/4.0
    Pimark = ET.SubElement(doc, 'text', {"x":str(xpos-4), "y":str(ybot-47), "fill":"black", "font-size":"16"})
    Pimark.text = "\u03C0"
    ET.SubElement(doc, 'line', _vertical(40, xpos, ybot))

    for r in range(10001, 100000+1):
        # x is just over 1 to 10 inclusive
        x = r/10000
        xpos = m*math.log10(x)+c
        length = 0
        textstr = ''
        fontsize = 16
        texty = ybot-80
        if r == 100000:            # at x == 10, r = 100000
            length = 70
            textstr = "100"
            fontsize = 18
        elif r % 10000 == 0:         # at x = 2, 3, etc 
            length = 60
            textstr = str(round(x))
            fontsize = 18
            texty = ybot-66
        elif r % 5000 == 0:         # at x = 1.5, 2.5, 3.5, etc 
            length = 50
            if r < 50000:
                textstr = str(x)
                fontsize = 14
                texty = ybot-55
        elif r % 1000 == 0 and r < 40000:         # at x = 1.1, 1.2, etc
            length = 30
        elif r % 500 == 0 and r < 20000:
            length = 20

        if length:
            vline = _vertical(length, xpos, ybot, col="black")
            ET.SubElement(doc, 'line', vline)
        if textstr:
            if len(textstr) == 1:
                textpos = round(xpos - 4)    #  textpos This is in pixels
            else:
                textpos = (xpos - 6)    # three characters, such as 1.5
            tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
            tel.text = textstr

    return doc





