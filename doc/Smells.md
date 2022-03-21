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


### Example Code Smell Documentation *(Delete this example from your final report)*:

0.  `src/mbrot_fractal.py`, [lines 142-163 (roughly towards the bottom)]
        * [What kind of code smell is this?] This is **dead code**
        * [Why is the smell a problem?] This is a variation of `colorOfThePixel()` that purportedly doesn't work.  There is already a version that does work, so this copy can safely be deleted.  In the unlikely event that I ever want to see it again, I can find it again with the `git log --patch` command. This function also has globals and confusing comments.
    *   Code Snippet:
        ```python
        def colorOfThePixel(c, colors):
        """Return the color of the current pixel within the Mandelbrot set"""
        global z
        global MAX_ITERATIONS
        global mainWindowObject
        z0 = complex(0, 0)  # z0

        for iter in range(MAX_ITERATIONS + 1):
            z0 = z0 * z0 + c
            # if the absolute value of z is less than TWO
            # if abs(z) > TWO:
            if abs(z) > 2.0:
                if z == float(2.0):
                    return colors[iter-1]
                elif abs(z) < z:
                    if abs(z) > TWO:
                        return colors[iter]
                    else:
                        return colors[iter+0]
                else:
                    return colors[iter+1]
        return colors[MAX_ITERATIONS]
        ```
    *   How the code smell was fixed:
        *   [Explain what you changed]] I deleted the unneccessary code.
1.  [Repeat for the next code smell]


## Code Smells

*TODO: Write your report here*
