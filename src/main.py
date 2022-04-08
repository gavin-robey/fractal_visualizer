'''
This module is the main driver of the program.
This module accepts input from the user via the command line and displays a fractal picture depending on user input.
This module imports 5 modules: sys, ImagePainter, FractalParser, FractalFactory, and PaletteFactory
This module will check whether the user has not entered a file, has entered a file or has entered a file and a palette.
In each scenario, the FractalParser, FractalFactory, PaletteFactory will be called.
Their parameters will be different depending on the scenario.
Their output will then be passed into the ImagePainter class.
All errors will be handled in their respective classes.
'''
import sys
from FractalParser import FractalParser
from FractalFactory import FractalFactory
from ImagePainter import ImagePainter
from PaletteFactory import PaletteFactory

if len(sys.argv) == 1:
    fractalFactory = FractalFactory().makeFractal()
    fractalInformation = FractalFactory().configuration
    paletteFactory = PaletteFactory().makePalette(fractalInformation["iterations"])

    print("creating default fractal")
    print("creating a default palette")

    ImagePainter(fractalInformation, fractalFactory, paletteFactory)

elif len(sys.argv) == 2:
    fractalInformation = FractalParser(sys.argv[1]).getConfiguration()
    fractalFactory = FractalFactory().makeFractal(fractalInformation)
    paletteFactoy = PaletteFactory().makePalette(fractalInformation["iterations"])

    print(f"creating a {fractalInformation['name']} fractal")
    print("creating a default palette")

    ImagePainter(fractalInformation, fractalFactory, paletteFactoy)

elif len(sys.argv) == 3:
    fractalInformation = FractalParser(sys.argv[1]).getConfiguration()
    fractalFactory = FractalFactory().makeFractal(fractalInformation)
    paletteFactoy = PaletteFactory().makePalette(fractalInformation["iterations"], sys.argv[2])

    print(f"creating a {fractalInformation['name']} fractal")
    print(f"creating a {sys.argv[2]} palette")

    ImagePainter(fractalInformation, fractalFactory, paletteFactoy)



