import xml.etree.ElementTree as ET

import math

from . import draw


def addLL02scale(rl, rightmove, zero) -> ET.Element:
    "Adds the LL02 scale to the rule, returns the scale element"

    doc = ET.Element('g')

    # LL02 mark
    if zero:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"30", "fill":"red", "font-size":"24"})
        LLmark.text = "LL"
        LL02mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"34", "fill":"red", "font-size":"12"})
        LL02mark.text = "02"
    else:
        LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":"78", "fill":"red", "font-size":"24"})
        LLmark.text = "LL"
        LL02mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":"80", "fill":"red", "font-size":"12"})
        LL02mark.text = "02"

    # e**-0.1x mark
    if zero:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 10), "y":"26","fill":"red", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 18), "y":"18","fill":"red", "font-size":"12"})
        exmark.text = "-0.1x"
    else:
        emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 10), "y":"84","fill":"red", "font-size":"16"})
        emark.text = "e"
        exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 18), "y":"76","fill":"red", "font-size":"12"})
        exmark.text = "-0.1x"


    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin


    # end at x = 1/e
    xpos = rightmove + rl.leftmargin + rl.scalewidth
    length = 35
    textstr = "1/e"
    fontsize = 18
    y0 = 50
    y1 = 40
    draw.line(doc, length, xpos, zero, col="black")
    draw.text(doc, textstr, xpos, zero, y0, y1, fontsize, col="red")


    # 1/e^0.1x from 0.904 to 1/e 

    for r in range(905, 400, -1):  # 905 to 399
        textstr = ''
        length = 0
        x = r/1000               # 0.905 to 0.399
        xpos = c+m*math.log10(-10*math.log(x))
        fontsize = 16
        if r % 100 == 0 :
            length = 35
            textstr = str(x)
            y0 = 50
            y1 = 40
        elif r % 50 == 0:
            length = 25
            textstr = str(x)
            y0 = 40
            y1 = 30
            fontsize = 14
        elif r % 10 == 0:
            length = 20
        elif r % 5 == 0:
            length = 15
        elif r > 850:
            length = 10

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize, col="red")


    for r in range(400, 369, -1):  # 400 to 370
        textstr = ''
        length = 0
        x = r/1000               # 0.400 to 0.370
        xpos = c+m*math.log10(-10*math.log(x))
        fontsize = 16
        if r % 100 == 0 :
            length = 35
            textstr = str(x)
            y0 = 50
            y1 = 40
        elif r % 10 == 0:
            length = 20
        elif r % 5 == 0:
            length = 15

        if length:
            draw.line(doc, length, xpos, zero, col="black")
        if textstr:
            draw.text(doc, textstr, xpos, zero, y0, y1, fontsize, col="red")



    return doc





