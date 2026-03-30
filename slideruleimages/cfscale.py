import xml.etree.ElementTree as ET

import math

from . import draw


def addCFscale(rl, rightmove, zero) -> ET.Element:
    "Adds the CF scale to the slider, returns the scale element"

    doc = ET.Element('g')

    # CF mark
    if zero:
        cfy = "40"
    else:
        cfy = "75"
    CFmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":cfy, "fill":"black", "font-size":"24"})
    CFmark.text = "CF"

    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin

    # Pi mark, positioned at left of the scale, at c
    draw.line(doc, 40, c, zero)
    draw.text(doc, "\u03C0", c, zero, 55, 45, 16)

    # pix mark
    if zero:
        pixmark = ET.SubElement(doc, 'text', {"x":str(c + m + 12), "y":"40","fill":"black", "font-size":"16"})
    else:
        pixmark = ET.SubElement(doc, 'text', {"x":str(c + m + 12), "y":"70","fill":"black", "font-size":"16"})
    pixmark.text = "\u03C0x"

    # start r
    # r = (x-1)x100
    # r = (3.13 -1)x 100  -- 3.13 to get beyond 3.1 but befor pi
    # r = 213

    # end r
    # r = (31 - 1)x 100
    # r = 3000


    for r in range(313, 3100+1):
        # r is 313 to 3100
        # x is 3.13 to 31 inclusive
        x = r/100
        # move to the left by log pi
        xpos = rightmove + rl.leftmargin + rl.scalewidth*math.log10(x) - rl.scalewidth*math.log10(math.pi)
        length = 0
        textstr = ''
        fontsize = 16
        y0 = 90
        y1 = 76
        if r == 1000 or r == 2000 or r == 3000:            # at x == 10,20,30
            length = 70
            textstr = str(round(x/10))
            fontsize = 18
        elif r % 100 == 0 and r<1000:         # at x = 2, 3, etc up to x<10
            length = 60
            textstr = str(round(x))
            fontsize = 18
            y0 = 80
            y1 = 67
        elif r == 1500 or r == 2500:                  # at x = 15, 25, r = 1500, 2500
            length = 60
            z = x/10.0 
            textstr = f"{z:.1f}"    # displayed as 1.5, 2.5
            fontsize = 14
            y0 = 75
            y1 = 65
        elif r % 100 == 0:         # at x = 11, 12, etc, and r must be greater than 900, x>10
            length = 30
            if r < 2000:           # only do text for x<20, r <2000
                z = x/10.0 
                textstr = f"{z:.1f}"    # displayed as 1.1, 1.2
                fontsize = 12
                y0 = 45
                y1 = 35
        elif r % 50 == 0:         # at x = 1.5, 2.5, 3.5, etc However text only at x<10
            if r < 1000:
                length = 50         # text and long length x < 10, short length only at x>10
                textstr = str(x)
                fontsize = 14
                y0 = 65
                y1 = 55
            else:
                length = 20           
        elif r % 10 == 0 and r<1000:         # at x = 1.1, 1.2, etc up to x<10, r<1000 
            length = 30

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    return doc

