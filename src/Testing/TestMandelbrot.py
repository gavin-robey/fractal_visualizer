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

import unittest
from Palette import Palette
import Julia, Mandelbrot
from FractalInformation import fractals


# autocmd BufWritePost <buffer> !python3 runTests.py  	         	  

class TestMandelbrot(unittest.TestCase):  	         	  
    def test_colorOfThePixel(self):  	         	  
        self.assertEqual(Palette("mbrot", complex(0, 0), Julia, Mandelbrot).getPixelColor(), '#e8283f')
        self.assertEqual(Palette("mbrot", complex(-0.751, 1.1075),Julia, Mandelbrot).getPixelColor(), '#baf12e')
        self.assertEqual(Palette("mbrot", complex(-0.2, 1.1075), Julia, Mandelbrot).getPixelColor(), '#e0ceaf')
        self.assertEqual(Palette("mbrot", complex(-0.75, 0.1075),Julia, Mandelbrot).getPixelColor(), '#f1da2e')
        self.assertEqual(Palette("mbrot", complex(-0.748, 0.1075), Julia, Mandelbrot).getPixelColor(), '#deb69f')
        self.assertEqual(Palette("mbrot", complex(-0.7562500000000001, 0.078125), Julia, Mandelbrot).getPixelColor(), '#e1bc7e')
        self.assertEqual(Palette("mbrot", complex(-0.7562500000000001, -0.234375), Julia, Mandelbrot).getPixelColor(), '#e7ddd7')
        self.assertEqual(Palette("mbrot", complex(0.3374999999999999, -0.625), Julia, Mandelbrot).getPixelColor(), '#e1d1bd')
        self.assertEqual(Palette("mbrot", complex(-0.6781250000000001, -0.46875), Julia, Mandelbrot).getPixelColor(), '#eccd43')
        self.assertEqual(Palette("mbrot", complex(0.4937499999999999, -0.234375), Julia, Mandelbrot).getPixelColor(), '#d9e758')
        self.assertEqual(Palette("mbrot", complex(0.3374999999999999, 0.546875), Julia, Mandelbrot).getPixelColor(), '#e1cbbd')

    def test_palleteLength(self):
        self.assertEqual(111, len(Palette("mbrot", complex(0, 0), Julia, Mandelbrot)))

    def testNumOfFractals(self):
        self.assertEqual(len(fractals), 12)

    def testPixelAmount(self):
        self.assertEqual(Mandelbrot.testPixelAmount(7, 7), 49)
        self.assertEqual(Mandelbrot.testPixelAmount(257, 321), 82497)
        self.assertEqual(Mandelbrot.testPixelAmount(256, 256), 65536)
        self.assertEqual(Mandelbrot.testPixelAmount(100, 100), 10000)
        self.assertEqual(Mandelbrot.testPixelAmount(640, 480), 307200)


if __name__ == '__main__':  	         	  
    unittest.main()  	         	  
