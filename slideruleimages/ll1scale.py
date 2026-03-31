import xml.etree.ElementTree as ET

import math

from . import draw

def addLL1scale(rl, rightmove, zero) -> ET.Element:
    "Adds the LL1 scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # LL1 mark
    if zero:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"40", "fill":"black", "font-size":"24"})
        LLmark.text = "LL"
        LL1mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"42", "fill":"black", "font-size":"12"})
        LL1mark.text = "1"
    else:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"70", "fill":"black", "font-size":"24"})
        LLmark.text = "LL"
        LL1mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"72", "fill":"black", "font-size":"12"})
        LL1mark.text = "1"

    # e**0.01x mark
    if zero:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 6), "y":"42","fill":"black", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"34","fill":"black", "font-size":"12"})
        exmark.text = "0.01x"
    else:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 6), "y":"64","fill":"black", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"56","fill":"black", "font-size":"12"})
        exmark.text = "0.01x"


    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin + rl.scalewidth + rl.scalewidth


    # x from 1.01 to 1.105 in steps of 0.0001
    for r in range(10100, 11051):   # 11051 to include 11050 due to range missing last value
        textstr = ''
        length = 0
        x = r/10000.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            length = 45
            textstr = str(x)
            fontsize = 16
            y0 = 60
            y1 = 50
        elif r % 50 == 0:
            length = 35
            if r < 10400:
                textstr = str(x)
                fontsize = 14
                y0 = 50
                y1 = 40
        elif r % 10 == 0:
            length = 25
        elif r % 5 == 0 and r<10400:
            length = 20
        elif r < 10120:
            length = 15
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)
    return doc


