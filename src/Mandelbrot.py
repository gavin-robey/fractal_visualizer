def getCount(c, paletteLength):
    '''
    This function returns: Integer
    This function has 2 arguments:
    c: Complex
    paletteLength: Integer
    This function loops through the length of the color palette and depending on some magic from the Mandelbrot algorithm
    it returns the number of iterations
    Changes from original plan:
    added a second return statement to return the full count - 1 (This is because we need to use it as an index)
    '''
    count = 0
    z = complex(0, 0)
    for i in range(paletteLength):
        z = z * z + c
        if abs(z) > 2:
            count += i
            return count
    return count - 1


def testPixelAmount(row, col):
    '''
    Returns the amount of pixels created depending on how many columns or rows there are
    '''
    pixels = row * col
    return pixels