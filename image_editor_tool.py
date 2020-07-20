from PIL import Image
from pathlib import *
import sys
import colorama
import termcolor
from PIL import ImageFilter
from Classes import *
import argparse

colorama.init()

parser = argparse.ArgumentParser(description='Media Powerful Tool')
parser.add_argument('-f', action = 'store', dest = "filter", default = None,
                    help = 'Available filter names: BLUR CONTOUR DETAIL EDGE_ENHANCE  EDGE_ENHANCE_MORE EMBOSS FIND_EDGES SHARPEN SMOOTH SMOOTH_MORE')
parser.add_argument('-s', action = 'store', dest = 'res_filename', default = None, help = "Results filename")
parser.add_argument('-c', action = 'store', dest = 'crop', default = None, help = "crop percentage")
parser.add_argument("-a",action = 'store', dest = "angle", default = None, help = "rotationing angle")
parser.add_argument('input_filename', action = 'store', help = 'Image file to work with')


def main():
    args = parser.parse_args()
    print(args)



def check_correct_file(args):
    """Try to open file.If it exists, it will return the PIL picture, otherwise False """
    try:
        im = Image.open(args.input_filename)
    except PIL.UnidentifiedImageError as e:
        print(termcolor.colored("Fatal error while opening " , args.input_filename), "red")
        return False





if __name__ == '__main__':
    main()

