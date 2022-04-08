import unittest
from FractalFactory import FractalFactory
from FractalParser import FractalParser


class TestFractalFactory(unittest.TestCase):

    def testJuliaCount(self):
        juliaConfiguration = {
            "type": "julia",
            "creal": -1.0,
            "cimag": 0.0,
            "pixels": 1024,
            "centerx": 0.0,
            "centery": 0.0,
            "axislength": 4.0,
            "iterations": 78,
        }

        self.assertEqual(FractalFactory().makeFractal(juliaConfiguration).count(complex(1, 2)), 0)
        self.assertEqual(FractalFactory().makeFractal(juliaConfiguration).count(complex(-1, 0.0002)), -1)
        self.assertEqual(FractalFactory().makeFractal(juliaConfiguration).count(complex(-5.45, 0.01)), 0)
        self.assertEqual(FractalFactory().makeFractal(juliaConfiguration).count(complex(0.004, 0.01)), -1)

    def testMandelbrotCount(self):
        self.assertEqual(FractalFactory().makeFractal().count(complex(1, 2)), 0)
        self.assertEqual(FractalFactory().makeFractal().count(complex(-1, 0.0002)), -1)
        self.assertEqual(FractalFactory().makeFractal().count(complex(-5.45, 0.01)), 0)
        self.assertEqual(FractalFactory().makeFractal().count(complex(0.004, 0.01)), -1)

    def testFractalParser(self):
        with self.assertRaises(RuntimeError):
            FractalParser("data/invalid.frac").getConfiguration()
