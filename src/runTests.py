import unittest
from Testing import TestFractalFactory, TestPaletteFactory


suite = unittest.TestSuite()  	         	  
tests = (TestPaletteFactory.TestPaletteFactory, TestFractalFactory.TestFractalFactory)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)  	         	  
runner.run(suite)  	         	  
