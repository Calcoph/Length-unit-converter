#cd D:\Diego\Documents\GitHub\Length-unit-converter

<<<<<<< HEAD
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
    "pc": 30856775814671900, "smt": 1.7
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
=======
from tkinter import *
from tkinter import ttk


class Combox(ttk.Combobox):
    def __init__(self, frame, inputName, state="readonly"):
        self.frame = frame
        self.state = state
        ttk.Combobox.__init__(self, frame, state=state)
        self.getInputName(inputName)
    def getInputName(self, inputName):
        bothValueOptions = {
            "km": "kilometer",
            "hm": "hectometer",
            "dam": "decameter",
            "m": "meter",
            "dm": "decimeter",
            "cm": "centimeter",
            "mm": "millimeter",
            "in": "inch",
            "ft": "foot",
            "yd": "yard",
            "mi": "mile",
            "leag": "league",
            "er": "earth radius",
            "ld": "lunar distance",
            "au": "astronomical unit",
            "ly": "light year",
            "pc": "parsec",
            "smt": "smoot"
            }
        if inputName.get() == 1:
            values = [
                "km",
                "hm",
                "dam",
                "m",
                "dm",
                "cm",
                "mm",
                "in",
                "ft",
                "yd",
                "mi",
                "leag",
                "er",
                "ld",
                "au",
                "ly",
                "pc",
                "smt"
                ]
        elif inputName.get() == 0:
            values = [
                "kilometer",
                "hectometer",
                "decameter",
                "meter",
                "decimeter",
                "centimeter",
                "millimeter",
                "inch",
                "foot",
                "yard",
                "mile",
                "league",
                "earth radius",
                "lunar distance",
                "astronomical unit",
                "light year",
                "parsec",
                "smoot"
                ]
        notInKeys = True
        currentlyDisplaying = self.get()
        for key, value in bothValueOptions.items():
            if currentlyDisplaying == key:
                currentlyDisplaying = key
                newDisplay = value
                notInKeys = False
        if notInKeys:
            for key, value in bothValueOptions.items():
                if currentlyDisplaying == value:
                    currentlyDisplaying = value
                    newDisplay = key
        try:
            self.set(newDisplay)
        except UnboundLocalError:
            pass
        self["values"] = values
