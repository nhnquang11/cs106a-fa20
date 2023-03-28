from simpleimage import SimpleImage

def double_left(filename):
    """
    Takes the left half of image, and copies it on top of the right half.
    """
    image = SimpleImage(filename)
    middle_width = image.width // 2
    for y in range(image.height):
        for x in range(middle_width):
            pixel = image.get_pixel(x, y)
            image.set_pixel(x + middle_width, y, pixel)
    image.show()

def main():
    double_left('karel.png')


if __name__ == "__main__":
    main()
