# slideruleimages
Python package to produce Slide Rule SVG images

A typical example might be:

    from slideruleimages import Rule

    # xvalue is where the C scale index is placed over the D value
    # right is True if the mid scale is moved to the right
    # right is False if the mid scale is moved to the left
    # hairline is where the hairline cursor is placed over the D value,
    # or zero if no hairline is used 

    rl = Rule(xvalue = 2.0, right = True, hairline=6.0,
              topruleheight = 0,                        # No top rule
              midruleheight = 120,                      # middle slider 120px high
              btmruleheight = 120)                      # bottom rule 120 px high

    # Add a C scale
    rl.addCscale(midrule=20)  # indicates this scale is put on the middle rule
                              # 20 pixels down from the top of the middle rule

    # Add a D scale
    rl.addDscale(btmrule=0)   # indicates this scale is put on the bottom rule
                              # 0 pixels down from the top of the bottom rule

    filename = "twoxthree.svg"

    rl.write(filename)

    print(f'{filename} created')

This would produce:

![example](https://raw.githubusercontent.com/bernie-skipole/slideruleimages/main/twoxthree.svg)

This package is intended to produce images useful for documents or web sites
which illustrate logarithms or Slide Rules. One such web site is available at:

https://bernie-skipole.github.io/sliderule/

The package has one class, Rule, which is illustrated above and has the methods:

write(filename) This saves the image file.

addDscale(btmrule=-1, midrule=-1, toprule=-1)

addCscale(btmrule=-1, midrule=-1, toprule=-1)

addCFscale(btmrule=-1, midrule=-1, toprule=-1)

addDFscale(btmrule=-1, midrule=-1, toprule=-1)

addLL3scale(btmrule=-1, midrule=-1, toprule=-1)

addLL2scale(btmrule=-1, midrule=-1, toprule=-1)

addLL1scale(btmrule=-1, midrule=-1, toprule=-1)

addLL0scale(btmrule=-1, midrule=-1, toprule=-1)

Only one of the arguments btmrule, midrule or toprule should be given a non -1 argument
which indicates which rule the scale should appear on, and the integer number of
pixels down from the top of that rule.

The package is available on Pypi at:

https://pypi.org/project/slideruleimages/



