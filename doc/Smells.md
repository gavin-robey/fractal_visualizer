# Code Smells Report

## Code Smells

0. `src/mbrot_fractal.py`, [lines 31-32 (At the very top of the file)]
    *  This is **dead code**
    * All this code is not used and will never be used, it is just cluttering up the entire file and making it very hard to read.
    *   Code Snippet:
        ```python
        #from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh  	         	  
        
        # These are the imports that I usually import  	         	  
        # import turtle  	         	  
        # import os  	         	  
        # import os.path  	         	  
        # import sys  	         	  
        # import time  	         	  
        # import math  	         	  
        
        # this import caused problems on my Windows computer...  	         	  
        # import numpy  
        ```
    *   How the code smell was fixed:
        * I deleted the unnecessary commented out code.
        

1. In `src/mbrot_fractal.py` in the `colorOfThePixel()` function, [Lines 98-104 (Roughly close to the top of the file)]
   * This is an example of using **Global Variables**
   * Global variables allow functions to have hard to detect problems occur. This same functionality can be recreated using a class and its data members.
   * Code Snippet:
   ```python
        def colorOfThePixel(c, palette):  	         	  
             """Return the color of the current pixel within the Mandelbrot set"""  	         	  
             global z  	         	  
             z = complex(0, 0)  # z0  	         	  

             global MAX_ITERATIONS  	         	  
             global iter 
   ```
    * How the code smell was fixed:
        * I deleted all the global variables and replaced them by creating functions that pass these variables in.
    ```python
        def colorOfThePixel(c, palette, maxIterations, iter):  	         	  
             """Return the color of the current pixel within the Mandelbrot set"""  	         	          	  
             z = complex(0, 0)  # z0  	         	  
    ```
 


2. In `src/mbrot_fractal.py` in the `colorOfThePixel()` function, [Lines 107-126 (Towards the bottom of the function)]
   *  This is an example of  **Overly complex decision trees** and **Dead code**
   * There are far too many if elif statements, the only one that is needed is the first if statement. Inside these if else statements are examples of dead code. For instance, in lines ``118`` and `126` these statements are never reached because they are either under a continue statement or a return statement.
   ```python
    len = MAX_ITERATIONS  	         	  
    for iter in range(len):  	         	  
        z = z * z + c  # Get z1, z2, ...  	         	  
        global TWO  	         	  
        if abs(z) > TWO:  	         	  
            z = float(TWO)  	         	  
            return palette[iter]  # The sequence is unbounded  	         	  
        elif abs(z) < TWO:  	         	  
            continue  	         	  
        elif abs(z) > seven:  	         	  
            print("You should never see this message in production")  	         	  
            continue  	         	  
            break  	         	  
        elif abs(z) < 0:  	         	  
            print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}")  	         	  
            sys.exit(1)  	         	  
        else:  	         	  
            pass  	         	  
    # XXX: one of these return statements made the program crash...  	         	  
    return palette[MAX_ITERATIONS - 1]   # Indicate a bounded sequence  	         	  
    return palette[MAX_ITERATIONS]  	         	  
   ```
   * How the code smell was fixed:
        *  I deleted all unnessecary if elif else statements and deleted all dead code.
   ```python
    for iter in range(len):  	         	  
        z = z * z + c  # Get z1, z2, ...  	         	   	  
        if abs(z) > 2:  	         	  
            z = float(TWO)  	         	  
            return palette[iter]  # The sequence is unbounded  
   ```


