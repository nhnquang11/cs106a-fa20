from simpleimage import SimpleImage


SQUEEZE_FACTOR = 4


def squeeze_width(filename, n):
    """
    A funhouse mirror effect governed by the int parameter n. 
    Create a new image with the same height as the original, but
    with a width that is n times smaller than the original's. 
    Copy the original image such that it is squeezed horizontally.

    For example, if n = 4, the pixels in the output image with an 
    x coordinate of 0 would be copies of the input pixels with
    an x coordinate of 0 * 4 = 0, while pixels in the output 
    image with an x coordinate of 1 would be copies of the input
    pixels with an x coordinate of 1 * 4 = 4, and so on.
    """
    image = SimpleImage(filename)
    squeezed = SimpleImage.blank(width=image.width//n, height=image.height)

    for y in range(squeezed.height):
        for x in range(squeezed.width):
            squeezed.set_pixel(x, y, image.get_pixel(x*n, y))

    squeezed.show()

def main():
    squeeze_width('karel.png', SQUEEZE_FACTOR)

if __name__ == "__main__":
    main()
