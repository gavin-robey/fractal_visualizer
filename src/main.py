#!/usr/bin/env python3  	         	  

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

import sys  	         	  

import julia_fractal as julia  	         	  
import mbrot_fractal  	         	  


JULIAS = [ 'fulljulia', 'hourglass', 'lace-curtains', 'lakes' ]  	         	  
MBROTS = [ 'elephants', 'leaf', 'mandelbrot', 'mandelbrot-zoomed', 'seahorse', 'spiral0', 'spiral1', 'starfish' ]  	         	  

# quit when too many arguments are given  	         	  
if len(sys.argv) < 2:  	         	  
    print("Please provide the name of a fractal as an argument")  	         	  
    for i in JULIAS + MBROTS:  	         	  
        print(f"\t{i}")  	         	  
    sys.exit(1)  	         	  

# quite when one of the arguments isn't in the command line  	         	  
elif sys.argv[1] not in JULIAS + MBROTS:  	         	  
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")  	         	  
    print("Please choose one of the following:")  	         	  
    all_of_the_fractals = JULIAS  	         	  
    all_of_the_fractals.extend(MBROTS)  	         	  
    for i in all_of_the_fractals:  	         	  
        print(f"\t{i}")  	         	  
    sys.exit(1)  	         	  

# Otherwise, quit with an error message to help the user learn how to run it  	         	  
else:  	         	  
    # fractal is the 1st argument after the program name  	         	  
    fracal = sys.argv[1]  	         	  
    if sys.argv[1] in JULIAS:  	         	  
        julia.julia_main(sys.argv[1])  	         	  
    elif sys.argv[1] in MBROTS:  	         	  
        fratcal = sys.argv[1]  	         	  
        mbrot_fractal.mbrot_main(fratcal)  	         	  

