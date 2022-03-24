import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop

# This color palette contains 100 color steps.
mbrotPalette = [
    '#89ff00', '#a4f817', '#baf12e', '#ccec43', '#d9e758', '#e3e46b', '#e1d97e',
    '#e0d18f', '#dfce9f', '#e0ceaf', '#e1d1bd', '#e4d6cb', '#e7ddd7', '#ece5e3',
    '#f1eeed', '#f8f7f7', '#ffffff', '#f8f7f7', '#f1eeed', '#ece4e3', '#e7dbd7',
    '#e4d3cb', '#e1cbbd', '#e0c4af', '#dfbf9f', '#e0bd8f', '#e1bc7e', '#e4bf6b',
    '#e7c458', '#eccd43', '#f1da2e', '#f8eb17', '#fdff00', '#f8eb17', '#f1da2e',
    '#eccd43', '#e7c458', '#e4bf6b', '#e1bc7e', '#e0bd8f', '#dfbf9f', '#e0c4af',
    '#e1cbbd', '#e4d3cb', '#e7dbd7', '#ece4e3', '#f1eeed', '#f8f7f7', '#ffffff',
    '#f7f6f6', '#f1eded', '#ebe4e2', '#e6dad7', '#e3d0ca', '#e0c6bd', '#debeae',
    '#deb69f', '#deaf8e', '#dfaa7d', '#e1a66b', '#e4a557', '#e9a643', '#eea92e',
    '#f4af17', '#f7b604', '#f4af17', '#eea92e', '#e9a643', '#e4a557', '#e1a66b',
    '#dfaa7d', '#deaf8e', '#deb69f', '#debeae', '#e0c6bd', '#e3d0ca', '#e6dad7',
    '#ebe4e2', '#f1eded', '#f7f6f6', '#ffffff', '#f8f7f7', '#f2f1ef', '#ebece5',
    '#e2e7db', '#d3e3d0', '#c5e0ca', '#b9ddce', '#abdbd9', '#9ec8da', '#8fa7da',
    '#8480db', '#9c70dc', '#c25fde', '#e04dcb', '#e43b8d', '#ffffff', '#f7f6f6',
    '#f0efec', '#e8eae1', '#dae5d5', '#c8e1cb', '#badecd', '#abdbd9', '#9cc4da',
    '#8b9cda', '#8d79db', '#b066dd', '#e052da', '#e33e97', '#e8283f', ]


def colorOfPixel(z, palette):
    """Return the color of the current pixel within the Mandelbrot set"""
    c = complex(0, 0)
    for i in range(len(palette)):
        c = c * c + z  # Get z1, z2, ...
        if abs(c) > 2:
            return palette[i]
    return palette[len(palette) - 1]


def paint(fractals, imageName, palette, img, window):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
    This code creates an image which is 640x640 pixels in size."""

    fractal = fractals[imageName]

    # Figure out how the boundaries of the PhotoImage relate to coordinates on the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)

    # Display the image on the screen  	         	  
    canvas = Canvas(window, width=512, height=512, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one pixel take?
    pixelSize = abs(maxx - minx) / 512

    for row in range(512, 0, -1):
        for col in range(512):
            x = minx + col * pixelSize
            y = miny + row * pixelSize
            color = colorOfPixel(complex(x, y), palette)
            img.put(color, (col, 512 - row))
        window.update()  # display a row of pixels  	         	  


# keeping this because this might be handy for the rewrite
def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")
    return pixels


# These are the different views of the Mandelbrot set you can make with this program.
images = {
    'mandelbrot': {
        'centerX': -0.6,
        'centerY': 0.0,
        'axisLen': 2.5,
    },

    'mandelbrot-zoomed': {
        'centerX': -1.0,
        'centerY': 0.0,
        'axisLen': 1.0,
    },

    'spiral0': {
        'centerX': -0.761335372924805,
        'centerY': 0.0835704803466797,
        'axisLen': 0.004978179931102462,
    },

    'spiral1': {
        'centerX': -0.747,
        'centerY': 0.1075,
        'axisLen': 0.002,
    },

    'seahorse': {
        'centerX': -0.745,
        'centerY': 0.105,
        'axisLen': 0.01,
    },

    'elephants': {
        'centerX': 0.30820836067024604,
        'centerY': 0.030620936230004017,
        'axisLen': 0.03,
    },

    'leaf': {
        'centerX': -1.543577002,
        'centerY': -0.000058690069,
        'axisLen': 0.000051248888,
    },

    'starfish': {
        'centerX': -0.463595023481762,
        'centerY': 0.598380871135558,
        'axisLen': 0.00128413675654471,
    },
}


def mbrot_main(image):

    # Set up the GUI so that we can paint the fractal image on the screen  	         	  
    before = time.time()
    window = Tk()
    img = PhotoImage(width=512, height=512)
    paint(images, image, mbrotPalette, img, window)

    # Save the image as a PNG  	         	  
    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{image}.png")
    print(f"Wrote image {image}.png")

    # Call tkinter.mainloop so the GUI remains open  	         	  
    print("Close the image window to exit the program")
    mainloop()
