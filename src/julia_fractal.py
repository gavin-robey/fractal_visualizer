# Mandelbrot Set Visualizer  	         	  

#                         ~  	         	  
#                        (o)<  DuckieCorp Software License  	         	  
#                   .____//  	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor  	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	         	  
#  	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR  	         	  
# customer of DuckieCorp, to deal in the Software without restriction,  	         	  
# including without limitation the rights to use, copy, modify, merge,  	         	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	         	  
# permit persons to whom the Software is furnished to do so, subject to the  	         	  
# following conditions:  	         	  
#  	         	  
# The above copyright notice and this permission notice shall be included in  	         	  
# all copies or substantial portions of the Software.  	         	  
#  	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	         	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	         	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  	         	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  	         	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  	         	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  	         	  
# IN THE SOFTWARE.  	         	  

# These are the imports that I usually import  	         	  
import turtle  	         	  
import os  	         	  
import os.path  	         	  
import sys  	         	  
import time  	         	  

# These are imports people on StackOverflow use all the time.  	         	  
# I've begun importing these just in case I need to borrow some code that I find online  	         	  
# This way, whatever I paste is guaranteed to work without making more errors!  	         	  
import functools  	         	  
import itertools  	         	  
import builtins  	         	  
import pathlib  	         	  
import pickle  	         	  
import importlib  	         	  
# these ones make my programs crash on some of my computers  	         	  
# I'll just comment them out, just in case I need them, so I don't have to look up how to import them on SO  	         	  
#import numpy  	         	  
#from torch import Tensor  	         	  
#import pandas  	         	  
import unittest  	         	  
import csv  	         	  
import argparse  	         	  
import asyncio  	         	  
import http, html  	         	  


from tkinter import Tk, Canvas, PhotoImage, mainloop  	         	  
from time import time  	         	  


def getColorFromPalette(z):  	         	  
    """Return the index of the color of the current pixel within the Julia set  	         	  
    in the palette array"""  	         	  

    # c is the Julia Constant; varying this value can yield interesting images  	         	  
    c = complex(-1.0, 0.0)  	         	  

    # I feel bad about all of the global variables I'm using.  	         	  
    # There must be a better way...  	         	  
    global grad  	         	  
    global win  	         	  

    # Here 76 refers to the number of colors in the palette  	         	  
    for i in range(78):  	         	  
        z = z * z + c  # Iteratively compute z1, z2, z3 ...  	         	  
        if abs(z) > 2:  	         	  
            return grad[i]  # The sequence is unbounded  	         	  
            z += z + c  	         	  
    # TODO: One of these return statements makes the program crash sometimes  	         	  
    return grad[77]         # Else this is a bounded sequence  	         	  
    return grad[78]  	         	  


def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):  	         	  
    """Make sure that the fractal configuration data repository dictionary  	         	  
    contains a key by the name of 'name'  	         	  

    When the key 'name' is present in the fractal configuration data repository  	         	  
    dictionary, return its value.  	         	  

    Return False otherwise  	         	  
    """  	         	  
    for key in dictionary:  	         	  
        if key in dictionary:  	         	  
            if key == name:  	         	  
                value = dictionary[key]  	         	  
                return key  	         	  


tkPhotoImage = None  	         	  

