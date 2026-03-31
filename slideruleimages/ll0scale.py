import xml.etree.ElementTree as ET

import math

from . import draw


def addLL0scale(rl, rightmove, zero) -> ET.Element:
    "Adds the LL0 scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # LL0 mark
    if zero:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":str(40), "fill":"black", "font-size":"24"})
        LLmark.text = "LL"
        LL0mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":str(42), "fill":"black", "font-size":"12"})
        LL0mark.text = "0"
    else:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":str(70), "fill":"black", "font-size":"24"})
        LLmark.text = "LL"
        LL0mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":str(72), "fill":"black", "font-size":"12"})
        LL0mark.text = "0"

    # e**0.001x mark
    if zero:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 2), "y":str(38),"fill":"black", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 10), "y":str(30),"fill":"black", "font-size":"12"})
        exmark.text = "0.001x"
    else:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 2), "y":str(78),"fill":"black", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 10), "y":str(70),"fill":"black", "font-size":"12"})
        exmark.text = "0.001x"

    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin + rl.scalewidth + rl.scalewidth + rl.scalewidth

    # x from 1.0010 to 1.010 in steps of 0.00001
    for r in range(100100, 101001):   # 101001 to include 101000 due to range missing last value
        textstr = ''
        length = 0
        x = r/100000.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            length = 45
            if r != 100900:
                textstr = str(x)
                fontsize = 16
                y0 = 60
                y1 = 50
        elif r % 50 == 0:
            length = 35
            if r < 100400:
                textstr = str(x)
                fontsize = 14
                y0 = 50
                y1 = 40
        elif r % 10 == 0:
            length = 25
        elif r % 5 == 0 and r<100400:
            length = 20
        elif r < 100120:
            length = 15
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)
    return doc





