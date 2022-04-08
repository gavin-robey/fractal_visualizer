import unittest
from PaletteFactory import PaletteFactory


class TestPaletteFactory(unittest.TestCase):


    def testLengthOfPaletteGold(self):
        self.assertGreaterEqual(PaletteFactory().makePalette(11).getLength(), 11)
        self.assertGreaterEqual(PaletteFactory().makePalette(20).getLength(), 20)
        self.assertGreaterEqual(PaletteFactory().makePalette(64).getLength(), 64)
        self.assertGreaterEqual(PaletteFactory().makePalette(220).getLength(), 220)
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getLength(), 512)
        self.assertGreaterEqual(PaletteFactory().makePalette(750).getLength(), 750)
        self.assertGreaterEqual(PaletteFactory().makePalette(900).getLength(), 900)
        self.assertGreaterEqual(PaletteFactory().makePalette(1000).getLength(), 1000)

    def testLengthOfPaletteRainbow(self):
        self.assertGreaterEqual(PaletteFactory().makePalette(11, "rainbow").getLength(), 11)
        self.assertGreaterEqual(PaletteFactory().makePalette(20, "rainbow").getLength(), 20)
        self.assertGreaterEqual(PaletteFactory().makePalette(64, "rainbow").getLength(), 64)
        self.assertGreaterEqual(PaletteFactory().makePalette(220, "rainbow").getLength(), 220)
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getLength(), 512)
        self.assertGreaterEqual(PaletteFactory().makePalette(750, "rainbow").getLength(), 750)
        self.assertGreaterEqual(PaletteFactory().makePalette(900, "rainbow").getLength(), 900)
        self.assertGreaterEqual(PaletteFactory().makePalette(1000, "rainbow").getLength(), 1000)

    def testColorOfPaletteGold(self):
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getColor(0), "#000000")
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getColor(2), "#0a0909")
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getColor(6), "#201918")
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getColor(10), "#392725")
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getColor(50), "#fcdba7")
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getColor(120), "#383838")
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getColor(250), "#37371c")
        self.assertGreaterEqual(PaletteFactory().makePalette(512).getColor(512), "#0c0b0a")

    def testColorOfPaletteRainbow(self):
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getColor(0), "#ffffff")
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getColor(2), "#f7f7f7")
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getColor(6), "#e8e7e5")
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getColor(10), "#dad9d3")
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getColor(50), "#282d69")
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getColor(120), "#383838")
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getColor(250), "#37371c")
        self.assertGreaterEqual(PaletteFactory().makePalette(512, "rainbow").getColor(512), "#0c0b0a")