#cd D:\Diego\Documents\GitHub\Length-unit-converter

from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class Combox(ttk.Combobox):
    def __init__(self, frame, inputName, units, font, state="readonly"):
        self.frame = frame
        self.state = state
        self.allValueOptions = units
        ttk.Combobox.__init__(self, frame, font=font, state=state)
        self.getInputName(inputName)
    def getInputName(self, inputName):# Changes the combobox options' names
        lengthValueOptions = {}
        for unit in self.allValueOptions:
            lengthValueOptions[self.allValueOptions[self.allValueOptions.index(unit)][0]] = self.allValueOptions[self.allValueOptions.index(unit)][1]
        values=[]
        if inputName.get() == 1:
            for value in lengthValueOptions:
                values.append(value)
        elif inputName.get() == 0:
            for value in lengthValueOptions:
                values.append(lengthValueOptions[value])
        # Changes the selected item's name in the combobox
        notInKeys = True
        currentlyDisplaying = self.get()
        for key, value in lengthValueOptions.items():
            if currentlyDisplaying == key:
                currentlyDisplaying = key
                newDisplay = value
                notInKeys = False
        if notInKeys:
            for key, value in lengthValueOptions.items():
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
        Tk.__init__(self)
        self.myFont = tkFont.Font(size=15)
        self.buttonStyle = ttk.Style()
        self.buttonStyle.configure("Big.TButton", font=self.myFont)
        self.option_add("*TCombobox*Listbox*Font", self.myFont)
        self.lengthConverterMinimumWindowSize = (484, 343)
        self.volumeConverterMinimumWindowSize = (484, 343)
        self.createMenu()
        self.home()
        self.grid()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
    def lengthConverter(self):
        self.title("Length converter")
        x, y = self.lengthConverterMinimumWindowSize
        self.allLengthValueOptions = [["km", "Kilometer", "Kilometers"],
                                        ["hm", "Hectometer", "Hectometers"],
                                        ["dam", "Decameter", "Decameters"],
                                        ["m", "Meter", "Meters"],
                                        ["dm", "Decimeter", "Decimeters"],
                                        ["cm", "Centimeter", "Centimeters"],
                                        ["mm", "Millimeter", "Millimeters"],
                                        ["in", "USC Inch", "USC Inches"],
                                        ["ft", "USC Foot", "USC Feet"],
                                        ["yd", "USC Yard", "USC Yards"],
                                        ["mi", "USC Mile", "USC Miles"],
                                        ["lea", "USC League", "USC Leagues"],
                                        ["er", "Earth radius", "Earth radiuses"],
                                        ["ld", "Lunar distance", "Lunar distances"],
                                        ["au", "Astronomical unit", "Astronomical units"],
                                        ["ly", "Light year", "Light years"],
                                        ["pc", "Parsec", "Parsecs"],
                                        ["smt", "Smoot", "Smoots"]
                                        ]
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
        unitInputBox = Combox(self.lengthFrame, self.inputName, self.allLengthValueOptions, font=self.myFont)
        unitInputBox.grid(column=2, row=2, padx=(7, 0), pady=(1, 2), sticky=(N, S, W, E))
        unitInputBox["values"] = unitInputBox.getInputName(self.inputName)
        unitOutputBox = Combox(self.lengthFrame, self.inputName, self.allLengthValueOptions, font=self.myFont)
        unitOutputBox.grid(column=2, row=4, padx=(7, 0), pady=(2, 0), sticky=(N, S, W, E))
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
        global output
        output = StringVar()
        quanInput = IntVar()
        changeTheInputs = lambda:changeInputs(unitInputBox, unitOutputBox)
        # all units converted to meters
        unitsInMeters = {"Kilometer": 1000.0,
                        "Hectometer": 100.0,
                        "Decameter": 10.0,
                        "Meter": 1.0,
                        "Decimeter": 0.1,
                        "Centimeter": 0.01,
                        "Millimeter": 0.001,
                        "USC Inch": 0.0254,
                        "USC Foot": 0.3048,
                        "USC Yard": 0.9144,
                        "USC Mile": 1609.344,
                        "USC League": 4828.032,
                        "Earth radius": 6371000.0,
                        "Lunar distance": 384402000.0,
                        "Astronomical unit": 149597870700.0,
                        "Light year": 9460730472580800.0,
                        "Parsec": 30856775814671900.0,
                        "Smoot": 1.70
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
            self.maxsize(x, y-132)
            self.minsize(x, y-132)
            self.maxsize(width=9999999, height=9999999)
            self.showDisclaimer.set(False)
        def recoverButton():
            self.fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
            self.maxsize(x, y)
            self.minsize(x, y)
            self.maxsize(width=9999999, height=9999999)
        ttk.Label(self.lengthFrame, text="Equals to:", font=self.myFont).grid(column=1, row=3,
                                                        sticky=(N, S, W, E))
        ttk.Label(self.lengthFrame, text="Convert any length unit to another one instantly!",\
                    font=self.myFont).grid(column=1, row=0, columnspan=2, sticky=(N, S, W, E))
        self.fadingButton = Button(self.lengthFrame, text=\
                                "******************************************************"\
                                +"\nThis is intended for day to day use and might have"\
                                +"\naccuracy problems dealing with numbers very large,"\
                                +"\nvery low or numbers that have a lot of decimals."\
                                +"\n******************************************************",
                                justify="left", width=40, command=disableButton, font=self.myFont
                                )
        self.fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
        ttk.Label(self.lengthFrame, textvariable=output, font=self.myFont).grid(column=1, row=4,
                                                        sticky=(N, S, W, E))
        ttk.Button(self.lengthFrame, text="^v", command=changeTheInputs, width=4, style="Big.TButton"
                    ).grid(column=2,
                            row=3,
                            )
        ttk.Button(self.lengthFrame, text="Home", command=home, width=0, style="Big.TButton").grid(column=1,
                                                                        row=6,
                                                                        sticky=W)
        ttk.Button(self.lengthFrame, text="Print window size", command=printInfo).\
        grid(column=2, row=6, sticky=(N, S, W, E))
        def convert(finalUnit, quantity, startingUnit):
            def selectOutputName(finalUnit, quantity):
                self.allLengthValueOptions
                if self.outputName.get() == 0:
                    for unit in self.allLengthValueOptions:
                        if finalUnit in unit:
                            return self.allLengthValueOptions[self.allLengthValueOptions.index(unit)][0]
                elif self.outputName.get() == 1:
                    if float(quantity) == 1.0:
                        return finalUnit
                    else:
                        for unit in self.allLengthValueOptions:
                            if finalUnit in unit:
                                return self.allLengthValueOptions[self.allLengthValueOptions.index(unit)][2]
            inputConvertion = {}
            for unit in self.allLengthValueOptions:
                inputConvertion[self.allLengthValueOptions[self.allLengthValueOptions.index(unit)
                                                            ][0]
                                ] = self.allLengthValueOptions[self.allLengthValueOptions.index(unit)][1]
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
        ttk.Button(self.lengthFrame, text="CONVERT", style="Big.TButton",
                    command=lambda:convert(unitOutputBox.get(), quanInput,
                                            unitInputBox.get())
                                            ).grid(column=1, row=5,
                                                    columnspan=2, padx=100,
                                                    pady=(12, 0), sticky=(N, S, W, E))
        def changeInputs(unitInputBox, unitOutputBox):
            inputbefore = unitInputBox.get()
            outputbefore = unitOutputBox.get()
            unitInputBox.set(outputbefore)
            unitOutputBox.set(inputbefore)
        quantityInput = ttk.Entry(self.lengthFrame, textvariable=quanInput, font=self.myFont)
        quantityInput.grid(column=1, row=2, padx=(0, 7), pady=(1, 0), sticky=(N, S, W, E))
        # Configure the entry
        quanInput.set("")
        quantityInput.focus()
        self.fadingButton.bind("<Enter>", lambda event:displayTooltip())
        self.fadingButton.bind("<Leave>", lambda event:displayText())
        self.bind('<Return>', lambda event:convert(unitOutputBox.get(),
                                                    quanInput, unitInputBox.get()
                                                    )
                    )
        # Set the minnimum window size
        self.update()
        self.minsize(x, y)
    def volumeConverter(self):
        self.title("Volume converter")
        x, y = self.volumeConverterMinimumWindowSize
        self.allVolumeValueOptions = [["km\u00b3", "Cubic kilometer", "Cubic kilometers"], # ESTOOOOO
                                    ["hm\u00b3", "Cubic hectometer", "Cubic hectometers"],
                                    ["dam\u00b3", "Cubic decameter", "Cubic decameters"],
                                    ["m\u00b3", "Cubic meter", "Cubic meters"],
                                    ["dm\u00b3", "Cubic decimeter", "Cubic decimeters"],
                                    ["cm\u00b3", "Cubic centimeter", "Cubic centimeters"],
                                    ["mm\u00b3", "Cubic millimeter", "Cubic millimeters"],
                                    ["in\u00b3", "USC Cubic inch", "USC Cubic inches"],
                                    ["ft\u00b3", "USC Cubic foot", "USC Cubic feet"],
                                    ["yd\u00b3", "USC Cubic yard", "USC Cubic yards"],
                                    ["mi\u00b3", "USC Cubic mile", "USC Cubic miles"],
                                    ["lea\u00b3", "USC Cubic league", "USC Cubic leagues"],
                                    ["er\u00b3", "Cubic earth radius", "Cubic earth radiuses"],
                                    ["ld\u00b3", "Cubic lunar distance", "Cubic lunar distances"],
                                    ["au\u00b3", "Cubic astronomical unit", "Cubic astronomical units"],
                                    ["ly\u00b3", "Cubic light year", "Cubic light years"],
                                    ["pc\u00b3", "Cubic parsec", "Cubic parsecs"],
                                    ["smt\u00b3", "Cubic smoot", "Cubic smoots"],
                                    ["kL", "Kiloliter", "Kiloliters"],
                                    ["hL", "Hectoliter", "Hectoliters"],
                                    ["daL", "Decaliter", "Decaliters"],
                                    ["L", "Liter", "Liters"],
                                    ["dL", "Deciliter", "Deciliters"],
                                    ["cL", "Centiliter", "Centiliters"],
                                    ["mL", "Milliliter", "Milliliters"],
                                    ["tsp", "USC Teaspoon", "USC Teaspoons"],
                                    ["Tbsp", "USC Tablespoon", "USC Tablespoons"]
                                    ]
        self.volumeFrame = ttk.Frame(self, padding="3 3 12 12") # La ventana de la ventana
        self.volumeFrame.grid(column=0, row=0, sticky=(N, W, E, S)) # Colocar la ventana
        self.volumeFrame.columnconfigure(1, weight=1)
        self.volumeFrame.columnconfigure(2, weight=1)
        self.volumeFrame.rowconfigure(0, weight=1)
        self.volumeFrame.rowconfigure(1, weight=1)
        self.volumeFrame.rowconfigure(2, weight=1)
        self.volumeFrame.rowconfigure(3, weight=1)
        self.volumeFrame.rowconfigure(4, weight=1)
        self.volumeFrame.rowconfigure(5, weight=1)
        self.volumeFrame.rowconfigure(6, weight=1)
        unitInputBox = Combox(self.volumeFrame, self.inputName, self.allVolumeValueOptions, font=self.myFont)
        unitInputBox.grid(column=2, row=2, padx=(7, 0), pady=(1, 2), sticky=(N, S, W, E))
        unitInputBox["values"] = unitInputBox.getInputName(self.inputName)
        unitOutputBox = Combox(self.volumeFrame, self.inputName, self.allVolumeValueOptions, font=self.myFont)
        unitOutputBox.grid(column=2, row=4, padx=(7, 0), pady=(2, 0), sticky=(N, S, W, E))
        unitOutputBox["values"] = unitInputBox.getInputName(self.inputName)
        unitInputBox.set("Cubic meter")
        unitOutputBox.set("Cubic foot")
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
        global output
        output = StringVar()
        quanInput = IntVar()
        changeTheInputs = lambda:changeInputs(unitInputBox, unitOutputBox)
        # All units converted to meters
        unitsInDecimeters = {"Cubic kilometer": 10000.0,# SIN HACER! ! ! ! ! !!!!!!!
                            "Cubic hectometer": 1000.0,
                            "Cubic decameter": 100.0,
                            "Cubic meter": 10.0,
                            "Cubic decimeter": 1.0,
                            "Cubic centimeter": 0.1,
                            "Cubic millimeter": 0.01,
                            "USC Cubic inch": 0.254,
                            "USC Cubic foot": 3.048,
                            "USC Cubic yard": 9.144,
                            "USC Cubic mile": 16093.44,
                            "USC Cubic league": 48280.32,
                            "Cubic earth radius": 63710000.0,
                            "Cubic lunar distance": 3844020000.0,
                            "Cubic astronomical unit": 1495978707000.0,
                            "Cubic light year": 94607304725808000.0,
                            "Cubic parsec": 308567758146719000.0,
                            "Cubic smoot": 17.0,
                            }
        # All units converted to liters
        unitsInLiters = {"Kiloliter": 1000.0,# SIN HACER! ! ! ! ! !!!!!!!
                            "Hectoliter": 100.0,
                            "Decaliter": 10.0,
                            "Liter": 1.0,
                            "Deciliter": 0.1,
                            "Centiliter": 0.01,
                            "Milliliter": 0.001,
                            "USC Teaspoon": 0.0049289215937,
                            "USC Tablespoon": 0.0147868
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
            self.maxsize(x, y-132)
            self.minsize(x, y-132)
            self.maxsize(width=9999999, height=9999999)
            self.showDisclaimer.set(False)
        def recoverButton():
            self.fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
            self.maxsize(x, y)
            self.minsize(x, y)
            self.maxsize(width=9999999, height=9999999)
        ttk.Label(self.volumeFrame, text="Equals to:", font=self.myFont).grid(column=1, row=3,
                                                        sticky=(N, S, W, E))
        ttk.Label(self.volumeFrame, text="Convert any volume unit to another one instantly!",\
                    font=self.myFont).grid(column=1, row=0, columnspan=2, sticky=(N, S, W, E))
        self.fadingButton = Button(self.volumeFrame, text=\
                                "******************************************************"\
                                +"\nThis is intended for day to day use and might have"\
                                +"\naccuracy problems dealing with numbers very large,"\
                                +"\nvery low or numbers that have a lot of decimals."\
                                +"\n******************************************************",
                                justify="left", width=40, command=disableButton, font=self.myFont
                                )
        self.fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
        ttk.Label(self.volumeFrame, textvariable=output, font=self.myFont).grid(column=1, row=4,
                                                        sticky=(N, S, W, E))
        ttk.Button(self.volumeFrame, text="^v", command=changeTheInputs, width=4, style="Big.TButton"
                    ).grid(column=2,
                            row=3,
                            )
        ttk.Button(self.volumeFrame, text="Home", command=home, width=0, style="Big.TButton").grid(column=1,
                                                                        row=6,
                                                                        sticky=W)
        ttk.Button(self.volumeFrame, text="Print window size", command=printInfo).\
        grid(column=2, row=6, sticky=(N, S, W, E))
        def convert(finalUnit, quantity, startingUnit):
            def selectOutputName(finalUnit, quantity):
                self.allVolumeValueOptions
                if self.outputName.get() == 0:
                    for unit in self.allVolumeValueOptions:
                        if finalUnit in unit:
                            return self.allVolumeValueOptions[self.allVolumeValueOptions.index(unit)][0]
                elif self.outputName.get() == 1:
                    if float(quantity) == 1.0:
                        return finalUnit
                    else:
                        for unit in self.allVolumeValueOptions:
                            if finalUnit in unit:
                                return self.allVolumeValueOptions[self.allVolumeValueOptions.index(unit)][2]
            inputConvertion = {}
            for unit in self.allVolumeValueOptions:
                inputConvertion[self.allVolumeValueOptions[self.allVolumeValueOptions.index(unit)
                                                            ][0]
                                ] = self.allVolumeValueOptions[self.allVolumeValueOptions.index(unit)][1]
            if startingUnit in inputConvertion:
                startingUnit = inputConvertion[startingUnit]
            if finalUnit in inputConvertion:
                finalUnit = inputConvertion[finalUnit]
            if startingUnit in unitsInDecimeters:
                decimeters = unitsInDecimeters[startingUnit]
                liters = decimeters ** 3
            elif startingUnit in unitsInLiters:
                liters = unitsInLiters[startingUnit]
            totalLiters = liters * int(str(quantity.get()))
            if finalUnit in unitsInDecimeters:
                finalDecimeters = unitsInDecimeters[finalUnit]
                total = totalLiters / (finalDecimeters ** 3)
            elif finalUnit in unitsInLiters:
                total = totalLiters / unitsInLiters[finalUnit]
            total = round(total)
            finalUnit = selectOutputName(finalUnit, total)
            final = total + " " + finalUnit
            output.set(final)
        ttk.Button(self.volumeFrame, text="CONVERT", style="Big.TButton",
                    command=lambda:convert(unitOutputBox.get(), quanInput,
                                            unitInputBox.get())
                                            ).grid(column=1, row=5,
                                                    columnspan=2, padx=100,
                                                    pady=(12, 0), sticky=(N, S, W, E))
        def changeInputs(unitInputBox, unitOutputBox):
            inputbefore = unitInputBox.get()
            outputbefore = unitOutputBox.get()
            unitInputBox.set(outputbefore)
            unitOutputBox.set(inputbefore)
        quantityInput = ttk.Entry(self.volumeFrame, textvariable=quanInput, font=self.myFont)
        quantityInput.grid(column=1, row=2, padx=(0, 7), pady=(1, 0), sticky=(N, S, W, E))
        # Configure the entry
        quanInput.set("")
        quantityInput.focus()
        self.fadingButton.bind("<Enter>", lambda event:displayTooltip())
        self.fadingButton.bind("<Leave>", lambda event:displayText())
        self.bind('<Return>', lambda event:convert(unitOutputBox.get(),
                                                    quanInput, unitInputBox.get()
                                                    )
                    )
        # Set the minnimum window size
        self.update()
        self.minsize(x, y)
    def destroyWidgets(self):
        try:
            self.lengthFrame.pack_forget()
            self.lengthFrame.grid_forget()
        except:
            pass
        try:
            self.volumeFrame.pack_forget()
            self.volumeFrame.grid_forget()
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
        x, y = self.lengthConverterMinimumWindowSize
        self.showDisclaimer = BooleanVar()
        self.showDisclaimer.set(True)
        self.inputName = IntVar()
        self.outputName = IntVar()
        def disableButton():
            self.fadingButton.grid_forget()
            self.maxsize(x, y-132)
            self.minsize(x, y-132)
            self.maxsize(width=9999999, height=9999999)
            self.showDisclaimer.set(False)
        def recoverButton():
            self.fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
            self.maxsize(x, y)
            self.minsize(x, y)
            self.maxsize(width=9999999, height=9999999)
        def getInputNames():
            unitInputBox.getInputName(self.inputName)
            unitOutputBox.getInputName(self.inputName)
        def checkDisclaimerStatus():
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
        HomeMinimumWindowSize = (277, 75)
        x, y = HomeMinimumWindowSize
        def length():
            self.destroyWidgets()
            self.lengthConverter()
        def volume():
            self.destroyWidgets()
            self.volumeConverter()
        self.title("Universal unit converter")
        self.homeFrame = ttk.Frame(self, padding="3 3 12 12")
        self.homeFrame.grid(column=0, row=0, sticky=(N, W, E, S)) # Colocar la ventana
        self.homeFrame.columnconfigure(1, weight=1)
        self.homeFrame.columnconfigure(2, weight=1)
        self.homeFrame.rowconfigure(1, weight=1)
        self.homeFrame.rowconfigure(2, weight=1)
        def printInfo():#used for debugging
            print(self.winfo_width(), self.winfo_height())
        ttk.Label(self.homeFrame, text="Choose your converter!", font=self.myFont
                    ).grid(column=1,
                            row=1,
                            sticky=(N, S, W, E),
                            columnspan=2
                            )
        #ttk.Button(self.homeFrame, text="Print window size", command=printInfo).\
        #grid(column=1, row=1, sticky=(N, S, W, E))
        ttk.Button(self.homeFrame, text="Length", command=length,
                    style="Big.TButton").grid(column=1,
                            row=2,
                            sticky=(N, S, W, E)
                            )
        ttk.Button(self.homeFrame, text="Volume", command=volume,
                    style="Big.TButton").grid(column=2,
                            row=2,
                            sticky=(N, S, W, E)
                            )
        #self.homeFrame.pack(expand=1)
        self.update()
        self.minsize(x, y)
root = Application() # La ventana en si
root.mainloop()
