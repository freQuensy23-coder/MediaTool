from PIL import Image
from pathlib import *
import sys
import colorama
import termcolor
from PIL import ImageFilter
from Classes import *
import argparse


parser = argparse.ArgumentParser(description='Media Powerful Tool')
parser.add_argument('-filter', action = 'store', dest = "filter", default = None,
                    help = 'Available filter names: BLUR CONTOUR DETAIL EDGE_ENHANCE  EDGE_ENHANCE_MORE EMBOSS FIND_EDGES SHARPEN SMOOTH SMOOTH_MORE')
parser.add_argument('-s', action = 'store', dest = 'res_filename', default = None)
parser.add_argument('-crop', action = 'store', dest = 'crop', default = None)
parser.add_argument("-a",action = 'store', dest = "angle", default = None)
parser.add_argument('input_filename', action = 'store', help = 'Image file to work with')


def main():
    args = parser.parse_args()
    print(args)
    if

if __name__ == '__main__':
    main()

