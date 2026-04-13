import xml.etree.ElementTree as ET

import math

from . import draw


def addSscale(rl, rightmove, zero) -> ET.Element:
    "Adds the S scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # S mark
    if zero:
        sy = "50"
    else:
        sy = "70"
    Smark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":sy, "fill":"black", "font-size":"24"})
    Smark.text = "S"

    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin

    # x mark
    if zero:
        yx = "40"
    else:
        yx = "65"
    xmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 12), "y":yx,"fill":"black", "font-size":"16"})
    xmark.text = "sin"

    # 90 mark
    draw.line(doc, 60, m+c, zero, col="black")
    draw.text(doc, "90", m+c, zero, 78, 65, 18)


    for r in range(560, 9000):
        # r is 560 to 8999   - this is along rule length
        x = r/100            # x is 5.6 to 89.99   degrees
        dx = math.sin(math.radians(x))*10
        xpos = c + m*math.log10(dx)
        length = 0
        textstr = ''
        fontsize = 16
        y0 = 68
        y1 = 55
        if r % 1000 == 0: 
            length = 50
            if r != 8000:
                textstr = str(round(x))
                fontsize = 18
        elif r % 500 == 0 and r < 8000: 
            length = 40
            if r < 6000:
                y0 = 55
                y1 = 45
                textstr = str(round(x))
                fontsize = 14
        elif r % 100 == 0 and r < 7000: 
            length = 30
            if r < 2000:
                y0 = 42
                y1 = 34
                textstr = str(round(x))
                fontsize = 14
        elif r % 50 == 0 and r < 4000: 
            length = 20
        elif r % 10 == 0 and r < 1000: 
            length = 15
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    return doc