3. In `src/mbrot_fractal.py` in the `paint()` function, [Lines 131-164 (In the middle of the file)]
   *  This is an example of using **Magic Numbers** and using **Global variables**.
   * It's nearly impossible to understand what the numbers on lines `160`,`164` etc, mean and what they are doing. It is also very difficult to create reusable code with these values. This section of the program is also using global variables again on lines `139` and `140`.
   ```python
     def paint(fractals, imagename):  	         	  
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
    This code creates an image which is 640x640 pixels in size."""  	         	  

    global palette  	         	  
    global img  	         	  

    fractal = fractals[imagename]  	         	  

    # Figure out how the boundaries of the PhotoImage relate to coordinates on  	         	  
    # the imaginary plane.  	         	  
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)  	         	  
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)  	         	  
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)  	         	  
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)  	         	  

    # Display the image on the screen  	         	  
    canvas = Canvas(window, width=512, height=512, bg='#000000')  	         	  
    canvas.pack()  	         	  
    canvas.create_image((256, 256), image=img, state="normal")  	         	  

    # At this scale, how much length and height on the imaginary plane does one  	         	  
    # pixel take?  	         	  
    pixelsize = abs(maxx - minx) / 512  	         	  

    portion = int(512 / 64)  	         	  
    total_pixels = 1048576  	         	  
    for row in range(512, 0, -1):  	         	  
        for col in range(512):  	         	  
            x = minx + col * pixelsize  	         	  
            y = miny + row * pixelsize  	         	  
            color = colorOfThePixel(complex(x, y), palette)  	         	  
            img.put(color, (col, 512 - row))  	         	  
        window.update()  # display a row of pixels  
   ```
    * How the code smell was fixed:
        *  I renamed these magic numbers with meaningful names so that their purpose can be understood.
    ```python
    windowSize = 512
    for row in range(windowSize, 0, -1):  	         	  
        for col in range(windowSize):  	         	  
            x = minx + col * pixelsize  	         	  
            y = miny + row * pixelsize  	         	  
            color = colorOfThePixel(complex(x, y), palette)  	         	  
            img.put(color, (col, windowSize - row))  	         	 
    ```

4. In `src/mbrot_fractal.py`, [Lines 173-202 (In the middle of the file)]
   *  This is an example of using **Dead Code**.
   *  This is just taking up way too much space that is being taken up, and is cluttering and confusing this file.
   ```python
    #def colorOfThePixel(c, colors):  	         	  
    #    """Return the color of the current pixel within the Mandelbrot set"""  	         	  
    #    global z  	         	  
    #    global MAX_ITERATIONS  	         	  
    #    global mainWindowObject  	         	  
    #    z0 = complex(0, 0)  # z0  	         	  
    #  	         	  
    #    for iter in range(MAX_ITERATIONS + 1):  	         	  
    #        z0 = z0 * z0 + c  	         	  
    #        # if the absolute value of z is less than TWO  	         	  
    #        ...         	  
   ```
   * How the code smell was fixed:
        *  I deleted all the meaningless lines that were commented out.


5. In `src/mbrot_fractal.py` in the `ages {}` dictionary, [Lines 203-257 (Towards the end of the file)]
   *  This is an example of using **Redundent Code**.
   *  Line `234` takes up way too much space and does nothing because it has been written twice.
   ```python
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

    'spiral1': {  	         	  
        'centerX': -0.747,  	         	  
        'centerY': 0.1075,  	         	  
        'axisLen': 0.002,  	         	  
    },
   ```
   * How the code smell was fixed:
        *  I deleted the redundent code.


6. In `src/mbrot_fractal.py`, [Lines 44-51 (At the beginning of the file)]
   * This is an example of using **Dead Code** and **Redundent Code**.
   * Some of the color variables, are never used and the colors themselves are quite random, which makes me want to delete them in a way. Also for some reason MAX_ITERATIONS is set to -1 but is then used later and sets itself equal to another value thus making it in this instace useless.
   ````python
    GRAPEFRUIT_PINK = '#e8283f'  	         	  
    LEMON = '#fdff00'  	         	  
    LIME_GREEN = '#89ff00'  	         	  
    KUMQUAT = '#fac309'  	         	  
    MAX_ITERATIONS = -1  	         	  
    POMELLO = '#2fff00'  	         	  
    TANGERINE = '#f7b604'  	         	  
    WHITE = '#ffffff'  	
   ````
   * How the code smell was fixed:
     * I deleted the redundant code and removed the color variables and replaced the items in the list with the respective color hash codes.
   

7. In `src/mbrot_fractal.py`, [Lines 197-202 (Towards the end of the file)]
   * This is an example of **Comments that share too much information** .
   * I know what a dictionary does, I do not need all the explanation.
    ```python
    # These are the different views of the Mandelbrot set you can make with this  	         	  
    # program.  	         	  
    #  	         	  
    # For convenience I have placed these into a dictionary so you may easily  	         	  
    # switch between them by entering the name of the image you want to generate  	         	  
    # into the variable 'image'.  
   ```

  * How the code smell was fixed:
    * I deleted the useless commments.
    

