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

class TestJulia(unittest.TestCase):

    def test_colorOfThePixel(self):  	         	  
        self.assertEqual(Palette("julia", complex(0, 0), Julia, Mandelbrot).getPixelColor(), '#009cb3')
        self.assertEqual(Palette("julia", complex(-0.751, 1.1075), Julia, Mandelbrot).getPixelColor(), '#ffe4b5')
        self.assertEqual(Palette("julia", complex(-0.2, 1.1075), Julia, Mandelbrot).getPixelColor(), '#ffe4b5')
        self.assertEqual(Palette("julia", complex(-0.75, 0.1075), Julia, Mandelbrot).getPixelColor(), '#009cb3')
        self.assertEqual(Palette("julia", complex(-0.748, 0.1075), Julia, Mandelbrot).getPixelColor(), '#009cb3')
        self.assertEqual(Palette("julia", complex(-0.7562500000000001, 0.078125), Julia, Mandelbrot).getPixelColor(), '#009cb3')
        self.assertEqual(Palette("julia", complex(-0.7562500000000001, -0.234375), Julia, Mandelbrot).getPixelColor(), '#ffeda4')
        self.assertEqual(Palette("julia", complex(0.3374999999999999, -0.625), Julia, Mandelbrot).getPixelColor(), '#ffe7ae')
        self.assertEqual(Palette("julia", complex(-0.6781250000000001, -0.46875), Julia, Mandelbrot).getPixelColor(), '#ffe7ae')
        self.assertEqual(Palette("julia", complex(0.4937499999999999, -0.234375), Julia, Mandelbrot).getPixelColor(), '#fff797')
        self.assertEqual(Palette("julia", complex(0.3374999999999999, 0.546875), Julia, Mandelbrot).getPixelColor(), '#ffe9ab')

    def testAxisLength(self):
        self.assertEqual(fractals["fulljulia"]["axisLen"], 4.0)
        self.assertEqual(fractals["hourglass"]["axisLen"], 0.017148277367054)
        self.assertEqual(fractals["lakes"]["axisLen"], 0.164938488846612)
        self.assertEqual(fractals["lace-curtains"]["axisLen"], 0.0121221433855615)
        self.assertEqual(fractals["mandelbrot"]["axisLen"], 2.5)
        self.assertEqual(fractals["mandelbrot-zoomed"]["axisLen"], 1.0)
        self.assertEqual(fractals["spiral0"]["axisLen"], 0.004978179931102462)
        self.assertEqual(fractals["spiral1"]["axisLen"], 0.002)
        self.assertEqual(fractals["seahorse"]["axisLen"], 0.01)
        self.assertEqual(fractals["elephants"]["axisLen"], 0.03)
        self.assertEqual(fractals["leaf"]["axisLen"], 0.000051248888)
        self.assertEqual(fractals["starfish"]["axisLen"], 0.00128413675654471)

    def testPixelAmount(self):
        self.assertEqual(Julia.testPixelAmount(7, 7), 49)
        self.assertEqual(Julia.testPixelAmount(257, 321), 82497)
        self.assertEqual(Julia.testPixelAmount(256, 256), 65536)
        self.assertEqual(Julia.testPixelAmount(100, 100), 10000)
        self.assertEqual(Julia.testPixelAmount(640, 480), 307200)

    def test_palleteLength(self):
        self.assertEqual(78, len(Palette("julia", complex(0, 0), Julia, Mandelbrot)))

    def testNumOfFractals(self):
        self.assertEqual(len(fractals), 12)


if __name__ == '__main__':  	         	  
    unittest.main()  	         	  
