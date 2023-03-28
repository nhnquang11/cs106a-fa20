"""
File: img_ascii.py
------------------

Converts the image to ASCII characters.
"""
from simpleimage import SimpleImage

FILENAME = 'brahm.jpg'
IMG_CHARS = '▓▒░ '
BREAKPOINTS = (64, 128, 192)


def convert_img_to_ascii(img_file):
    """
    Converts an image to ASCII characters stored in IMG_CHARS based on the
    brightness breakpoints in BREAKPOINTS and prints out the resulting ascii.
    """
    image = SimpleImage(img_file)
    resize_img_for_ascii(image)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            print(convert_pixel_to_ascii(pixel), end='')
        print()

def convert_pixel_to_ascii(pixel):
    avg = (pixel.red + pixel.green + pixel.blue) / 3
    if avg < BREAKPOINTS[0]:
        return IMG_CHARS[0]
    elif BREAKPOINTS[0] <= avg <= BREAKPOINTS[1]:
        return IMG_CHARS[1]
    elif BREAKPOINTS[1] <= avg <= BREAKPOINTS[2]:
        return IMG_CHARS[2]
    return IMG_CHARS[-1]

def main():
    convert_img_to_ascii(FILENAME)


def resize_img_for_ascii(img):
    """
    PROVIDED FUNCTION: Resize an image to account for the fact that the ASCII
    characters are taller than they are wide, so that the resulting ASCII looks
    proportionally correct.

    Arguments
    ---------
    img (simpleimage.SimpleImage) -- The image to resize.
    """
    # Stretch the width of the image by a factor of two
    width = img.width * 2.3
    height = img.height

    # Scale so the width is 150px
    scale_factor = 70 / width
    width = round(scale_factor * width)
    height = round(scale_factor * height)

    # Resize the underlying PIL image.
    img.pil_image = img.pil_image.resize((width, height))
    img.px = img.pil_image.load()
    size = img.pil_image.size
    img._width = size[0]
    img._height = size[1]


if __name__ == '__main__':
    main()