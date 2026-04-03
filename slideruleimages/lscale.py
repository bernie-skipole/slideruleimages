import xml.etree.ElementTree as ET

import math

from . import draw


def addLscale(rl, rightmove, zero):
    "Adds the L scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # L mark
    if zero:
        ly = "50"
    else:
        ly = "70"
    Lmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":ly, "fill":"black", "font-size":"24"})
    Lmark.text = "L"

    m = rl.scalewidth/10
    c = rightmove + rl.leftmargin

    # logx mark
    if zero:
        yx = "30"
    else:
        yx = "80"
    logxmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 6), "y":yx,"fill":"black", "font-size":"16"})
    logxmark.text = "log x"

    for r in range(201):
        # r is 0 to 200   - provides integer values
        # x is 0 to 10 inclusive
        x = r/20
        xpos = m*x+c
        length = 0
        textstr = ''
        fontsize = 16
        y0 = 66
        y1 = 54
        if r % 20 == 0:         # at x = 1, 2, 3, etc 
            length = 50
            textstr = str(round(x))
            fontsize = 18
        elif r % 10 == 0:         # at x = 0.5, 1.5, 2.5, 3.5, etc 
            length = 40
            textstr = str(x)
            fontsize = 14
            y0 = 55
            y1 = 44
        elif r % 2 == 0:         # at x = 0.1, 0.2, 0.3 etc
            length = 30
        else:
            length = 20          # at x = 0.05, 0.15, 0.25 etc

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    return doc





