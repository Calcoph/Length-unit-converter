#cd D:\Diego\Documents\GitHub\Length-unit-converter

from tkinter import *
from tkinter import ttk





class Application(Tk):
    def __init__(self):
        Tk.__init__(self) # Esto por algún motivo es super importante
        self.createWidgets()
    def createWidgets(self):
        def getinputname():# !!!!!! NECESITA TRABAJO AQUI!!!!!!
            if inputname.get() == 0:
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
            elif inputname.get() == 1:
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
            return values
        def round(floatnumber):
            stringnumber = str(float(floatnumber))
            if "." in stringnumber:
                indexofdot = stringnumber.index(".")
                newnumber = []
                iterations = 0
                while iterations <= (indexofdot + 2):
                    if (iterations + 1) > len(stringnumber):
                        break
                    if iterations == (indexofdot + 2):
                        try:
                            if int(stringnumber[indexofdot + 3]) >= 5:
                                newnumber.append(str(int(stringnumber[indexofdot + 2]) + 1))
                            else:
                                newnumber.append(stringnumber[iterations])
                        except IndexError:
                            newnumber.append(stringnumber[iterations])
                    else:
                        newnumber.append(stringnumber[iterations])
                    iterations += 1
                if "e" in stringnumber:
                    indexofe = stringnumber.index("e")
                    iterations = indexofe
                    while iterations < len(stringnumber):
                        newnumber.append(stringnumber[(iterations)])
                        iterations += 1
                    newnumber = "".join(newnumber)
                    return newnumber
                else:
                    newnumber = "".join(newnumber)
                    return newnumber
            else:
                return stringnumber
        # The menu
        mainframe = ttk.Frame(self, padding="3 3 12 12") # La ventana de la ventana
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # Colocar la ventana
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        inputname = IntVar()
        outputname = IntVar()
        inputname.set(1)
        outputname.set(0)
        global output
        output = StringVar()
        quaninput = IntVar()
        unitnameoptions = Menu(filemenu, tearoff=0)
        unitnameoptions.add_radiobutton(label="Abreviated inputs", variable=inputname, value=0)
        unitnameoptions.add_radiobutton(label="Full named inputs", variable=inputname, value=1)
        unitnameoptions.add_separator()
        unitnameoptions.add_radiobutton(label="Abreviated outputs", variable=outputname, value=0)
        unitnameoptions.add_radiobutton(label="Full named outputs", variable=outputname, value=1)
        filemenu.add_cascade(label="Unit name options", menu=unitnameoptions)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="Settings", menu=filemenu)
        self.config(menu=menubar)
        changetheinputs = lambda:changeinputs(unitinputbox, unitoutputbox)

        # all units converted to meters
        unitsinmeters = {
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
        unitnames = [
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
        ttk.Label(mainframe, text="Equals to:").grid(column=1, row=3, sticky=(N, S, W, E))
        ttk.Label(mainframe, text="Convert any length unit to another one instantly!").grid(column=1, row=1, columnspan=2, sticky=(N, S, W, E))
        ttk.Label(mainframe, textvariable=output).grid(column=1, row=4, sticky=(N, S, W, E))
        ttk.Button(mainframe, text="^v", command=changetheinputs).grid(column=2, row=3, sticky=(N, S, W, E))
        def convert(finalunit, quantity, startingunit):
            meters = unitsinmeters[startingunit]
            totalmeters = meters * int(str(quantity.get()))
            total = totalmeters / unitsinmeters[finalunit]
            total = round(total)
            final = total + " " + finalunit
            output.set(final)
        ttk.Button(mainframe, text="CONVERT", command=lambda:convert(unitoutputbox.get(), quaninput, unitinputbox.get())).grid(column=1, row=5, columnspan=2, padx=100, pady=(12, 0), sticky=(N, S, W, E))
        unitinputbox = ttk.Combobox(mainframe, state="readonly", values=getinputname())
        unitinputbox.grid(column=2, row=2, sticky=(N, S, W, E))
        unitoutputbox = ttk.Combobox(mainframe, state="readonly", values=getinputname())
        unitoutputbox.grid(column=2, row=4, sticky=(N, S, W, E))
        unitinputbox.set("meter")
        unitoutputbox.set("foot")
        def changeinputs(unitinputbox, unitoutputbox):
            inputbefore = unitinputbox.get()
            outputbefore = unitoutputbox.get()
            unitinputbox["values"] = outputbefore
            unitoutputbox["values"] = inputbefore
        quantityinput = ttk.Entry(mainframe, textvariable=quaninput)
        quantityinput.grid(column=1, row=2, sticky=(N, S, W, E))
        # Configure the entry
        quaninput.set("")
        quantityinput.focus()
        mainframe.pack(expand=1)
        # Bindings
        self.bind('<Return>', lambda event:convert(unitoutputbox.get(), quaninput, unitinputbox.get()))





root = Application() # La ventana en si
root.title("Feet to Meters") # Titulo de la ventana
# Set the minnimum window size
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
