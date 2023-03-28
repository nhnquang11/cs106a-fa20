from simpleimage import SimpleImage

FONT_FILE = 'impact.ttf'
SIZE = 50
COLOR = 'white'

class MemeGenerator:

    def __init__(self, filename):
        self.image = SimpleImage(filename)

    def set_image(self, filename):
        self.image = SimpleImage(filename)

    def add_text(self, text, x, y):
        self.image.create_text(text, x, y, "Courier", size=30, color='white')

    def render(self):
        self.image.show()