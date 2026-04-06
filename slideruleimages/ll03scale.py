import xml.etree.ElementTree as ET

import math

from . import draw


def addLL03scale(rl, rightmove, zero) -> ET.Element:
    "Adds the LL03 scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # LL03 mark
    if zero:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"26", "fill":"red", "font-size":"24"})
        LLmark.text = "LL"
        LL03mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"30", "fill":"red", "font-size":"12"})
        LL03mark.text = "03"
    else:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"78", "fill":"red", "font-size":"24"})
        LLmark.text = "LL"
        LL03mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"80", "fill":"red", "font-size":"12"})
        LL03mark.text = "03"

    # e**-x mark
    if zero:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"34","fill":"red", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 22), "y":"26","fill":"red", "font-size":"12"})
        exmark.text = "-x"
    else:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":"80","fill":"red", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 22), "y":"72","fill":"red", "font-size":"12"})
        exmark.text = "-x"


    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin

    # start at x = 1/e
    xpos = rightmove + rl.leftmargin
    length = 35
    textstr = "1/e"
    fontsize = 18
    y0 = 50
    y1 = 40
    draw.line(doc, length, xpos, zero, col="black")
    draw.text(doc, textstr, xpos, zero, y0, y1, fontsize, col="red")

    # 1/e^x from 0.36 to 0.01

    for r in range(360, 10, -1):  # 360 to 10
        textstr = ''
        length = 0
        x = r/1000               # 0.36 to 0.1
        xpos = c+m*math.log10(-1*math.log(x))
        fontsize = 16
        if r == 50:
            length = 30
            draw.text(doc, "0.05", xpos-10, zero, 50, 40, fontsize, col="red")
        elif r<100 and r>40:
            if r % 10 == 0:
                length = 20
            elif r % 5 == 0:
                length = 10 
        elif r<=40:
            if r % 20 == 0:
                length = 30
                textstr = str(x)
                y0 = 50
                y1 = 40
            elif r % 10 == 0 :
                length = 30
            elif r % 5 == 0 :
                length = 20
            else :
                length = 10
        elif r % 100 == 0 :
            length = 30
            textstr = str(x)
            y0 = 50
            y1 = 40
        elif r % 50 == 0 :
            length = 20
        else:
            if r % 10 == 0:
                length = 10

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize, col="red")


    for r in range(100, 10, -1):  # 100 to 9
        textstr = ''
        length = 0
        x = r/10000               # 0.01 to 0.001
        xpos = c+m*math.log10(-1*math.log(x))
        fontsize = 16
        if r == 100:
            length = 30
            draw.text(doc, "10", xpos, zero, 50, 40, 16, col="red")
            draw.text(doc, "-2", xpos+16, zero, 40, 50, 12, col="red")
        elif r == 50:
            length = 30
            textstr = "5"
            y0 = 50
            y1 = 40
        elif r == 20:
            length = 30
            textstr = "2"
            y0 = 50
            y1 = 40
        elif r % 10 == 0:
            length = 20
        elif r < 50 and r % 5 == 0:
            length = 10
        elif r < 20:
            length = 5
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize, col="red")

    for r in range(100, 10, -1):  # 100 to 9
        textstr = ''
        length = 0
        x = r/100000               # 0.001 to 0.0001
        xpos = c+m*math.log10(-1*math.log(x))
        fontsize = 16
        if r == 100:
            length = 30
            draw.text(doc, "10", xpos, zero, 50, 40, 16, col="red")
            draw.text(doc, "-3", xpos+16, zero, 40, 50, 12, col="red")
        elif r == 50:
            length = 30
            textstr = "5"
            y0 = 50
            y1 = 40
        elif r == 20:
            length = 30
            textstr = "2"
            y0 = 50
            y1 = 40
        elif r % 10 == 0:
            length = 20
        elif r < 50 and r % 5 == 0:
            length = 10
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize, col="red")

    for r in range(100, 49, -1):  # 100 to 49
        textstr = ''
        length = 0
        x = r/1000000               # 0.0001 to 0.00001
        xpos = c+m*math.log10(-1*math.log(x))
        fontsize = 16
        if r == 100:
            length = 30
            draw.text(doc, "10", xpos, zero, 50, 40, 16, col="red")
            draw.text(doc, "-4", xpos+16, zero, 40, 50, 12, col="red")
        elif r == 50:
            length = 30
            textstr = "5"
            y0 = 50
            y1 = 40
        elif r % 10 == 0:
            length = 20
        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize, col="red")




    return doc