class Application(Tk):
    def __init__(self):
        Tk.__init__(self) # Esto por algún motivo es super importante
        self.createMenu()
        self.home()
        self.grid()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
    def lengthConverter(self):
        self.title("Length converter")
        self.lengthFrame = ttk.Frame(self, padding="3 3 12 12") # La ventana de la ventana
        self.lengthFrame.grid(column=0, row=0, sticky=(N, W, E, S)) # Colocar la ventana
        self.lengthFrame.columnconfigure(1, weight=1)
        self.lengthFrame.columnconfigure(2, weight=1)
        self.lengthFrame.rowconfigure(0, weight=1)
        self.lengthFrame.rowconfigure(1, weight=1)
        self.lengthFrame.rowconfigure(2, weight=1)
        self.lengthFrame.rowconfigure(3, weight=1)
        self.lengthFrame.rowconfigure(4, weight=1)
        self.lengthFrame.rowconfigure(5, weight=1)
        self.lengthFrame.rowconfigure(6, weight=1)
        unitInputBox = Combox(self.lengthFrame, self.inputName)
        unitInputBox.grid(column=2, row=2, sticky=(N, S, W, E))
        unitInputBox["values"] = unitInputBox.getInputName(self.inputName)
        unitOutputBox = Combox(self.lengthFrame, self.inputName)
        unitOutputBox.grid(column=2, row=4, sticky=(N, S, W, E))
        unitOutputBox["values"] = unitInputBox.getInputName(self.inputName)
        unitInputBox.set("meter")
        unitOutputBox.set("foot")
        def home():
            self.destroyWidgets()
            self.home()
        def round(floatNumber):
            stringNumber = str(float(floatNumber))
            if "." in stringNumber:
                indexOfDot = stringNumber.index(".")
                newNumber = []
                iterations = 0
                while iterations <= (indexOfDot + 2):
                    if (iterations + 1) > len(stringNumber):
                        break
                    if iterations == (indexOfDot + 2):
                        try:
                            if int(stringNumber[indexOfDot + 3]) >= 5:
                                newNumber.append(str(int(stringNumber[indexOfDot + 2]) + 1))
                            else:
                                newNumber.append(stringNumber[iterations])
                        except IndexError:
                            newNumber.append(stringNumber[iterations])
                    else:
                        newNumber.append(stringNumber[iterations])
                    iterations += 1
                if "e" in stringNumber:
                    indexOfE = stringNumber.index("e")
                    iterations = indexOfE
                    while iterations < len(stringNumber):
                        newNumber.append(stringNumber[(iterations)])
                        iterations += 1
                    newNumber = "".join(newNumber)
                    return newNumber
                else:
                    newNumber = "".join(newNumber)
                    return newNumber
            else:
                return stringNumber
        # The menu
        #menuBar = Menu(self)###############
        #settings = Menu(menuBar, tearoff=0)################
        global output
        output = StringVar()
        quanInput = IntVar()
        changeTheInputs = lambda:changeInputs(unitInputBox, unitOutputBox)
        # all units converted to meters
        unitsInMeters = {
            "kilometer": 1000.0,
            "hectometer": 100.0,
            "decameter": 10.0,
            "meter": 1.0,
            "decimeter": 0.1,
            "centimeter": 0.01,
            "millimeter": 0.001,
            "inch": 0.0254,
            "foot": 0.3048,
            "yard": 0.9144,
            "mile": 1609.344,
            "league": 4828.032,
            "earth radius": 6371000.0,
            "lunar distance": 384402000.0,
            "astronomical unit": 149597870700.0,
            "light year": 9460730472580800.0,
            "parsec": 30856775814671900.0,
            "smoot": 1.70
            }
            # Most of the widgets
        def displayTooltip():
            self.fadingButton["height"] = 5
            self.fadingButton["text"] = "Click HERE to hide this"
        def displayText():
            self.fadingButton["text"] ="******************************************************"\
            +"\nThis is intended for day to day use and might have"\
            +"\naccuracy problems dealing with numbers very large,"\
            +"\nvery low or numbers that have a lot of decimals."\
            +"\n******************************************************"
        def getInputNames():
            unitInputBox.getInputName(self.inputName)
            unitOutputBox.getInputName(self.inputName)
        def printInfo():#used for debugging
            print(self.winfo_width(), self.winfo_height())
        self.unitNameOptions.add_radiobutton(label="Abreviated inputs",
                                        variable=self.inputName, value=1,
                                        command=getInputNames
                                        )
        self.unitNameOptions.add_radiobutton(label="Full named inputs",
                                        variable=self.inputName, value=0,
                                        command=getInputNames
                                        )
        self.unitNameOptions.add_separator()
        self.unitNameOptions.add_radiobutton(label="Abreviated outputs",
                                        variable=self.outputName, value=0)
        self.unitNameOptions.add_radiobutton(label="Full named outputs",
                                        variable=self.outputName, value=1)
        def disableButton():
            self.fadingButton.grid_forget()
            self.maxsize(width=291, height=163)
            self.minsize(width=291, height=163)
            self.maxsize(width=9999999, height=9999999)
            self.showDisclaimer.set(False)
        def recoverButton():
            self.fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
            self.maxsize(width=305, height=249)
            self.minsize(width=305, height=249)
            self.maxsize(width=9999999, height=9999999)
        ttk.Label(self.lengthFrame, text="Equals to:").grid(column=1, row=3,
                                                        sticky=(N, S, W, E))
        ttk.Label(self.lengthFrame, text="Convert any length unit to another one instantly!",\
                    ).grid(column=1, row=0, columnspan=2, sticky=(N, S, W, E))
        self.fadingButton = Button(self.lengthFrame, text=\
                                "******************************************************"\
                                +"\nThis is intended for day to day use and might have"\
                                +"\naccuracy problems dealing with numbers very large,"\
                                +"\nvery low or numbers that have a lot of decimals."\
                                +"\n******************************************************",
                                justify="left", width=40, command=disableButton)
        self.fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
        ttk.Label(self.lengthFrame, textvariable=output).grid(column=1, row=4,
                                                        sticky=(N, S, W, E))
        ttk.Button(self.lengthFrame, text="^v", command=changeTheInputs).grid(column=2,
                                                                        row=3,
                                                                        sticky=(N, S, W, E))
        ttk.Button(self.lengthFrame, text="Home", command=home, width=0).grid(column=1,
                                                                        row=6,
                                                                        sticky=W)
        def convert(finalUnit, quantity, startingUnit):
            def selectOutputName(finalUnit, quantity):
                output0 = {
                    "kilometer": "km",
                    "hectometer": "hm",
                    "decameter": "dam",
                    "meter": "m",
                    "decimeter": "dm",
                    "centimeter": "cm",
                    "millimeter": "mm",
                    "inch": "in",
                    "foot": "ft",
                    "yard": "yd",
                    "mile": "mi",
                    "league": "leag",
                    "earth radius": "er",
                    "lunar distance": "ld",
                    "astronomical unit": "au",
                    "light year": "ly",
                    "parsec": "pc",
                    "smoot": "smt"
                    }
                output1 = {
                    "kilometer": "kilometers",
                    "hectometer": "hectometers",
                    "decameter": "decameters",
                    "meter": "meters",
                    "decimeter": "decimeters",
                    "centimeter": "centimeters",
                    "millimeter": "millimeters",
                    "inch": "inches",
                    "foot": "feet",
                    "yard": "yards",
                    "mile": "miles",
                    "league": "leagues",
                    "earth radius": "earth radiuses",
                    "lunar distance": "lunar distances",
                    "astronomical unit": "astronomical units",
                    "light year": "light years",
                    "parsec": "parsecs",
                    "smoot": "smoots"
                    }
                if self.outputName.get() == 0:
                    return output0[finalUnit]
                elif self.outputName.get() == 1:
                    if float(quantity) == 1.0:
                        return finalUnit
                    else:
                        return output1[finalUnit]
            inputConvertion = {
                "km": "kilometer",
                "hm": "hectometer",
                "dam": "decameter",
                "m": "meter",
                "dm": "decimeter",
                "cm": "centimeter",
                "mm": "millimeter",
                "in": "inch",
                "ft": "foot",
                "yd": "yard",
                "mi": "mile",
                "leag": "league",
                "er": "earth radius",
                "ld": "lunar distance",
                "au": "astronomical unit",
                "ly": "light year",
                "pc": "parsec",
                "smt": "smoot"
                }
            if startingUnit in inputConvertion:
                startingUnit = inputConvertion[startingUnit]
            if finalUnit in inputConvertion:
                finalUnit = inputConvertion[finalUnit]
            meters = unitsInMeters[startingUnit]
            totalMeters = meters * int(str(quantity.get()))
            total = totalMeters / unitsInMeters[finalUnit]
            total = round(total)
            finalUnit = selectOutputName(finalUnit, total)
            final = total + " " + finalUnit
            output.set(final)
        ttk.Button(self.lengthFrame, text="CONVERT",
                    command=lambda:convert(unitOutputBox.get(), quanInput,
                                            unitInputBox.get(), outputName)
                                            ).grid(column=1, row=5,
                                                    columnspan=2, padx=100,
                                                    pady=(12, 0), sticky=(N, S, W, E))
        def changeInputs(unitInputBox, unitOutputBox):
            inputbefore = unitInputBox.get()
            outputbefore = unitOutputBox.get()
            unitInputBox.set(outputbefore)
            unitOutputBox.set(inputbefore)
        quantityInput = ttk.Entry(self.lengthFrame, textvariable=quanInput)
        quantityInput.grid(column=1, row=2, sticky=(N, S, W, E))
        # Configure the entry
        quanInput.set("")
        quantityInput.focus()
        #self.lengthFrame.pack(expand=1)
        # Bindings
        self.fadingButton.bind("<Enter>", lambda event:displayTooltip())
        self.fadingButton.bind("<Leave>", lambda event:displayText())
        self.bind('<Return>', lambda event:convert(unitOutputBox.get(),
                                                    quanInput, unitInputBox.get()
                                                    )
                                                    )
        # Set the minnimum window size
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
    def destroyWidgets(self):
        try:
            self.lengthFrame.pack_forget()
            self.lengthFrame.grid_forget()
        except:
            pass
        try:
            self.homeFrame.grid_forget()
            self.homeFrame.pack_forget()
        except:
            pass
        self.maxsize(width=9999999, height=9999999)
        self.minsize(width=0, height=0)
    def createMenu(self): #TRABAJOAQUIIII
        #   menu abajo
        self.showDisclaimer = BooleanVar()
        self.showDisclaimer.set(True)
        self.inputName = IntVar()
        self.outputName = IntVar()
        def disableButton():
            self.fadingButton.grid_forget()
            self.maxsize(width=291, height=163)
            self.minsize(width=291, height=163)
            self.maxsize(width=9999999, height=9999999)
            self.showDisclaimer.set(False)
        def recoverButton():
            self.fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
            self.maxsize(width=305, height=249)
            self.minsize(width=305, height=249)
            self.maxsize(width=9999999, height=9999999)
        def getInputNames():
            unitInputBox.getInputName(self.inputName)
            unitOutputBox.getInputName(self.inputName)
        def checkDisclaimerStatus():######################
            if self.showDisclaimer.get() == False:
                disableButton()
            else:
                recoverButton()
        menuBar = Menu(self)
        settings = Menu(menuBar, tearoff=0)
        self.unitNameOptions = Menu(settings, tearoff=0)
        settings.add_cascade(label="Unit name options", menu=self.unitNameOptions)
        settings.add_separator()
        settings.add_checkbutton(label="Show disclaimer",
                                    variable=self.showDisclaimer,
                                    onvalue=True, offvalue=False,
                                    command=checkDisclaimerStatus)
        settings.add_command(label="Exit", command=self.quit)
        menuBar.add_cascade(label="Settings", menu=settings)
        self.config(menu=menuBar)
        #   menu arriba
    def home(self):
        def length():
            self.destroyWidgets()
            self.lengthConverter()
        self.title("Universal unit converter")
        self.homeFrame = ttk.Frame(self, padding="3 3 12 12")
        self.homeFrame.grid(column=0, row=0, sticky=(N, W, E, S)) # Colocar la ventana
        self.homeFrame.columnconfigure(1, weight=1)
        self.homeFrame.columnconfigure(2, weight=1)
        self.homeFrame.rowconfigure(1, weight=1)
        self.homeFrame.rowconfigure(2, weight=1)
        ttk.Label(self.homeFrame, text="Choose your converter!"
                    ).grid(column=1,
                            row=1,
                            sticky=(N, S, W, E),
                            columnspan=2
                            )
        ttk.Button(self.homeFrame, text="Length", command=length
                    ).grid(column=1,
                            row=2,
                            sticky=(N, S, W, E)
                            )
        ttk.Button(self.homeFrame, text="Volume", command=length
                    ).grid(column=2,
                            row=2,
                            sticky=(N, S, W, E)
                            )
        #self.homeFrame.pack(expand=1)
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
root = Application() # La ventana en si
root.mainloop()
>>>>>>> GUI