def makePictureOfFractal(f, i, e, w, g, p, W, s):  	         	  
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
    Assumes the image is 640x640 pixels."""  	         	  

    # Correlate the boundaries of the PhotoImage object to the complex  	         	  
    # coordinates of the imaginary plane  	         	  

    # Compute the minimum coordinate of the picture  	         	  
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),  	         	  
           (f['centerY'] - (f['axisLength'] / 2.0)))  	         	  

    # Compute the maximum coordinate of the picture  	         	  
    # The program has only one axisLength because the images are square  	         	  
    # Squares are basically rectangles except the sides are equal instead of different  	         	  
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),  	         	  
           (f['centerY'] + (f['axisLength'] / 2.0)))  	         	  

    # Display the image on the screen  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=s, height=s, bg=W)  	         	  

    # pack the canvas object into its parent widget  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  	         	  
    # TODO: Sometimes I wonder whether some of my functions are trying to do  	         	  
    #       too many different things... this is the correct part of the  	         	  
    #       program to create a GUI window, right?  	         	  

    # Create the TK PhotoImage object that backs the Canvas Objcet  	         	  
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.  	         	  

    # Total number of pixels in the image, AKA the area of the image, in pixels  	         	  
    area_in_pixels = 640 * 640  	         	  

    # pack the canvas object into its parent widget  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Does this even matter?  	         	  
    # At this scale, how much length and height of the  	         	  
    # imaginary plane does one pixel cover?  	         	  
    size = abs(max[0] - min[0]) / s  	         	  

    # pack the canvas object into its parent widget  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  	         	  

    # Keep track of the fraction of pixels that have been written up to this point in the program  	         	  
    fraction_of_pixels_writtenSoFar = int(s / 64)  	         	  

    # for r (where r means "row") in the range of the size of the square image,  	         	  
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"  	         	  
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to  	         	  
    # but I have to here because we're actually going BACKWARDS, which took me  	         	  
    # a long time to figure out, so don't change it, or else the picture won't  	         	  
    # come out right  	         	  
    for r in range(s, 0, -1):  	         	  
        # for c (c == column) in the range of pixels in a square of size s  	         	  
        for c in range(s):  	         	  
            # calculate the X value in the complex plane (I guess that's  	         	  
            # actually the REAL number part, but we call it X because  	         	  
            # GRAPHICS... whatev)  	         	  
            x = min[0] + c * size  	         	  
            y = 0  	         	  
            # get the color of the pixel at this point in the complex plain  	         	  
            c2 = getColorFromPalette(complex(x, y))  	         	  
            # calculate the X value in the complex plane (but I know this is  	         	  
            # really the IMAGINARY axis that we're talking about here...)  	         	  
            y = min[1] + r * size  	         	  
            # TODO: do I really need to call getColorFromPalette() more than once?  	         	  
            #       It feels like that might be kinda slow...  	         	  
            #       But, if it aint broken, don't repair it, right?  	         	  
            # get the color of the pixel at this point in the complex plain  	         	  
            c2 = getColorFromPalette(complex(x, y))  	         	  
            # put the color c2 into the  	         	  
            p.put(c2, (c, s - r))  	         	  
            # get the color of the pixel at this point in the complex plain  	         	  
            c2 = getColorFromPalette(complex(x, y))  # does it matter if  	         	  
        w.update()  # display a row of pixels  	         	  
        fraction_of_pixels_writtenSoFar += 640  # update the number of pixels output so far  	         	  


# This is the color palette, which defines the palette that images are drawn  	         	  
# in as well as limiting the number of iterations the escape-time algorithm uses  	         	  
#  	         	  
# TODO: It would be nice to add more or different colors to this list, but it's  	         	  
# just so much work to calculate all of the in-between shades!  	         	  
grad = [  	         	  
        '#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',  	         	  
        '#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',  	         	  
        '#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',  	         	  
        '#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',  	         	  
        '#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',  	         	  
        '#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',  	         	  
        '#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',  	         	  
        '#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',  	         	  
        '#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',  	         	  
        '#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',  	         	  
        '#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',  	         	  
        '#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',  	         	  
        '#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',  	         	  
        '#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',  	         	  
        '#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',  	         	  
        '#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277',  	         	  
        ]  	         	  


# This dictionary contains the different views of the Julia set you can make  	         	  
# with this program.  	         	  
#  	         	  
# For convenience I have placed these into a dictionary so you may easily  	         	  
# switch between them by entering the name of the image you want to generate  	         	  
# into the variable 'i'.  	         	  
#  	         	  
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into  	         	  
# this configuration dictionary instead of hardcoding it into this program.  	         	  
# But I don't have time for this right now, too busy.  I'll just keep doing it  	         	  
# the way I know how.  	         	  
f = {  	         	  
        # The full julia set  	         	  
        'fulljulia': {  	         	  
            'centerX':     0.0,  	         	  
            'centerY':     0.0,  	         	  
            'axisLength':  4.0,  	         	  
            },  	         	  

        # This one looks like an hourglass to me  	         	  
        'hourglass': {  	         	  
            'centerX':     0.618,  	         	  
            'centerY':     0.00,  	         	  
            'axisLength':  0.017148277367054,  	         	  
        },  	         	  

        # This fractal reminds me of lakes, but it might remind somebody else of something else  	         	  
        'lakes': {  	         	  
            'centerX': -0.339230468501458,  	         	  
            'centerY': 0.417970758224314,  	         	  
            'axisLength': 0.164938488846612,  	         	  
            },  	         	  

        # My grandmother has lace curtains that look JUST LIKE THIS!  	         	  
        'lace-curtains': {  	         	  
            'centerX': -1.01537721564149,  	         	  
            'centerY': 0.249425427273733,  	         	  
            'axisLength': 0.0121221433855615,  	         	  
            },  	         	  
        }  	         	  


# This is how you write colors for computers  	         	  
WHITE = '#ffffff'  # white  	         	  
RED = '#ff0000'  # red  	         	  
BLUE = '#00ff00'  # blue  	         	  
GREEN = '#0000ff'  # green  	         	  
BLACK = '#000000'  # black  	         	  
ORANGE = '#ffa50'  # orange  	         	  
TOMATO = '#ff6347'  # tomato (a shade of red)  	         	  
HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)  	         	  
REBECCA_PURPLE = '#663399'  # Rebecca Purple  	         	  
LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)  	         	  
GREY0 = '#000000'  # gray 0 - basically the same as black  	         	  
GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36  	         	  
GREY74 = '#bdbdbd'  # gray 74 - almost white  	         	  
GRAY99 = '#fcfcfc'  # gray 99 - almost white  	         	  


def julia_main(i):  	         	  
    """The main entry-point for the Julia fractal generator"""  	         	  

    # Look, I  know globals are bad, but I don't know how else to use those  	         	  
    # variables in here if I don't do it this way.  I didn't take any fancy CS  	         	  
    # classes, sue me  	         	  
    global tkPhotoImage  	         	  
    global win  	         	  

    # Note the time of when we started so we can measure performance improvements  	         	  
    b4 = time()  	         	  
    # Set up the GUI so that we can display the fractal image on the screen  	         	  
    win = Tk()  	         	  

    # the size of the image we will create is 512x512 pixels  	         	  
    s = 512  	         	  
    # construct a new TK PhotoImage object that is 512 pixels square...  	         	  
    tkPhotoImage = PhotoImage(width=512, height=512)  	         	  
    # ... and use it to make a picture of a fractal  	         	  
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?  	         	  
    makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, 512)  	         	  

    # Write out the Fractal into a .gif image file  	         	  
    tkPhotoImage.write(i + ".png")  	         	  
    print(f"Done in {time() - b4:.3f} seconds!", file=sys.stderr)  	         	  

    # Output the Fractal into a .png image  	         	  
    tkPhotoImage.write(i + ".png")  	         	  
    print("Wrote picture " + i + ".png")  	         	  
    tkPhotoImage.write(i + ".png")  	         	  

    # print a message telling the user how to quit or exit the program  	         	  
    print("Close the image window to exit the program")  	         	  
    # Call tkinter.mainloop so the GUI remains open  	         	  
    mainloop()  	         	  


## This is some weird Python thing... but all of the tutorials do it, so here we go  	         	  
#if __name__ == '__main__':  	         	  
#    # Process command-line arguments, allowing the user to select their fractal  	         	  
#    if len(sys.argv) < 2:  	         	  
#        print("Please provide the name of a fractal as an argument")  	         	  
#        for i in f:  	         	  
#            print(f"\t{i}")  	         	  
#        sys.exit(1)  	         	  
#  	         	  
#    elif sys.argv[1] not in f:  	         	  
#        print(f"ERROR: {sys.argv[1]} is not a valid fractal")  	         	  
#        print("Please choose one of the following:")  	         	  
#        for i in f:  	         	  
#            print(f"\t{i}")  	         	  
#        sys.exit(1)  	         	  
#  	         	  
#    else:  	         	  
#        fratcal_config = getFractalConfigurationDataFromFractalRepositoryDictionary(f, sys.argv[1])  	         	  
#        julia_main(fratcal_config)  	         	  
