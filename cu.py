# 1 inch = 0,0254m
# 1 foot = 0,3048m // 12in
# 1 yard = 0,9144m // 3ft
# 1 mile = 1609,344m // 1760yd

# To add more units must add them to unitnames, units and unitsinmetres
unitnames = [# List of available units in a handful of possible spellings
    ["km", "kilometre", "kilometres", "kilometer", "kilometers"],
    ["hm", "hectometre", "hectometres", "hectometer", "hectometers"],
    ["dam", "decametre", "decametres", "decameter", "decameters"],
    ["m", "metre", "metres", "meter", "meters"],
    ["dm", "decimetre", "decimetres", "decimeter", "decimeters"],
    ["cm", "centimetre", "centimetres", "centimeter", "centimeters"],
    ["mm", "milimetre", "milimetres", "milimeter", "milimeters", "millimeter", "millimeters", "millimetre", "millimetres"],
    ["in", "inch", "inches"], ["ft", "foot", "feet"], ["yd", "yard", "yards"],
    ["mi", "mile", "miles", "mille", "milles"]
    ["leag", "league", "leagues", "leage", "leages"]
    ["er", "earth radius", "earth radiuses", "earth radious", "earth radiouses"]
    ["ld", "lunar distance", "lunar distances", "moon distance", "moon distances"]
    ["au", "astronomical unit", "astronomical units", "astro unit", "astro units"]
    ["ly", "light year", "light years", "ligth year", "ligth years"]
    ["pc", "parsec", "parsecs", "parasec", "parasecs", "parasect", "parasects"]
    ["smt", "smoot", "smoots", "moot", "moots"]
]

units = {# This list is used to know which uintnames list (index) belongs to what unit
    0: "km", 1: "hm", 2: "dam", 3: "m", 4: "dm", 5: "cm", 6: "mm",
    7: "inch", 8: "ft", 9: "yd", 10: "mi", 11: "leag", 12: "er", 13: "ld",
    14: "au", 15: "ly", 16: "pc", 17: "smt"
}

unitsinmetres = {# All units converted to meters
    "km": 1000.0, "hm": 100.0, "dam": 10.0, "m": 1.0, "dm": 0.1, "cm": 0.01, "mm": 0.001,
    "inch": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344, "leag": 4828.032
    "er": 6371000, "ld": 384402000, "au": 149597870700, "ly": 9460730472580800,
    "pc": 30856775814671900, "smt": 1.70
}

def unit_finder(inp): # Finds what unit is the user talking about
        out = inp
        for x in range(len(unitnames)): # Iterates over all the lists in unitnames
            if inp in unitnames[x]:
                out = x # Stores the index of the unit in unitnames
        return out
def unit_printer(): # Joins the units to print them
    units2 = []
    for x in range(len(unitnames)):
        units2.append((unitnames[x][1]))
    ", ".join(units2)
    return units2
def unit_checker(inp): # Checks if the input is valid
    isin = False
    for x in range(len(unitnames)): # Iterates over all the lists in unitnames
        if inp in unitnames[x]: # Checks if the innput is in any of the lists
            isin = True
    return isin
def convert(finalunit, quantity, startingunit): # Converts the units
    meters = unitsinmetres[units[startingunit]] # First, convert the starting unit to metres
    totalmeters = meters * quantity
    total = totalmeters / unitsinmetres[units[finalunit]] # Actually converts to the final unit
    finalunit = units[finalunit]
    final = str(total) + finalunit # Makes the output fancy
    return final

# Welcome message
print "***************************************************************************"
print "\nWelcome to the unit converter! all the available units at the moment are:"
print unit_printer()
print
print "Input a blank answer to restart or 'exit' to end the program \n"
print "***************************************************************************"

will_to_live = True
while will_to_live == True: # Asking the important things right there
    fromunitinput = raw_input("convert from ").lower() # The unit to convert from
    if fromunitinput == "exit": # Checks if user wants to exit
        will_to_live = False
        break
    elif fromunitinput == "": # Checks if the user wants to reset
        print
    else:
        if unit_checker(fromunitinput): # Checks if the input is valid
            fromunit = unit_finder(fromunitinput) # Make the input usefull
            quantity = raw_input("How many %s? " % unitnames[fromunit][2]) # Asks for quantity of the unit
            if quantity == "exit": # Checks if user wants to exit
                will_to_live = False
                break
            elif quantity == "": # Checks if the user wants to reset
                print
            else:
                if quantity.isdigit(): # Checks if the input is valid
                    quantity = int(quantity)
                    tounitinput = raw_input("convert to ").lower() # The unit to convert to
                    tounit = unit_finder(tounitinput) # Make the input usefull
                    if tounitinput == "exit": # Checks if user wants to exit
                        will_to_live = False
                        break
                    elif tounitinput == "": # Checks if the user wants to reset
                        print
                    else:
                        if unit_checker(tounitinput): # Checks if the input is valid
                            print convert(tounit, quantity, fromunit) # Prints the result
                        else:
                            print
                            print "That is not a valid unit"
                            print
                else:
                    print
                    print "That is not a valid input, please write a number"
                    print
        else:
            print
            print "That is not a valid unit"
            print
