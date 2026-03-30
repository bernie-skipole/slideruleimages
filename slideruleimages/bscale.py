import xml.etree.ElementTree as ET

import math

from . import draw


def addBscale(rl, rightmove, zero):
    "Adds the B scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # B mark
    if zero:
        by = "50"
    else:
        by = "70"
    Bmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":by, "fill":"black", "font-size":"24"})
    Bmark.text = "B"

    # scaling with y = mx+c for first half of scale
    m = rl.scalewidth/2.0
    c = rightmove + rl.leftmargin

    # Pi mark
    xpos = m*math.log10(math.pi) + c
    draw.line(doc, 40, xpos, zero)
    draw.text(doc, "\u03C0", xpos, zero, 52, 44, 16)

    # x mark
    if zero:
        yx = "40"
        yx2 = "35"
    else:
        yx = "65"
        yx2 = "60"
    xmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 12), "y":yx,"fill":"black", "font-size":"16"})
    xmark.text = "x"
    x2mark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 20), "y":yx2,"fill":"black", "font-size":"12"})
    x2mark.text = "2"

    for r in range(100, 1000+1):
        # r is 100 to 1000   - provides integer values
        # x is 1 to 10 inclusive
        x = r/100
        xpos = m*math.log10(x)+c
        length = 0
        textstr = ''
        fontsize = 16
        y0 = 75
        y1 = 66
        if r == 100:            # at x == 1, r = 100
            length = 60
            textstr = "1"
            fontsize = 18
        elif r == 1000:            # at x == 10, r = 1000
            length = 60
            textstr = "10"
            fontsize = 18
        elif r % 100 == 0:         # at x = 2, 3, etc 
            length = 50
            textstr = str(round(x))
            fontsize = 18
            y0 = 66
            y1 = 54
        elif r % 50 == 0:         # at x = 1.5, 2.5, 3.5, etc 
            length = 40
            if r < 500:
                textstr = str(x)
                fontsize = 14
                y0 = 55
                y1 = 44
        elif r % 10 == 0 and r < 400:         # at x = 1.1, 1.2, etc
            length = 30
        elif r % 5 == 0 and r < 200:
            length = 20

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    c = rightmove + rl.leftmargin + rl.scalewidth/2.0

    # Pi mark
    xpos = m*math.log10(math.pi) + c
    draw.line(doc, 40, xpos, zero)
    draw.text(doc, "\u03C0", xpos, zero, 52, 44, 16)


    for r in range(101, 1000+1):
        # x is just over 1 to 10 inclusive
        x = r/100
        xpos = m*math.log10(x)+c
        length = 0
        textstr = ''
        fontsize = 16
        y0 = 75
        y1 = 66
        if r == 1000:            # at x == 10, r = 1000
            length = 60
            textstr = "100"
            fontsize = 18
        elif r % 100 == 0:         # at x = 2, 3, etc 
            length = 50
            textstr = str(round(x))
            fontsize = 18
            y0 = 66
            y1 = 54
        elif r % 50 == 0:         # at x = 1.5, 2.5, 3.5, etc 
            length = 40
            if r < 500:
                textstr = str(x)
                fontsize = 14
                y0 = 55
                y1 = 44
        elif r % 10 == 0 and r < 400:         # at x = 1.1, 1.2, etc
            length = 30
        elif r % 5 == 0 and r < 200:
            length = 20

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    return doc





