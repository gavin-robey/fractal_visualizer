'''
This module is the main driver of the program.
This module accepts input from the user via the command line and displays a fractal picture depending on user input.
This module imports 3 modules: sys, ImagePainter, and FractalInformation
Most of this file will be very simular to the starter code, the only things to change will be which modules are used to
output the picture.
All of the commands for either the Julia algorithm or the Mandelbrot algorithm are stored in a list.
This is done to check if the given command is valid.
If there are no arguments given, then the program will display all the fractal types the user can enter, and then exits the program.
If there is an argument that is passed in, but it is not valid then an error message will display,
all the fractal types will be displayed, and the program will exit.
If there is an argument that is passed in, and it is valid, then the appropriate algorithm will be used.
This will be achieved by calling the ImagePainter class and passing in the fractal information and the fractal type
'''
import sys
from ImagePainter import ImagePainter
from FractalInformation import fractals

JULIAS = ['fulljulia', 'hourglass', 'lace-curtains', 'lakes']
MBROTS = ['elephants', 'leaf', 'mandelbrot', 'mandelbrot-zoomed', 'seahorse', 'spiral0', 'spiral1', 'starfish']


def displayOptions(message):
    '''
    Return: None
    This function is not included on the original plan, this was created to reduce redundency
    This function has one parameter: message which is a string
    This function prints a message to the user and displays all options of fractal types then exits the program
    '''
    print(message)
    for i in JULIAS + MBROTS:
        print(f"\t{i}")
    sys.exit(1)


if len(sys.argv) < 2:
    displayOptions("Please provide the name of a fractal as an argument")
elif sys.argv[1] not in JULIAS + MBROTS:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    displayOptions("Please choose one of the following:")
else:
    fractalName = sys.argv[1]
    if sys.argv[1] in JULIAS:
        ImagePainter(fractalName, fractals, fractals[fractalName]["type"])
    elif sys.argv[1] in MBROTS:
        ImagePainter(fractalName, fractals, fractals[fractalName]["type"])