8. In `src/juila_fractal.py`, [Lines 28-52 (At the top of the file)]
   *  This is an example of  **Dead Code** and **Comments that share too much information**.
   *  Unused import statements takes up space, they are not relevant and make the file very unreadable. These comments do not add anything to the overall file.
   ```python
    # These are imports people on StackOverflow use all the time.  	         	  
    # I've begun importing these just in case I need to borrow some code that I find online  	         	  
    # This way, whatever I paste is guaranteed to work without making more errors!  	         	  
    import functools  	         	  
    import itertools  
    ...
    import argparse  	         	  
    import asyncio  	         	  
    import http, html  
   ```
   * How the code smell was fixed:
     *  I deleted the poorly commented code and deleted all unused import statements.
   

9. In `src/juila_fractal.py` in `getColorFromPallete`, [Lines 71-79 (At the top of the file/ bottom of the function)]
     *This is an example of using **Magic Numbers**, **Dead Code** and **Comments that lie to you**.
     * At the moment I have no idea what this snippet of code does. This is very un readable. On line 71, this comment is lying.
    ```python
    # Here 76 refers to the number of colors in the palette  	         	  
    for i in range(78):  	         	  
        z = z * z + c  # Iteratively compute z1, z2, z3 ...  	         	  
        if abs(z) > 2:  	         	  
            return grad[i]  # The sequence is unbounded  	         	  
            z += z + c  	         	  
    # TODO: One of these return statements makes the program crash sometimes  	         	  
    return grad[77]         # Else this is a bounded sequence  	         	  
    return grad[78]  	         	  
    ```
    * How the code smell was fixed:
        * I used the length of the color palette instead, this is more descriptive and makes understanding this code much easier. I also deleted the lying comment.

    ```python
    for i in range(len(grad)):  	         	  
        z = z * z + c  # Iteratively compute z1, z2, z3 ...  	         	  
        if abs(z) > 2:  	         	  
            return grad[i]  # The sequence is unbounded  	         	            	  
    return grad[len(grad) - 1]         # Else this is a bounded sequence  	         	  
    ```
   

10. In `src/juila_fractal.py`, [Lines 82-95 (At the top of the file)]
     * This is an example of using **Poor Names**.
     * This function name is far too long and is just plain confusing. Looking at the code further reveals that this function is actually never used, and when deleted, the code still runs perfectly.
     ```python
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
    ```
    * How the code smell was fixed:
            * I deleted the entire function since it does not do anything at all.
    

11. In `src/juila_fractal.py` in `makePictureOfFractal`, [Lines 100-177 (Int the middle of the file)]
     * This is an example of a **Function that is too long** and a **Function with a parameter list that is too long.**.
     * This function does way too many things, this functionality needs to be broken up, in fact I have no idea all of what it does yet. It also has a ridiculously long parameter list with horrible names. Half if not most of the parameters are not even being used in function itself and must be deleted.
    ```python
    def makePictureOfFractal(f, i, e, w, g, p, W, s):  	         	  
        """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
        Assumes the image is 640x640 pixels."""  	         	  
    
        ...        	  
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
    ```
    * How the code smell was fixed:
      * There are parts of this function that should be done with all the other TKinter processes, these will all be done in a separate class.
    
  
12. In `src/juila_fractal.py`, [Lines 208-211 (Towards the end of the file)]
     * This is an example of **Comments that lie to you**.
     * Comments like these are misleading and make it hard to understand the code in its current state. The reason why this specific line of comments is wrong, is because the function the author is describing no longer exists and has been replaced with a different function.
    ````python
    # For convenience I have placed these into a dictionary so you may easily  	         	  
    # switch between them by entering the name of the image you want to generate  	         	  
    # into the variable 'i'.  	         	  
    #  	         	  
    ````
    * How the code smell was fixed:
      *  This fix is too simple, I deleted the comments and replaced them with accurate information.


13. In `src/juila_fractal.py` in the `makePictureOfFractal` function, [Lines 154-176 (Towards the end of the file)]
     * This is an example of **Spaghetti Code**.
     * Most of this code is useless, its also in a giant nested for loop, which means it's both barely readable and is also unnecessarily inefficient. c2 is called and overridden multiple times.
    ```python
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
    ```
    * How the code smell was fixed:
      *  I deleted unused code and condensed this to look exactly like the mbrot_fractal version of this function that did the exact same thing.    