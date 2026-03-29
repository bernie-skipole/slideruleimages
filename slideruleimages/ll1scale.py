import xml.etree.ElementTree as ET

import math


def _vertical(doc, length, xpos, ybot, col="black"):
    """Creates a vertical line
       doc is the scale element to which this line will be inserted
       length is the length of the vertical line
       ybot is the ending y position
       xpos is the x position
       col is the colour of the line"""
    # get xpos to the nearest .25
    xpos = round(xpos*4)/4.0
    vline = {"x1":str(xpos), "y1":str(ybot), "x2":str(xpos), "y2":str(ybot-length), "style":f"stroke:{col};stroke-width:1"}
    ET.SubElement(doc, 'line', vline)

def _text(doc, textstr, xpos, texty, fontsize):
    "Adds text"
    if textstr:
        if len(textstr) == 1:
            textpos = round(xpos - 4)    #  textpos This is in pixels
        else:
            textpos = round(xpos - 6)    # three characters, such as 1.5
        
        tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
        tel.text = textstr


def addLL1scale(rl, rightmove) -> ET.Element:
    "Adds the LL1 scale to the rule, returns the scale element"

    ybot = 100

    doc = ET.Element('g')

    # LL1 mark
    LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":str(ybot-30), "fill":"black", "font-size":"24"})
    LLmark.text = "LL"
    LL1mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":str(ybot-28), "fill":"black", "font-size":"12"})
    LL1mark.text = "1"

    # e**0.01x mark
    emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 6), "y":str(ybot-36),"fill":"black", "font-size":"16"})
    emark.text = "e"
    exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":str(ybot-44),"fill":"black", "font-size":"12"})
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
            texty = ybot-50
        elif r % 50 == 0:
            length = 35
            if r < 10400:
                textstr = str(x)
                fontsize = 14
                texty = ybot-40
        elif r % 10 == 0:
            length = 25
        elif r % 5 == 0 and r<10400:
            length = 20
        elif r < 10120:
            length = 15
        if length:
            _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, xpos, texty, fontsize)

    return doc





