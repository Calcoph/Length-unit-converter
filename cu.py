#cd D:\Diego\Documents\GitHub\Length-unit-converter

from tkinter import *
from tkinter import ttk


class Combox(ttk.Combobox):
    def __init__(self, frame, inputName, state="readonly"):
        self.frame = frame
        self.state = state
        ttk.Combobox.__init__(self, frame, state=state)
        self.inputName = inputName
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
        if inputName.get() == 0:
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
        elif inputName.get() == 1:
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
        self.createWidgets()
    def createWidgets(self):
        inputName = IntVar()
        outputName = IntVar()
        self.showDisclaimer = BooleanVar()
        self.showDisclaimer.set(True)
        inputName.set(1)
        outputName.set(0)
        mainFrame = ttk.Frame(self, padding="3 3 12 12")
        mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        #mainFrame.columnconfigure(0, weight=1)
        #mainFrame.rowconfigure(0, weight=1)
        unitInputBox = Combox(mainFrame, inputName)
        unitInputBox.grid(column=2, row=2, sticky=(N, S, W, E))
        unitInputBox["values"] = unitInputBox.getInputName(inputName=inputName)
        unitOutputBox = Combox(mainFrame, inputName)
        unitOutputBox.grid(column=2, row=4, sticky=(N, S, W, E))
        unitOutputBox["values"] = unitInputBox.getInputName(inputName=inputName)
        unitInputBox.set("meter")
        unitOutputBox.set("foot")
        def getInputNames(inputName):
            unitInputBox.getInputName(inputName)
            unitOutputBox.getInputName(inputName)
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
        menuBar = Menu(self)
        settings = Menu(menuBar, tearoff=0)
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
        # List of all available units (abreviation, name, plural name)
        unitNames = [
            ["km", "kilometer", "kilometers"],
            ["hm", "hectometer", "hectometers"],
            ["dam","decameter", "decameters"],
            ["m", "meter", "meters"],
            ["dm", "decimeter", "decimeters"],
            ["cm", "centimeter", "centimeters"],
            ["mm", "millimeter", "millimeters"],
            ["in", "inch", "inches"],
            ["ft", "foot", "feet"],
            ["yd", "yard", "yards"],
            ["mi", "mile", "miles"],
            ["leag", "league", "leagues"],
            ["er", "earth radius", "earth radiuses"],
            ["ld", "lunar distance", "lunar distances"],
            ["au", "astronomical unit", "astronomical units"],
            ["ly", "light year", "light years"],
            ["pc", "parsec", "parsecs"],
            ["smt", "smoot", "smoots"]
            ]
            # Most of the widgets
        def disableButton():
            fadingButton.grid_forget()
            self.maxsize(width=291, height=138)
            self.minsize(width=291, height=138)
            self.maxsize(width=9999999, height=9999999)
            self.showDisclaimer.set(False)
        def recoverButton():
            fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
            self.maxsize(width=305, height=224)
            self.minsize(width=305, height=224)
            self.maxsize(width=9999999, height=9999999)
        def displayTooltip():
            fadingButton["height"] = 5
            fadingButton["text"] = "Click HERE to hide this"
        def displayText():
            fadingButton["text"] ="******************************************************"\
            +"\nThis is intended for day to day use and might have"\
            +"\naccuracy problems dealing with numbers very large,"\
            +"\nvery low or numbers that have a lot of decimals."\
            +"\n******************************************************"
        def checkDisclaimerStatus():
            if self.showDisclaimer.get() == False:
                disableButton()
            else:
                recoverButton()

        def printInfo():#used for debugging
            print(self.winfo_width(), self.winfo_height())
        unitNameOptions = Menu(settings, tearoff=0)
        unitNameOptions.add_radiobutton(label="Abreviated inputs",
                                        variable=inputName, value=0,
                                        command=lambda:getInputNames(inputName))
        unitNameOptions.add_radiobutton(label="Full named inputs",
                                        variable=inputName, value=1,
                                        command=lambda:getInputNames(inputName))
        unitNameOptions.add_separator()
        unitNameOptions.add_radiobutton(label="Abreviated outputs",
                                        variable=outputName, value=0)
        unitNameOptions.add_radiobutton(label="Full named outputs",
                                        variable=outputName, value=1)
        settings.add_cascade(label="Unit name options", menu=unitNameOptions)
        settings.add_separator()
        settings.add_checkbutton(label="Show disclaimer",
                                variable=self.showDisclaimer,
                                onvalue=True, offvalue=False,
                                command=checkDisclaimerStatus)
        settings.add_command(label="Exit", command=self.quit)
        menuBar.add_cascade(label="Settings", menu=settings)
        self.config(menu=menuBar)
        ttk.Label(mainFrame, text="Equals to:").grid(column=1, row=3, sticky=(N, S, W, E))
        ttk.Label(mainFrame, text="Convert any length unit to another one instantly!"\
        ).grid(column=1, row=0, columnspan=2, sticky=(N, S, W, E))
        fadingButton = Button(mainFrame, text=\
                            "******************************************************"\
                            +"\nThis is intended for day to day use and might have"\
                            +"\naccuracy problems dealing with numbers very large,"\
                            +"\nvery low or numbers that have a lot of decimals."\
                            +"\n******************************************************",
                            justify="left", width=40, command=disableButton)
        fadingButton.grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
        ttk.Label(mainFrame, textvariable=output).grid(column=1, row=4,
                                                        sticky=(N, S, W, E))
        ttk.Button(mainFrame, text="^v", command=changeTheInputs).grid(column=2,
                                                                        row=3,
                                                                        sticky=(N, S, W, E))
        ttk.Button(mainFrame, text="Home", command=home, width=0).grid(column=1,
                                                                        row=6,
                                                                        sticky=W)
        def convert(finalUnit, quantity, startingUnit, outputName):
            def selectOutputName(finalUnit, outputName, quantity):
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
                if outputName.get() == 0:
                    return output0[finalUnit]
                elif outputName.get() == 1:
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
            finalUnit = selectOutputName(finalUnit, outputName, total)
            final = total + " " + finalUnit
            output.set(final)
        ttk.Button(mainFrame, text="CONVERT",
                    command=lambda:convert(unitOutputBox.get(), quanInput,
                                            unitInputBox.get(), outputName)
                                            ).grid(column=1, row=5, columnspan=2,
                                                    padx=100, pady=(12, 0),
                                                    sticky=(N, S, W, E)
                                                    )
        def changeInputs(unitInputBox, unitOutputBox):
            inputbefore = unitInputBox.get()
            outputbefore = unitOutputBox.get()
            unitInputBox.set(outputbefore)
            unitOutputBox.set(inputbefore)
        quantityInput = ttk.Entry(mainFrame, textvariable=quanInput)
        quantityInput.grid(column=1, row=2, sticky=(N, S, W, E))
        # Configure the entry
        quanInput.set("")
        quantityInput.focus()
        mainFrame.pack(expand=1)
        # Bindings
        fadingButton.bind("<Enter>", lambda event:displayTooltip())
        fadingButton.bind("<Leave>", lambda event:displayText())
        self.bind('<Return>', lambda event:convert(unitOutputBox.get(),
                                                    quanInput, unitInputBox.get(),
                                                    outputName))
        # Set the minnimum window size
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
    def destroyWidgets(self, mainFrame):
        mainFrame.pack_forget()
        mainFrame.grid_forget()
        self.maxsize(width=9999999, height=9999999)
        self.minsize(width=0, height=0)
    def home(self):
        def length():
            self.destroyWidgets(mainFrame)
            self.lengthConverter()
        self.title("Universal unit converter")
        mainFrame = ttk.Frame(self, padding="3 3 12 12")
        mainFrame.grid(column=0, row=0, sticky=(N, W, E, S)) # Colocar la ventana
        mainFrame.columnconfigure(0, weight=1)
        mainFrame.rowconfigure(0, weight=1)
        ttk.Label(mainFrame, text="Choose your converter!").grid(column=1,
                                                                row=1,
                                                                sticky=(N, S, W, E),
                                                                columnspan=2)
        ttk.Button(mainFrame, text="Length", command=length).grid(column=1,
                                                                    row=2,
                                                                    sticky=(N, S, W, E))
        ttk.Button(mainFrame, text="Volume", command=length).grid(column=2,
                                                                    row=2,
                                                                    sticky=(N, S, W, E))
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
root = Application() # La ventana en si
root.title("Feet to Meters") # Titulo de la ventana


root.mainloop()
