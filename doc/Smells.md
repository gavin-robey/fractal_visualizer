# Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
*	Copy the offensive code
*	Explain why the smell is a problem
*	Describe how you can fix


### These are some of the code smells you may find in the starter code:

0.  "Magic" numbers
    *   Numeric literals that appear in critical places but without any apparent meaning
    *   "When I see the number `214` here, does it have the same meaning as the `214` over there?"
1.  Global variables
    *   A global is being used to avoid passing a parameter into a function
    *   A global is being used to return an extra value from a function
2.  Poorly-named variables
    *   Variables with one-letter long names are okay to use in special contexts; otherwise, they should be avoided
        *   For example, a counter called `i` or `j` used in a `for` loop that is but a few lines long
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
    *   Variables with really, really long names can make code *less* easy to read
    *   If a programmer is not careful, variables can accidentally override or "shadow" other identifiers in a program
        *   Builtin Python functions such as `input`, `len`, `list`, `max`,
            `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness
3.  Comments that share too much information
    *   A function or method is filled with many explanatory comments
    *   This is often done because the variable names and function names are poorly chose
    *   Rather, let the code speak for itself
4.  Comments that lie to you
    *   A comment which may have once been helpful, but no longer accurately describes the code
    *   A comment that is straight-up misleading, perhaps written by a developer without a clue
5.  Parameter list that is too long
    *   More than three or four parameters for a method
    *   Parameters that are passed in but left unused
6.  Function/Method that is too long
    *   A method contains too many lines of code
    *   Typically this happens because the method has too many different responsibilities
    *   Generally, any method longer than ten lines should make you ask the question "what if I split this into smaller, more focused pieces?"
7.  Overly complex decision trees
    *   Overly long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Have all of the branches been tested?
8.  Spaghetti code
    *   Lots of meandering code without a clear goal
    *   Many functions/objects used in inconsistent ways
    *   All code is contained in one giant function/method with huge `if/else` branches
    *   "It would be easier to rewrite this than to understand it"
9.  Redundant code
    *   When you see a line of code that is repeated, ask whether it makes any difference to be run more than once.
10. Dead code
    *   A variable, parameter, field, method or class is no longer used (usually because it is obsolete)
    *   Big blocks of commented-out code that serve no purpose and clutter up the file

Other code smells may be present; list them as well.

## Code Smells

0. `src/mbrot_fractal.py`, [lines 31-32 (At the very top of the file)]
        * [What kind of code smell is this?] This is **dead code**
        * [Why is the smell a problem?] All this code is not used and will never be used, it is just cluttering up the entire file and making it very hard to read.
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
        *   [Explain what you changed]] I deleted the unneccessary commented out code.
1. In `src/mbrot_fractal.py` in the `colorOfThePixel()` function, [Lines 98-104 (Roughly close to the top of the file)]
        * [What kind of code smell is this?] This is an example of using **Global Variables**
        * [Why is the smell a problem?] Global variables allow functions to have hard to detect problems occur. This same functionality can be recreated using a class and its data members.
   * Code Snippet:
   ```python
        def colorOfThePixel(c, palette):  	         	  
             """Return the color of the current pixel within the Mandelbrot set"""  	         	  
             global z  	         	  
             z = complex(0, 0)  # z0  	         	  

             global MAX_ITERATIONS  	         	  
             global iter 
   ```
    *   How the code smell was fixed:
        *   [Explain what you changed]] I deleted all the global variables and replaced them with data members in a class to be used throughout the program.

2. In `src/mbrot_fractal.py` in the `colorOfThePixel()` function, [Lines 107-126 (Towards the bottom of the function)]
   * [What kind of code smell is this?] This is an example of  **Overly complex decision trees** and **Dead code**
   * [Why is the smell a problem?] There are far too many if elif statements, the only one that is needed is the first if statement. Inside these if else statements are examples of dead code. For instance, in lines ``118`` and `126` these statements are never reached because they are either under a continue statement or a return statement.
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
        * [Explain what you changed]] I deleted all unnessecary if elif else statements and deleted all dead code.

3. In `src/mbrot_fractal.py` in the `paint()` function, [Lines 131-164 (In the middle of the file)]
   * [What kind of code smell is this?] This is an example of using **Magic Numbers** and using **Global variables**.
   * [Why is the smell a problem?] It's nearly impossible to understand what the numbers on lines `160`,`164` etc, mean and what they are doing. It is also very difficult to create reusable code with these values. This section of the program is also using global variables again on lines `139` and `140`.
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
        * [Explain what you changed]] I renamed these magic numbers with meaningful names so that their purpose can be understood.

4. In `src/mbrot_fractal.py`, [Lines 173-202 (In the middle of the file)]
   * [What kind of code smell is this?] This is an example of using **Dead Code**.
   * [Why is the smell a problem?] This is just taking up way too much space that is being taken up, and is cluttering and confusing this file.
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
        * [Explain what you changed]] I deleted all the meaningless lines that were commented out.

5. In `src/mbrot_fractal.py` in the `ages {}` dictionary, [Lines 203-257 (Towards the end of the file)]
   * [What kind of code smell is this?] This is an example of using **Redundent Code**.
   * [Why is the smell a problem?] Line `234` takes up way too much space and does nothing because it has been written twice.
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
        * [Explain what you changed]] I deleted the redundent code.

6. In `src/mbrot_fractal.py`, [Lines 44-51 (At the beginning of the file)]
   * [What kind of code smell is this?] This is an example of using **Dead Code** and **Redundent Code**.
   * [Why is the smell a problem?] Some of the color variables, are never used and the colors themselves are quite random, which makes me want to delete them in a way. Also for some reason MAX_ITERATIONS is set to -1 but is then used later and sets itself equal to another value thus making it in this instace useless.
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
     * [Explain what you changed]] I deleted the redundent code and removed the color variables and replaced the items in the list with the respective color hash codes.
   
7. In `src/mbrot_fractal.py`, [Lines 197-202 (Towards the end of the file)]
   * [What kind of code smell is this?] This is an example of **Comments that share too much information** .
   * [Why is the smell a problem?] I know what a dictionary does, I do not need all the explenation.
    ```python
    # These are the different views of the Mandelbrot set you can make with this  	         	  
    # program.  	         	  
    #  	         	  
    # For convenience I have placed these into a dictionary so you may easily  	         	  
    # switch between them by entering the name of the image you want to generate  	         	  
    # into the variable 'image'.  
   ```

  * How the code smell was fixed:
       * [Explain what you changed]] I deleted the redundent code.
    
8. In `src/juila_fractal.py`, [Lines 28-52 (At the top of the file)]
   * [What kind of code smell is this?] This is an example of  **Dead Code** and **Comments that share too much information**.
   * [Why is the smell a problem?] Unused import statements takes up space, they are not relevant and make the file very unreadable. These comments do not add anything to the overall file.
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
     * [Explain what you changed]] I deleted the poorly commented code and deleted all unused import statements.
   
9. In `src/juila_fractal.py` in `getColorFromPallete`, [Lines 59-69 (At the top of the file/ function)]
   * [What kind of code smell is this?] This is an example of using **Poorly named variables**.
   * [Why is the smell a problem?] The variables used in this function have either one letter names of names that do not make much sense. This is a problem because this makes the code in the file much less readable and more difficult to implement.
   ```python
    def getColorFromPalette(z):  	         	  
        """Return the index of the color of the current pixel within the Julia set  	         	  
        in the palette array"""  	         	  
    
        # c is the Julia Constant; varying this value can yield interesting images  	         	  
        c = complex(-1.0, 0.0)  	         	  
    
        # I feel bad about all of the global variables I'm using.  	         	  
        # There must be a better way...  	         	  
        global grad  	         	  
        global win  
   ```
   * How the code smell was fixed:
        * [Explain what you changed] I changed the parameter names to much more meaningful names such as `"c"` to `juliaConstant`. This conveys the meaning much easier.

10. In `src/juila_fractal.py` in `getColorFromPallete`, [Lines 71-79 (At the top of the file/ bottom of the function)]
     *[What kind of code smell is this?] This is an example of using **Magic Numbers** and **Dead Code**.
     *[Why is the smell a problem?] At the moment I have no idea what this snippet of code does. This is very un readable
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
        * [Explain what you changed] I used the length of the color palette instead, this is more descriptive and makes understanding this code much easier.

11. In `src/juila_fractal.py`, [Lines 82-95 (At the top of the file)]
     *[What kind of code smell is this?] This is an example of using **Poor Names**.
     *[Why is the smell a problem?] This function name is far too long and is just plain confusing. Looking at the code further reveals that this function is actually never used, and when deleted, the code still runs perfectly.
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
            * [Explain what you changed] I deleted the entire function since it does not do anything at all.
    
12. In `src/juila_fractal.py` in `makePictureOfFractal`, [Lines 100-177 (Int the middle of the file)]
     *[What kind of code smell is this?] This is an example of a **Function that is too long** and a **Function with a parameter list that is too long.**.
     *[Why is the smell a problem?]   This function does way too many things, this functionality needs to be broken up, in fact I have no idea all of what it does yet. It also has a ridiculously long parameter list with horrible names. Half if not most of the parameters are not even being used in function itself and must be deleted.
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
      * [Explain what you changed] There are parts of this function that should be done with all the other TKinter processes, these will all be done in a separate class.
      
13. In `src/juila_fractal.py`, [Lines 208-211 (Towards the end of the file)]
     *[What kind of code smell is this?] This is an example of **Comments that lie to you**.
     *[Why is the smell a problem?] Comments like these are misleading and make it hard to understand the code in its current state. The reason why this specific line of comments is wrong, is because the function the author is describing no longer exists and has been replaced with a different function.
    ````python
    # For convenience I have placed these into a dictionary so you may easily  	         	  
    # switch between them by entering the name of the image you want to generate  	         	  
    # into the variable 'i'.  	         	  
    #  	         	  
    ````
    * How the code smell was fixed:
      * [Explain what you changed] This fix is too simple, I deleted the comments and replaced them with accurate information.

14. In `src/juila_fractal.py` in the `makePictureOfFractal` function, [Lines 154-176 (Towards the end of the file)]
     *[What kind of code smell is this?] This is an example of **Spaghetti Code**.
     *[Why is the smell a problem? Most of this code is useless, its also in a giant nested for loop, which means it's both barely readable and is also unnecessarily inefficient. c2 is called and overridden multiple times.
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
      * [Explain what you changed] I deleted unused code and condensed this to look exactly like the mbrot_fractal version of this function that did the exact same thing.    