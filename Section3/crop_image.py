from simpleimage import SimpleImage

PIXELS_TO_CROP = 30


def crop_image(filename, n):
    """
    crops the image to fit inside of a frame by shaving 
    n pixels from each side of the image. 

    You may assume that n is less than half the width of 
    the image. 
    """
    image = SimpleImage(filename)
    crop = SimpleImage.blank(width=image.width-2*PIXELS_TO_CROP, height=image.height-2*PIXELS_TO_CROP)

    for y in range(crop.height):
        for x in range(crop.width):
            crop.set_pixel(x, y, image.get_pixel(x + PIXELS_TO_CROP, y + PIXELS_TO_CROP))

    crop.show()

def main():
    crop_image('karel.png', PIXELS_TO_CROP)


if __name__ == "__main__":
    main()
