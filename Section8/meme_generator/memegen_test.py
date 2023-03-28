# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('one-does-not.png')

    # add text to the top and bottom of the meme
    meme_gen.add_text('ONE DOES NOT SIMPLY', 60, 5)
    meme_gen.add_text('MAKE A MEME GENERATOR IN PYTHON', 10, 220)

    # generate the meme!
    meme_gen.render()

if __name__ == '__main__':
    main()
