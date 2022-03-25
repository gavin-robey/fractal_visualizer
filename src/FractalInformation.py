'''
This module contains all the needed information for each fractal
This module consists of only one dictionary containing all the values used.
There are 12 keys each containing necessary values.
Each of the 12 keys contains another dictionary that holds 3 keys each.
These keys are 'centerX', 'centerY', and 'axisLen'
'''
fractals = {
    'fulljulia': {
        'centerX':  0.0,
        'centerY':  0.0,
        'axisLen':  4.0,
    },
    'hourglass': {
        'centerX':  0.618,
        'centerY':  0.00,
        'axisLen':  0.017148277367054,
    },
    'lakes': {
        'centerX': -0.339230468501458,
        'centerY': 0.417970758224314,
        'axisLen': 0.164938488846612,
    },
    'lace-curtains': {
        'centerX': -1.01537721564149,
        'centerY': 0.249425427273733,
        'axisLen': 0.0121221433855615,
    },
    'mandelbrot': {
        'centerX': -0.6,
        'centerY': 0.0,
        'axisLen': 2.5,
    },
    'mandelbrot-zoomed': {
        'centerX': -1.0,
        'centerY': 0.0,
        'axisLen': 1.0,
    },
    'spiral0': {
        'centerX': -0.761335372924805,
        'centerY': 0.0835704803466797,
        'axisLen': 0.004978179931102462,
    },
    'spiral1': {
        'centerX': -0.747,
        'centerY': 0.1075,
        'axisLen': 0.002,
    },
    'seahorse': {
        'centerX': -0.745,
        'centerY': 0.105,
        'axisLen': 0.01,
    },
    'elephants': {
        'centerX': 0.30820836067024604,
        'centerY': 0.030620936230004017,
        'axisLen': 0.03,
    },
    'leaf': {
        'centerX': -1.543577002,
        'centerY': -0.000058690069,
        'axisLen': 0.000051248888,
    },
    'starfish': {
        'centerX': -0.463595023481762,
        'centerY': 0.598380871135558,
        'axisLen': 0.00128413675654471,
    }
}