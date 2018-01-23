# 1 inch = 0,0254m
# 1 foot = 0,3048m // 12in
# 1 yard = 0,9144m // 3ft
# 1 mile = 1609,344m // 1760yd

# list of available units in a handful of possible spelling
unitnames = [
    ["km", "kilometre", "kilometres", "kilometer", "kilometers"],
    ["hm", "hectometre", "hectometres", "hectometer", "hectometers"],
    ["dam", "decametre", "decametres", "decameter", "decameters"],
    ["m", "metre", "metres", "meter", "meters"],
    ["dm", "decimetre", "decimetres", "decimeter", "decimeters"],
    ["cm", "centimetre", "centimetres", "centimeter", "centimeters"],
    ["mm", "milimetre", "milimetres", "milimeter", "milimeters", "millimeter", "millimeters", "millimetre", "millimetres"],
    ["in", "inch", "inches"], ["ft", "foot", "feet"], ["yd", "yard", "yards"],
    ["mi", "mille", "milles", "mile", "miles"]
]
# this list is used to know which uintnames list is for what unit
units = {
    0: "km", 1: "hm", 2: "dam", 3: "m", 4: "dm", 5: "cm", 6: "mm", 7: "inch", 8: "ft", 9: "yd", 10: "mi"
}
# all units converted to meters
unitsinmetres = {
    "km": 1000.0, "hm": 100.0, "dam": 10.0, "m": 1.0, "dm": 0.1, "cm": 0.01, "mm": 0.001,
    "inch": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344
}

def unit_finder(inp):
        out = inp
        for x in range(len(unitnames)):
            if inp in unitnames[x]:
                out = x
        return out
def unit_printer():
    units2 = []
    for x in range(len(unitnames)):
        units2.append((unitnames[x][1]))
    ", ".join(units2)
    return units2
def unit_checker(inp):
    isin = False
    for x in range(len(unitnames)):
        if inp in unitnames[x]:
            isin = True
    return isin
def convert(finalunit, quantity, startingunit):
    meters = unitsinmetres[units[startingunit]]
    totalmeters = meters * quantity
    total = totalmeters / unitsinmetres[units[finalunit]]
    finalunit = units[finalunit]
    final = str(total) + finalunit
    return final

print "***************************************************************************"
print "\nWelcome to the unit converter! all the available units at the moment are:"
print unit_printer()
print
print "Input a blank answer to restart or 'exit' to end the program \n"
print "***************************************************************************"

will_to_live = True
while will_to_live == True:
    fromunitinput = raw_input("convert from ").lower()
    if fromunitinput == "exit":
        will_to_live = False
        break
    elif fromunitinput == "":
        print
    else:
        if unit_checker(fromunitinput):
            fromunit = unit_finder(fromunitinput)
            quantity = raw_input("How many %s? " % unitnames[fromunit][2])
            if quantity == "exit":
                will_to_live = False
                break
            elif quantity == "":
                print
            else:
                if quantity.isdigit():
                    quantity = int(quantity)
                    tounitinput = raw_input("convert to ").lower()
                    tounit = unit_finder(tounitinput)
                    if tounitinput == "exit":
                        will_to_live = False
                        break
                    elif tounitinput == "":
                        print
                    else:
                        if unit_checker(tounitinput):
                            print convert(tounit, quantity, fromunit)
                        else:
                            print
                            print "That is not a valid unit"
                            print
                else:
                    print
                    print "That is not a valid unit"
                    print
        else:
            print
            print "That is not a valid unit"
            print
