from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
import sys


class ImagePainter:

    def __init__(self, fractalInformation, fractalFactory, paletteFactory):
        '''
        This class creates the picture of the specified fractal and draws it to the screen using the tkinter module.
        This class also uses the fractal information to find the distance between points and passes that data into the
        Fractal.count() method to determine the color of each pixel.
        All of these calculations are timed and the time that it takes to do these operations is printed to the console.
        '''
        self.__fractalInformation = fractalInformation
        self.__fractalFactory = fractalFactory
        self.__paletteFactory = paletteFactory
        self.__window = Tk()
        self.__windowSize = fractalInformation["pixels"]
        self.__img = PhotoImage(width=self.__windowSize, height=self.__windowSize)
        self.__main()

    def __main(self):
        '''
        Creates a file containing the image created and exports it with the name of the algorithm type
        Prints out messages to the user explaining the time it took, as well as the name of the file that
        was created.
        Keeps the window of the picture made open.
        '''
        before = time()
        self.__display()
        after = time()

        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        self.__img.write(f"{self.__fractalInformation['name']}.png")
        print(f"Wrote image {self.__fractalInformation['name']}.png")
        print("Close the image window to exit the program")
        mainloop()

    def __display(self):
        '''
        This method finds the distance between the smallest x value, the largest x value, and the smallest y value.
        It then takes those values and finds the pixel size.
        It then creates a canvas that is the size of the window, this canvas is whats used to create an image on a window.
        This method then iterates over every row and column to input each pixel.
        In this iteration, it uses the Palette.getColor() method to determine what color the pixel is then adds this pixel to the canvas
        Then this method updates the window so all the changes to the canvas mad above are saved.
        '''
        minx = self.__fractalInformation['centerx'] - (self.__fractalInformation['axislength'] / 2.0)
        maxx = self.__fractalInformation['centerx'] + (self.__fractalInformation['axislength'] / 2.0)
        miny = self.__fractalInformation['centery'] - (self.__fractalInformation['axislength'] / 2.0)
        pixelSize = abs(maxx - minx) / self.__windowSize

        canvas = Canvas(self.__window, width=self.__windowSize, height=self.__windowSize, bg='#000000')
        canvas.pack()
        canvas.create_image((self.__windowSize / 2, self.__windowSize / 2), image=self.__img, state="normal")

        for row in range(self.__windowSize, 0, -1):
            for col in range(self.__windowSize):
                x = minx + col * pixelSize
                y = miny + row * pixelSize
                color = self.__paletteFactory.getColor(self.__fractalFactory.count(complex(x, y)))
                self.__img.put(color, (col, self.__windowSize - row))
            self.__window.update()
