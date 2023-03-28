"""
File: warhol.py
---------------
This program takes in a picture and 
generates a Warhol-style version of it.
"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage
from random import choice

# Name of file that we will use to create the warhol image
IMAGE_FILE = 'images/simba.jpg'

RANDOM_SCALE = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
WIDTH_REP = 10
HEIGHT_REP = 10

def create_filtered_image(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol program. It creates an
    image object from the image in the file IMAGE_FILE, and then recolors the image
    object.  The parameters to this function are:
      red_scale: A number to multiply each pixels' red component by
      green_scale: A number to multiply each pixels' green component by
      blue_scale: A number to multiply each pixels' blue component by
    This function should return a newly generated image with the appropriately
    scaled color values of the pixels.
    """
    image = SimpleImage(IMAGE_FILE)

    for pixel in image:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale

    return image

def make_warhol():
    """
    This function generates a Warhol-style picture based on the original image in the
    file IMAGE_FILE.  The Warhol image contains "patches" that are different colored
    versions of the original image.  This function returns the Warhol image.
    """
    image = SimpleImage(IMAGE_FILE)
    warhol = SimpleImage.blank(width=image.width*WIDTH_REP, height=image.height*HEIGHT_REP)

    # traverse through each part in the warhol image
    # create a new filtered image and 
    # copy it into each part of the warhol image
    for row in range(HEIGHT_REP):
        for col in range(WIDTH_REP):
            # randomly pick a scale for each channel
            red_scale = choice(RANDOM_SCALE)
            green_scale = choice(RANDOM_SCALE)
            blue_scale = choice(RANDOM_SCALE)

            # create a filtered image
            filtered_image = create_filtered_image(red_scale, green_scale, blue_scale)

            # copy each pixel of a filtered image into the warhol-style version
            for y in range(filtered_image.height):
                for x in range(filtered_image.width):
                    pixel = filtered_image.get_pixel(x, y)
                    warhol.set_pixel(x+col*filtered_image.width, y+row*filtered_image.height, pixel)

    return warhol
    


def main():
    """
    This program tests your create_filtered_image and make_warhol functions by calling
    those functions and displaying the resulting images.  Feel free to modify this code
    when you are writing your program.  For example, the call to the create_filtered_image
    function is provided to test that function by itself.  Feel free to delete that portion
    of the code when you have the create_filtered_image working, and then just focus on
    the make_warhol function.
    """
    single_patch = create_filtered_image(1.5, 0, 1.5)
    if single_patch != None:
        single_patch.show()

    warhol_image = make_warhol()
    if warhol_image != None:
        warhol_image.show()


if __name__ == '__main__':
    main()
