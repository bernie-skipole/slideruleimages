import xml.etree.ElementTree as ET

import math

from . import draw


def addTscale(rl, rightmove, zero) -> ET.Element:
    "Adds the T scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # T mark
    if zero:
        ty = "50"
    else:
        ty = "70"
    Tmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":ty, "fill":"black", "font-size":"24"})
    Tmark.text = "T"

    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin

    # x mark
    if zero:
        yx = "40"
    else:
        yx = "65"
    xmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 12), "y":yx,"fill":"black", "font-size":"16"})
    xmark.text = "tan"

    # 45 mark
    draw.line(doc, 60, m+c, zero, col="black")
    draw.text(doc, "45", m+c, zero, 78, 65, 18)


    for r in range(57, 450):
        # r is 57 to 449   - this is along rule length
        x = r/10            # x is 5.7 to 44.99   degrees
        dx = math.tan(math.radians(x))*10
        xpos = c + m*math.log10(dx)
        length = 0
        textstr = ''
        fontsize = 16
        y0 = 68
        y1 = 55
        if r % 100 == 0: # x = 10, 20, 30, 40
            length = 50
            textstr = str(round(x))
            fontsize = 18
        elif r % 50 == 0:  # x = 15, 25, 35 
            length = 40
            y0 = 55
            y1 = 45
            textstr = str(round(x))
            fontsize = 14
        elif r % 10 == 0: # x = 6, 7, 8 ....
            length = 30
            if r < 200:   # up to x = 19
                y0 = 42
                y1 = 34
                textstr = str(round(x))
                fontsize = 14
        elif r % 5 == 0:       # at 0.5 markers
            length = 20
        elif r < 100: # at 0.1 markers
            length = 15
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    return doc

