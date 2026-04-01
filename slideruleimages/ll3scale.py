import xml.etree.ElementTree as ET

import math

from . import draw


def addLL3scale(rl, rightmove, zero) -> ET.Element:
    "Adds the LL3 scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # LL3 mark
    if zero:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"40", "fill":"black", "font-size":"24"})
        LLmark.text = "LL"
        LL3mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"42", "fill":"black", "font-size":"12"})
        LL3mark.text = "3"
    else:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"70", "fill":"black", "font-size":"24"})
        LLmark.text = "LL"
        LL3mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"72", "fill":"black", "font-size":"12"})
        LL3mark.text = "3"

    # e**x mark
    if zero:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"34","fill":"black", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 22), "y":"26","fill":"black", "font-size":"12"})
        exmark.text = "x"
    else:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"80","fill":"black", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 22), "y":"72","fill":"black", "font-size":"12"})
        exmark.text = "x"


    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin

    # start at x = e
    xpos = c
    length = 35
    textstr = "e"
    fontsize = 18
    y0 = 50
    y1 = 40
    draw.line(doc, length, xpos, zero, col="black")
    draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)

    # x from 2.75 to 4.0 in steps of 0.05
    for r in range(275, 400, 5):
        textstr = ''
        length = 0
        x = r/100.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            length = 35
            textstr = "3"
            fontsize = 16
            y0 = 50
            y1 = 40
        elif r % 50 == 0:
            length = 25
            textstr = str(x)
            fontsize = 16
            y0 = 40
            y1 = 30
        elif r % 10 == 0:
            length = 20
        else:
            length = 14
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)
    # x from 4.0 to 10.0 in steps of 0.1
    for r in range(400, 1000):
        textstr = ''
        length = 0
        x = r/100.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            length = 35
            textstr = str(int(x))
            fontsize = 16
            y0 = 50
            y1 = 40
        elif r % 50 == 0:
            length = 25
        elif r % 25 == 0 and r > 700:
            length = 20
        elif r % 10 == 0 and r < 700:
            length = 14
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)
    # x from 10.0 to 100.0 in steps of 1
    for r in range(10, 100):
        textstr = ''
        length = 0
        x = float(r)
        xpos = m*math.log10(math.log(x)) + c
        if r % 10 == 0:
            if r <= 50:
                length = 35
                textstr = str(int(x))
                fontsize = 16
                y0 = 50 
                y1 = 40
            else:
                length = 25
        elif r % 5 == 0:
            if r <= 50:
                length = 25
            else:
                length = 20
            if r == 15:
                textstr = "15"
                fontsize = 16
                y0 = 40
                y1 = 30
        elif r < 40:
            length = 14
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)
    # x from 100 to 1000 in steps of 10
    for r in range(100, 1000, 10):
        textstr = ''
        length = 0
        x = float(r)
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            if r in (100, 200, 500):
                length = 40
                textstr = str(r)
                fontsize = 16
                y0 = 55
                y1 = 45
                textpos = xpos-10
            else:
                length = 25
        elif r % 50 == 0:
            length = 20
        elif r < 200:
            length = 14
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)
    # x from 1000 to 5000 in steps of 100
    for r in range(1000, 5000, 100):
        textstr = ''
        length = 0
        x = float(r)
        xpos = m*math.log10(math.log(x)) + c
        if r % 1000 == 0:
            if r in (1000, 2000, 3000):
                length = 50
                fontsize = 16
                y0 = 65
                y1 = 55
                textpos = xpos
                if r == 1000:
                    textstr = '1k'
                elif r == 2000:
                    textstr = '2k'
                else:
                    textstr = '3k'
            else:
                length = 25
        elif r % 500 == 0:
            length = 20
        elif r < 2000:
            length = 14
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)
    # x from 5000 to 20000 in steps of 1000
    for r in range(5000, 20001, 1000):
        textstr = ''
        length = 0
        x = float(r)
        xpos = m*math.log10(math.log(x)) + c
        if r % 5000 == 0:
            if r == 15000:
                length = 20
            elif r in (5000, 10000, 20000):
                length = 50
                fontsize = 16
                y0 = 65
                y1 = 55
                if r == 5000:
                    textpos = xpos
                else:
                    textpos = xpos-10
                textstr = f'{int(r/1000)}k'
        else:
            length = 14
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize)
    return doc





