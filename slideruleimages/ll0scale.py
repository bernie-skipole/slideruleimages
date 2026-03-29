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


def addLL0scale(rl, rightmove) -> ET.Element:
    "Adds the LL0 scale to the rule, returns the scale element"

    ybot = 100

    doc = ET.Element('g')

    # LL0 mark
    LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":str(ybot-30), "fill":"black", "font-size":"24"})
    LLmark.text = "LL"
    LL0mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":str(ybot-28), "fill":"black", "font-size":"12"})
    LL0mark.text = "0"

    # e**0.001x mark
    emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 2), "y":str(ybot-22),"fill":"black", "font-size":"16"})
    emark.text = "e"
    exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 10), "y":str(ybot-30),"fill":"black", "font-size":"12"})
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
                texty = ybot-50
        elif r % 50 == 0:
            length = 35
            if r < 100400:
                textstr = str(x)
                fontsize = 14
                texty = ybot-40
        elif r % 10 == 0:
            length = 25
        elif r % 5 == 0 and r<100400:
            length = 20
        elif r < 100120:
            length = 15
        if length:
            _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, xpos, texty, fontsize)

    return doc





