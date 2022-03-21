# CS 1440 Assignment 4.1 Hints

## Students' advice from last semester

*   Have fun with it once your program is working. Git will let you go backwards, so try making more fractals, add in features, etc.
*   I tried to make the data I got from a fractal file easy to use and by assigning all numbers to be an int without realizing it would clobber all the floats and my program didn't work until I realized I was creating a massive logic error.
*   Don't overcomplicate simple things.
*   Do not overthink it, both people I know in this class and myself ran into issues because we were vastly overthinking and not looking at the program as a whole. 
*   Do not procrastinate at any level! Get started day one.
*   I forgot to remove the `\n` characters from the `.frac` files
*   Something that was effective for me was balancing the various structures between similar but different modules (such as my several fractal or palette modules) after performing any changes to any specific one.  This was incredibly useful for maintaining structure and order during this second half of the assignment.
*   Definitely have a clear idea for the purpose of abstraction and why it is important for code management, and definitely don't be afraid to ask the TA's for clarifications on things :)
*   The way I built the config file parser helped significantly. I focused on first breaking down each line into tokens in one part of the `FractalInformation.py` file, then I wrote a separate function for parsing these "tokens" into the standard data types and formats that the program expected, following the lexer and parser technique.
*   Really get creative with your own fractals! It's super awesome when you find an algorithm that looks pretty cool. I randomly came across an algorithm that kind of looked like the bat symbol!
*   I was super glad that I worked so hard to understand the code from assn4.0 because this made assn4.1 a lot easier. Of course I had to write a bunch of new code and completely change the implementation but that just took a lot of time so it wasn't too hard.
*   Reading and re-reading the instructions and following along step by step was really nice.
*   Start on the UML early. It is a really good planning tool
*   My computer renders RIDICULOUSLY slow, so trying to test without making the fractal images smaller was irritating.
*   Because my plan wasn't entirely complete, I ran into a wall partway through implementation when I wasn't sure how my classes and methods fit together.
*   Stick to the schedule. Finish the first part and understand how the program works on time. Then, when the second part arrives, reorganizing the code into classes and adding functionality will be easy.
*   Run your code often. I can really say that about any assignment, but if there's an assignment in this class where that especially applies, it's this one. You'll be breaking a LOT of code. Keep making sure your code works, tests are also good too.
*   If you feel you did well on assignment 4.0, reuse that code. I think it will be faster and easier to modify if it is your own.
*   I spent too much time trying to understand the fractals. Really I should have just used the given formulas because the math makes no sense.
*   Make sure you understand the flow of data for this assignment. Find out where things need to be called and write it out.
*   Make sure the background color of your output window isn't white, because it's hard to tell if your program is working or frozen.


## Erik's Hints

### Performance

-   Some students struggle because their implementation takes a *very* long time to draw a complete picture
-   Most of the program's time is spent in the `count()` method of the `Fractal` classes
    -   Think about it; this method is called once per pixel, and a picture has thousands or millions of pixels
    -   A 1024 x 1024 picture contains 1,048,576 pixels
    -   Performing arithmetic on complex numbers is one contributing factor to `count()`'s slowness
    -   Keep `count()` as simple as you possibly can, avoiding extraneous calculations
-   Carefully consider each line of code within a loop and ask yourself "does this *really* need to happen inside this loop?"
    -   If it doesn't matter if a line of code is run multiple times, moving it out of the loop can speed things up
-   While you're testing, edit the `.frac` files under `data` and reduce the number of `pixels` and `iterations`
    -   Restore the original values to make a lit wallpaper for your desktop; it'll be worth the wait ;)


### Experimentation

-   Use git branches liberally so you can easily retrace your steps and try
    again.
-   Generate fractal images before and after making sweeping changes so you can
    visually compare the program's output and detect mistakes.


### Generating color palettes

-   Use Python's  `colour`  module.  The `colour.Color` class makes computing a
    color palette from one color to another very easy.
        -   `Color.range_to()` interpolates between two colors.
        -   `Color.get_hex_l()` presents a Color object as a `"#RRGGBB"` string
            which is compatible with `tkinter.PhotoImage`
-   If `import colour` causes this error:
    ```
    ModuleNotFoundError: No module named 'colour'
    ```
    You should install the `colour` package from the command line using this
    command:
    ```
    pip3 install --user colour
    ```
    If that fails, you may need to run this command as an Administrator (esp.
    if you originally installed Python "for all users").
    ```
    pip3 install colour
    ```


### Configuration file format

-   Process this file one line at a time, the same as we've done all semester long
-   Split lines into two pieces on the delimiter
    -   Convert each line to lowercase as you read it
    -   Build up a dictionary one lowercase key at a time
-   Some numeric values must be integers while others are floats
    -   Use `float()` instead of `int()` to make floats from strings
    -   `complex(real, imag)` converts two real numbers into a complex number value


### Image quality

*   More detailed images can be obtained by specifying a large number of
    iterations in the fractal configuration file.
    *   However, the effect is lost when the difference between two adjacent
        colors is slight.
    *   The solution is to interpolate between more than two colors, preferably
        sharply contrasting colors. The color palettes produced from your
        `PaletteFactory` class can be made to interpolate over a list of colors
        of your choosing.


### Abstract classes

*   Python provides a standard library called `abc` (short for *Abstract Base
    Class*) which is widely used to define abstract classes that cannot be
    instantiated.
    *   For our simple needs, `abc` does the exact same thing as constructors
        that raise `NotImplementedError` by employing advanced Python language
        features whose explanations are outside of the scope of this class.
*   I'm not saying that `abc` is bad or that you shouldn't ever use it; I am
    saying that I do not encourage you to use `abc` for this assignment because
    it adds complexity without benefit.  This assignment is complex enough
    already.
*   Relying on a module that you do not understand is a hallmark of *cargo cult
    programming*.  If you insist on using `abc` anyway, you are on your own
    when you run into problems.
