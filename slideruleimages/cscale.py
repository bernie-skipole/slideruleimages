import xml.etree.ElementTree as ET

import math

from . import draw


def addCscale(rl, rightmove, zero):
    "Adds the C scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # C mark
    if zero:
        cy = "50"
    else:
        cy = "70"
    Cmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":cy, "fill":"black", "font-size":"24"})
    Cmark.text = "C"

    # scaling with y = mx+c for first half of scale
    m = rl.scalewidth
    c = rightmove + rl.leftmargin

    # Pi mark
    xpos = m*math.log10(math.pi) + c
    draw.line(doc, 40, xpos, zero)
    draw.text(doc, "\u03C0", xpos, zero, 52, 47, 16)

    # x mark
    if zero:
        yx = "40"
    else:
        yx = "65"
    xmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 12), "y":yx,"fill":"black", "font-size":"16"})
    xmark.text = "x"

    for r in range(100, 1000+1):
        # r is 100 to 1000   - this is along rule length
        # x is 1 to 10 inclusive
        x = r/100
        xpos = rightmove + rl.leftmargin + rl.scalewidth*math.log10(x)
        length = 0
        textstr = ''
        fontsize = 16
        y0 = 95
        y1 = 80
        if r == 100:                   # at x == 1, r = 100
            length = 70
            textstr = "1"
            fontsize = 18
        elif r == 1000:            # at x == 10, r= 1000
            length = 70
            textstr = "10"
            fontsize = 18
        elif r % 100 == 0:         # at x = 2, 3, etc 
            length = 60
            textstr = str(round(x))
            fontsize = 18
            y0 = 80
            y1 = 66
        elif r % 50 == 0:         # at x = 1.5, 2.5, 3.5, etc 
            length = 50
            textstr = str(x)
            fontsize = 14
            y0 = 65
            y1 = 55
        elif r % 10 == 0:         # at x = 1.1, 1.2, etc 
            length = 30
            if r < 200:           # only do text for x<2, r <200  
                textstr = str(x)
                fontsize = 12
                y0 = 40
                y1 = 33
        elif r < 400:             # x < 4, r < 400
            if r % 5 == 0:        # at x =1.05, 1.15, etc
                length = 20

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    return doc

