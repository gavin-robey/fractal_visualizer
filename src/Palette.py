import Julia
import Mandelbrot


class Palette:
    def __init__(self, fractalType, coordinate):
        '''
        This class returns String, more specifically a string representing a color.
        In order to access the color found, call the getPixelColor method
        This class has 2 arguments:
        fractalType: String
        coordinate: Complex number
        This class has 4 data members:
        fractalType: String: representing the type of the fractal
        coordinate: Complex: representing the coordinate of the real and imaginary number
        mbrotPalette: List of Strings: Representing the color palette for the mandelbrot algorithm
        juliaPalette: List of Strings: Representing the color palette for the julia algorithm
        This class returns the color of the current pixel by finding the index of the specific color palette given
        by either the Mandelbrot module or the Julia module.
        '''
        self.__fractalType = fractalType
        self.__coordinate = coordinate
        self.__mbrotPalette = [
        '#89ff00', '#a4f817', '#baf12e', '#ccec43', '#d9e758', '#e3e46b', '#e1d97e',
        '#e0d18f', '#dfce9f', '#e0ceaf', '#e1d1bd', '#e4d6cb', '#e7ddd7', '#ece5e3',
        '#f1eeed', '#f8f7f7', '#ffffff', '#f8f7f7', '#f1eeed', '#ece4e3', '#e7dbd7',
        '#e4d3cb', '#e1cbbd', '#e0c4af', '#dfbf9f', '#e0bd8f', '#e1bc7e', '#e4bf6b',
        '#e7c458', '#eccd43', '#f1da2e', '#f8eb17', '#fdff00', '#f8eb17', '#f1da2e',
        '#eccd43', '#e7c458', '#e4bf6b', '#e1bc7e', '#e0bd8f', '#dfbf9f', '#e0c4af',
        '#e1cbbd', '#e4d3cb', '#e7dbd7', '#ece4e3', '#f1eeed', '#f8f7f7', '#ffffff',
        '#f7f6f6', '#f1eded', '#ebe4e2', '#e6dad7', '#e3d0ca', '#e0c6bd', '#debeae',
        '#deb69f', '#deaf8e', '#dfaa7d', '#e1a66b', '#e4a557', '#e9a643', '#eea92e',
        '#f4af17', '#f7b604', '#f4af17', '#eea92e', '#e9a643', '#e4a557', '#e1a66b',
        '#dfaa7d', '#deaf8e', '#deb69f', '#debeae', '#e0c6bd', '#e3d0ca', '#e6dad7',
        '#ebe4e2', '#f1eded', '#f7f6f6', '#ffffff', '#f8f7f7', '#f2f1ef', '#ebece5',
        '#e2e7db', '#d3e3d0', '#c5e0ca', '#b9ddce', '#abdbd9', '#9ec8da', '#8fa7da',
        '#8480db', '#9c70dc', '#c25fde', '#e04dcb', '#e43b8d', '#ffffff', '#f7f6f6',
        '#f0efec', '#e8eae1', '#dae5d5', '#c8e1cb', '#badecd', '#abdbd9', '#9cc4da',
        '#8b9cda', '#8d79db', '#b066dd', '#e052da', '#e33e97', '#e8283f',
        ]
        self.__juliaPalette = [
        '#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',
        '#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',
        '#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',
        '#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',
        '#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',
        '#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',
        '#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',
        '#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',
        '#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',
        '#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',
        '#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',
        '#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',
        '#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',
        '#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',
        '#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',
        '#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277',
        ]

    def getPixelColor(self):
        '''
        This method returns: String
        This method has no arguments
        This method checks which type of fractal is being called
        Then it returns a color from the proper color palette by using the index returned by either the Julia or Mandelbrot
        modules.
        '''
        if self.__fractalType == 'julia':
            return self.__juliaPalette[Julia.getCount(self.__coordinate, len(self.__juliaPalette))]
        elif self.__fractalType == 'mbrot':
            return self.__mbrotPalette[Mandelbrot.getCount(self.__coordinate, len(self.__mbrotPalette))]