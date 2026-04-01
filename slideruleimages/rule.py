import xml.etree.ElementTree as ET

import math

from .ascale import addAscale

from .bscale import addBscale

from .dscale import addDscale

from .cscale import addCscale

from .cfscale import addCFscale

from .dfscale import addDFscale

from .kscale import addKscale

from .ll3scale import addLL3scale

from .ll2scale import addLL2scale

from .ll1scale import addLL1scale

from .ll0scale import addLL0scale



class Rule:
    "Defines a rule dimensions"

    def __init__(self, xvalue:float = 1.0, right:bool = True, hairline:float=0.0,
                      topruleheight = 120,
                      midruleheight = 200,
                      btmruleheight = 120,
                      col = "#f9fc69"):
        """xvalue is where the C scale index is placed over the D value
           right is True if the mid scale is moved to the right
           right is False if the mid scale is moved to the left
           hairline is where the hairline cursor is placed over the D value, or zero if no hairline is used
           col is the colour of the rule, by default a pale yellow"""

        self.topruleheight = topruleheight
        self.midruleheight = midruleheight
        self.btmruleheight = btmruleheight

        self.scalewidth = 900
        self.leftmargin = 50
        self.rightmargin = 50

        self.mainmove = 0.0
        self.slidermove = 0.0

        if xvalue<1 or xvalue>10:
            raise ValueError("Invalid x value, must be between 1 and 10")

        if right:
            self.mainmove = 0.0
            if xvalue == 1:
                self.slidermove = 0.0
            else:
                self.slidermove = self.scalewidth*math.log10(xvalue)   # This is the movement of a rule
        else:
            self.slidermove = 0.0
            if xvalue == 1:
                self.mainmove = 0.0
            else:
                self.mainmove = self.scalewidth*math.log10(10.0/xvalue)   # This is the movement of a rule

        if hairline:
            if hairline<1 or hairline>10:
                raise ValueError("Invalid hairline value, should be either zero or a number between 1 and 10")
            self.hairline = hairline
        else:
            self.hairline = 0.0

        self._doc = ET.Element('svg', width=str(self.imagewidth), height=str(self.imageheight), version='1.1', xmlns='http://www.w3.org/2000/svg')
        textstyle = ET.SubElement(self._doc, 'style')
        textstyle.text = """text {
          font-family: Arial, Helvetica, sans-serif;
          font-weight: Thin;
          }
    """

        # top rule
        if self.topruleheight:
            ### rectangle of background colour
            ET.SubElement(self._doc, 'rect', {"width":str(self.rulewidth), "height":str(self.topruleheight),
                                              "x":str(self.mainmove),"y":"0",
                                              "style":f"fill:{col};stroke-width:1;stroke:black"})

        # midrule - the slider
        if self.midruleheight:
            ### rectangle of background colour
            ET.SubElement(self._doc, 'rect', {"width":str(self.rulewidth), "height":str(self.midruleheight),
                                              "x":str(self.slidermove),"y":str(self.topruleheight),
                                              "style":f"fill:{col};stroke-width:1;stroke:black"})

        # bottom rule
        if self.btmruleheight:
            # bottom rule
            heightofy = self.topruleheight + self.midruleheight
            ### rectangle of background colour
            ET.SubElement(self._doc, 'rect', {"width":str(self.rulewidth), "height":str(self.btmruleheight),
                                              "x":str(self.mainmove),"y":str(heightofy),
                                              "style":f"fill:{col};stroke-width:1;stroke:black"})

        # hairline
        if self.hairline:
            ET.SubElement(self._doc, 'line', {"x1":str(self.hairlinepos),
                                        "y1":"0",
                                        "x2":str(self.hairlinepos),
                                        "y2":str(self.imageheight),
                                        "style":"stroke:grey;stroke-width:1"})

    @property
    def hairlinepos(self):
        if not self.hairline:
            return self.mainmove
        return self.mainmove + self.leftmargin + self.scalewidth*math.log10(self.hairline)

    @property
    def imagewidth(self):
        return self.mainmove + self.slidermove + self.leftmargin + self.scalewidth + self.rightmargin

    @property
    def rulewidth(self):
        return self.leftmargin + self.scalewidth + self.rightmargin

    @property
    def imageheight(self):
        return self.topruleheight + self.midruleheight + self.btmruleheight

    def write(self, filename):
        tree = ET.ElementTree(self._doc)
        tree.write(filename, xml_declaration=True)

    def _createscale(self, fn, btmrule, midrule, toprule):
        zero = False
        if toprule>-1:
            if midrule>-1 or btmrule>-1:
                raise ValueError("Only one of btmrule, midrule or toprule should be specified")
            rightmove = self.mainmove
            if not toprule:
                zero=True   # the pixel distance from the top of this ruler is zero
        elif midrule>-1:
            if btmrule>-1:
                raise ValueError("Only one of btmrule, midrule or toprule should be specified")
            rightmove = self.slidermove
            if not midrule:
                zero=True   # the pixel distance from the top of this ruler is zero
        elif btmrule>-1:
            rightmove = self.mainmove
            if not btmrule:
                zero=True   # the pixel distance from the top of this ruler is zero
        else:
            raise ValueError("At least one rule must be specified")
        element = fn(self, rightmove, zero)
        if toprule>-1:
            if toprule>0:
                element.set("transform", f"translate(0 {toprule})")
        elif midrule>-1:
            if self.topruleheight + midrule > 0:
                element.set("transform", f"translate(0 {self.topruleheight + midrule})")
        elif btmrule>-1:
            if self.topruleheight + self.midruleheight + btmrule > 0:
                element.set("transform", f"translate(0 {self.topruleheight + self.midruleheight + btmrule})")
        self._doc.append(element)

    def addAscale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addAscale, btmrule, midrule, toprule)

    def addBscale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addBscale, btmrule, midrule, toprule)

    def addDscale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addDscale, btmrule, midrule, toprule)

    def addCscale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addCscale, btmrule, midrule, toprule)

    def addCFscale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addCFscale, btmrule, midrule, toprule)

    def addDFscale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addDFscale, btmrule, midrule, toprule)

    def addKscale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addKscale, btmrule, midrule, toprule)

    def addLL3scale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addLL3scale, btmrule, midrule, toprule)

    def addLL2scale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addLL2scale, btmrule, midrule, toprule)

    def addLL1scale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addLL1scale, btmrule, midrule, toprule)

    def addLL0scale(self, btmrule=-1, midrule=-1, toprule=-1):
        self._createscale(addLL0scale, btmrule, midrule, toprule)



