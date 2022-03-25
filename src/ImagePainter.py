from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
from Palette import Palette
import Julia
import Mandelbrot
import sys


class ImagePainter:

    def __init__(self, imageName, fractalInformation, fractalType):
        '''
        This class returns None, in order to draw a picture to the screen just initialize this class.
        This class has 3 arguments:
        imageName: String
        fractalInformation: Dictionary with keys of type String and values of type Integer
        fractalType: String
        This class has 7 data members:
        imageName: String
        fractal: Dictionary with keys of type String and values of type Integer
        fractalType: String
        window: a window created from the tkinter module
        windowSize: Integer representing the size of the window
        img: the PhotoImage class that stores all the pixels for our image at a given size
        main: calls the main method so that this class can run without calling any methods
        This class imports 6 modules: tkinter, time, Palette, sys, Julia, and Mandelbrot
        This class creates the picture of the specified fractal and draws it to the screen using the tkinter module.
        This class also uses the fractal information to find the distance between points and passes that data into the
        Palette class to determine the color of each pixel.
        All of these calculations are timed and the time that it takes to do these operations is printed to the console.
        '''
        self.__imageName = imageName
        self.__fractal = fractalInformation[imageName]
        self.__fractalType = fractalType
        self.__window = Tk()
        self.__windowSize = 512
        self.__img = PhotoImage(width=self.__windowSize, height=self.__windowSize)
        self.__main()

    def __main(self):
        '''
        Returns: None
        Times how long it takes to create and display a picture to the screen.
        Creates a file containing the image created and exports it with the name of the algorithm type
        Prints out messages to the user explaining the time it took, as well as the name of the file that
        was created.
        Keeps the window of the picture made open.
        '''
        before = time()
        self.__display()
        after = time()

        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        self.__img.write(f"{self.__imageName}.png")
        print(f"Wrote image {self.__imageName}.png")
        print("Close the image window to exit the program")
        mainloop()

    def __display(self):
        '''
        This method returns: None
        This method has no arguments.
        This method finds the distance between the smallest x value, the largest x value, and the smallest y value.
        It then takes those values and finds the pixel size.
        It then creates a canvas that is the size of the window, this canvas is whats used to create an image on a window.
        This method then iterates over every row and column to input each pixel.
        In this iteration, it uses the Palette class to determine what color the pixel is then adds this pixel to the canvas
        Then this method updates the window so all the changes to the canvas mad above are saved.
        '''
        minx = self.__fractal['centerX'] - (self.__fractal['axisLen'] / 2.0)
        maxx = self.__fractal['centerX'] + (self.__fractal['axisLen'] / 2.0)
        miny = self.__fractal['centerY'] - (self.__fractal['axisLen'] / 2.0)
        pixelSize = abs(maxx - minx) / self.__windowSize

        canvas = Canvas(self.__window, width=self.__windowSize, height=self.__windowSize, bg='#000000')
        canvas.pack()
        canvas.create_image((self.__windowSize / 2, self.__windowSize / 2), image=self.__img, state="normal")

        for row in range(self.__windowSize, 0, -1):
            for col in range(self.__windowSize):
                x = minx + col * pixelSize
                y = miny + row * pixelSize
                color = Palette(self.__fractalType, complex(x, y), Julia, Mandelbrot).getPixelColor()
                self.__img.put(color, (col, self.__windowSize - row))
            self.__window.update()  # display a row of pixels
