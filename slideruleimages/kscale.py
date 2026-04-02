import xml.etree.ElementTree as ET

import math

from . import draw


def addKscale(rl, rightmove, zero):
    "Adds the K scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # K mark
    if zero:
        ky = "50"
    else:
        ky = "70"
    Kmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":ky, "fill":"black", "font-size":"24"})
    Kmark.text = "K"

    # x mark
    if zero:
        yx = "40"
        yx3 = "35"
    else:
        yx = "65"
        yx3 = "60"
    xmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 12), "y":yx,"fill":"black", "font-size":"16"})
    xmark.text = "x"
    x3mark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 20), "y":yx3,"fill":"black", "font-size":"12"})
    x3mark.text = "3"

    # 1000 mark
    xpos = rightmove  + rl.leftmargin + rl.scalewidth
    draw.line(doc, 60, xpos, zero, col="black")
    draw.text(doc, "1000", xpos, zero, 75, 66, 18)

    # scaling with y = mx+c
    m = rl.scalewidth/3.0
    c = rightmove + rl.leftmargin
    for part in ("1", "10", "100"):    # The scale has three equal parts

        # Pi mark
        xpos = m*math.log10(math.pi) + c
        draw.line(doc, 35, xpos, zero)
        draw.text(doc, "\u03C0", xpos, zero, 48, 40, 16)

        for r in range(100, 1000):
            # r is 100 to 999   - provides integer values
            # x is 1 to 10 not inclusive of the 1o
            x = r/100
            xpos = m*math.log10(x)+c
            length = 0
            textstr = ''
            fontsize = 16
            y0 = 75
            y1 = 66
            if r == 100:            # at x == 1, r = 100
                length = 60
                fontsize = 18
                textstr = part
            elif r % 100 == 0:         # at x = 2, 3, etc 
                length = 50
                textstr = str(round(x))
                fontsize = 18
                y0 = 66
                y1 = 54
            elif r % 50 == 0:         # at x = 1.5, 2.5, 3.5, etc 
                length = 40
                if r < 300:
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

        c += m # add m for next part

    return doc





