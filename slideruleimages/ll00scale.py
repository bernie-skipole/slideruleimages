import xml.etree.ElementTree as ET

import math

from . import draw


def addLL00scale(rl, rightmove, zero) -> ET.Element:
    "Adds the LL00 scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # LL00 mark
    if zero:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"30", "fill":"red", "font-size":"24"})
        LLmark.text = "LL"
        LL00mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"34", "fill":"red", "font-size":"12"})
        LL00mark.text = "00"
    else:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"78", "fill":"red", "font-size":"24"})
        LLmark.text = "LL"
        LL00mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"80", "fill":"red", "font-size":"12"})
        LL00mark.text = "00"

    # e**-0.001x mark
    if zero:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 6), "y":"26","fill":"red", "font-size":"14"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"18","fill":"red", "font-size":"10"})
        exmark.text = "-0.001x"
    else:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 6), "y":"84","fill":"red", "font-size":"14"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"76","fill":"red", "font-size":"10"})
        exmark.text = "-0.001x"


    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin


    # 1/e^0.001x from 0.999 to 0.99

    for r in range(99900, 98990, -1):  # 99900 to 99000
        textstr = ''
        length = 0
        x = r/100000               # 0.999 to 0.990
        xpos = c+m*math.log10(-1000*math.log(x))
        fontsize = 16
        offset = 5          # moves displayed numbers by a bit
        if r == 99900:
            length = 35
            textstr = str(x)
            fontsize = 16
            y0 = 50
            y1 = 40
        elif r % 100 == 0:
            length = 30
            if r != 99100:
                textstr = str(x)
                fontsize = 16
                y0 = 45
                y1 = 35
                offset = 10
        elif r % 50 == 0:
            length = 25
            if r > 99600:
                textstr = str(x)
                fontsize = 14
                y0 = 40
                y1 = 30
                offset = 10
        elif r % 10 == 0:
            length = 20
        elif r % 5 == 0 and r > 99600:
            length = 15
        elif r > 99880:
            length = 10

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos-offset, zero, y0, y1, fontsize, col="red")

    return doc





