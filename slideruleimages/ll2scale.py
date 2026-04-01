import xml.etree.ElementTree as ET

import math

from . import draw


def addLL2scale(rl, rightmove, zero) -> ET.Element:
    "Adds the LL2 scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # LL2 mark
    if zero:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"40", "fill":"black", "font-size":"24"})
        LLmark.text = "LL"
        LL2mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"42", "fill":"black", "font-size":"12"})
        LL2mark.text = "2"
    else:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"70", "fill":"black", "font-size":"24"})
        LLmark.text = "LL"
        LL2mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"72", "fill":"black", "font-size":"12"})
        LL2mark.text = "2"


    # e**0.1x mark
    if zero:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"44","fill":"black", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 22), "y":"36","fill":"black", "font-size":"12"})
        exmark.text = "0.1x"
    else:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"64","fill":"black", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 22), "y":"56","fill":"black", "font-size":"12"})
        exmark.text = "0.1x"


    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin + rl.scalewidth

    xpos = m*math.log10(math.log(1.11)) + c
    textstr = "1.11"
    fontsize = 14
    y0 = 40
    y1 = 30
    draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    xpos = m*math.log10(math.log(1.13)) + c
    textstr = "1.13"
    fontsize = 14
    y0 = 40
    y1 = 30
    draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    xpos = c
    textstr = "e"
    fontsize = 14
    y0 = 60
    y1 = 50
    draw.text(doc, textstr, xpos+2, zero, y0, y1, fontsize)
    length = 40
    draw.line(doc, length, xpos, zero, col="black")


    # x from 1.105 to 2.0 in steps of 0.001
    for r in range(1105, 2000):
        textstr = ''
        length = 0
        x = r/1000.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            length = 45
            textstr = str(x)
            fontsize = 16
            y0 = 60
            y1 = 50
        elif r % 50 == 0:
            length = 35
            if r < 1500:
                textstr = str(x)
                fontsize = 14
                y0 = 50
                y1 = 40
        elif r % 10 == 0:
            length = 25
        elif r % 5 == 0 and r<1300:
            length = 20
        elif r < 1140:
            length = 15
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    # x from 2 to 2.7 in steps of 0.01
    for r in range(200, 271):
        textstr = ''
        length = 0
        x = r/100.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 10 == 0:
            length = 45
            if r < 240 or r==250:
                textstr = str(x)
                fontsize = 12
                y0 = 60
                y1 = 50
        elif r % 5 == 0:
            length = 35
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    return doc





