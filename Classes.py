from PIL import Image
from pathlib import *
import sys
import colorama
import termcolor
from PIL import ImageFilter



class Photo:
    def __init__(self, path):
        self.path = path
        self.image = Image.open(path)

    def rotate_image(self, angle):
        """Rotate image to some angle (in degrees)"""
        self.image = self.image.rotate(angle)

    def crop(self, x0, y0, x1, y1):
        """x0, y0 - coordinates of left corner, x1, y1 of the right"""
        img = self.image
        width0 = img.size[0]
        height0 = img.size[1]
        img = img.crop((x0, y0, x1 - x0, y1 - y0))
        self.image = img

    def crop_image_by_percent(self, percent):
        """Using this you can crop image by percent (in absolute value 50% = 0.5) (0 - not cropped, 1 - one pixel)"""
        img = self.image
        width0 = img.size[0]
        height0 = img.size[1]
        delta_width = width0 * percent / 2
        delta_height = height0 * percent / 2
        self.crop(delta_width, delta_height, width0 - delta_width, height0 - delta_height)

    def apply_filter(self, filter):
        """Filter image """
        self.image = self.image.filter(filter)

    def show(self):
        """Show image in default OS image viewer"""
        self.image.show()

    def save(self, file_name):
        """Save image to the same folder with filename"""
        self.image.save(file_name + ".jpeg")


class Folder:
    def __init__(self, path):
        self.path = path
        self.files = self.get_folder_files()


    def get_folder_files(self):
        """Returns all files (and folders) in this folder"""
        p = Path(self.path).glob('**/*')
        files = [x for x in p if x.is_file()]
        return files


def get_file_extension(file):
    """Returns file extension"""
    return file.suffixes[-1]