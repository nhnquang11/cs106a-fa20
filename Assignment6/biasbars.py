"""
File: biasbars.py
---------------------
This program plots the frequency of words from reviews of two genders. 
The historical dataset consists of nearly 20 years of reviews of college 
and university professors posted on RateMyProfessors.com. 
This data visualization application helps investigate and 
reason about how humans use language in gendered ways.
"""

import tkinter
import biasbarsdata
import biasbarsgui as gui


# Provided constants to load and plot the word frequency data
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

FILENAME = "data/full-data.txt"

VERTICAL_MARGIN = 30
LEFT_MARGIN = 60
RIGHT_MARGIN = 30
LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]
LABEL_OFFSET = 10
BAR_WIDTH = 75
LINE_WIDTH = 2
TEXT_DX = 2
NUM_VERTICAL_DIVISIONS = 7
TICK_WIDTH = 15
BAR_WOMEN_COLOR = 'dodgerblue'
BAR_MEN_COLOR = 'orange'

def get_centered_x_coordinate(width, idx):
    """
    Given the width of the canvas and the index of the current review
    quality bucket to plot, returns the x coordinate of the centered
    location for the bars and label to be plotted relative to.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current label in the LABELS list
    Returns:
        x_coordinate (float): The centered x coordinate of the horizontal line 
                              associated with the specified label.
    >>> round(get_centered_x_coordinate(1000, 0), 1)
    211.7
    >>> round(get_centered_x_coordinate(1000, 1), 1)
    515.0
    >>> round(get_centered_x_coordinate(1000, 2), 1)
    818.3
    """
    # splits the frame into n equal segments where n is the number of labels
    segment_width = (width - LEFT_MARGIN - RIGHT_MARGIN) / len(LABELS)

    return LEFT_MARGIN + segment_width * (idx + 0.5) 


def draw_fixed_content(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background border and x-axis labels on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing content from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas
    
    # draw frame to display bars
    canvas.create_rectangle(
            LEFT_MARGIN,
            VERTICAL_MARGIN, 
            width - RIGHT_MARGIN, 
            height - VERTICAL_MARGIN,
            width=LINE_WIDTH
        )

    # draw labels under the bottom of the frame
    for i in range(len(LABELS)):
        canvas.create_text(
            get_centered_x_coordinate(width, i),
            height - VERTICAL_MARGIN + LABEL_OFFSET,
            anchor='c',
            text=LABELS[i]
        )

def plot_word(canvas, word_data, word):
    """
    Given a dictionary of word frequency data and a single word, plots
    the distribution of the frequency of this word across gender and 
    rating category.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        word_data (dictionary): Dictionary holding word frequency data
        word (str): The word whose frequency distribution you want to plot
    """

    draw_fixed_content(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # We have provided code to calculate the maximum frequency for the specified
    # word from the provided dict 
    gender_data = word_data[word]
    max_frequency = max(max(gender_data[biasbarsdata.KEY_WOMEN]), max(gender_data[biasbarsdata.KEY_MEN]))

    # Draw ticks on the left side of the frame.
    plot_ticks(canvas)

    # Add labels representing frequency on the left side of the ticks.
    plot_labels(canvas, max_frequency)

    plot_bars(canvas, gender_data, max_frequency)

def plot_bars(canvas, gender_data, max_frequency):
    """
    Given the data of frequency, plot bars chart for both genders.
    """
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    frame_height = height - 2 * VERTICAL_MARGIN
    for i in range(len(LABELS)):
        for gender in gender_data:
            y0 = height - VERTICAL_MARGIN
            y1 = y0 - gender_data[gender][i] / max_frequency * frame_height 
            if gender == biasbarsdata.KEY_WOMEN:
                x0 = get_centered_x_coordinate(width, i) - BAR_WIDTH
                x1 = x0 + BAR_WIDTH
                canvas.create_rectangle(x0, y0, x1, y1, fill=BAR_WOMEN_COLOR)
            elif gender == biasbarsdata.KEY_MEN:
                x0 = get_centered_x_coordinate(width, i)
                x1 = x0 + BAR_WIDTH
                canvas.create_rectangle(x0, y0, x1, y1, fill=BAR_MEN_COLOR)
            canvas.create_text(x0 + TEXT_DX, y1, text=gender, anchor=tkinter.NW)

def plot_labels(canvas, max_frequency):
    """
    # Adds labels representing frequency on the left side of the ticks.
    """
    height = canvas.winfo_height()
    part = max_frequency / NUM_VERTICAL_DIVISIONS
    for i in range(NUM_VERTICAL_DIVISIONS + 1):
        freq = round(max_frequency - i * part)
        x = LEFT_MARGIN - LABEL_OFFSET
        y = VERTICAL_MARGIN + i * (height - 2 * VERTICAL_MARGIN) / NUM_VERTICAL_DIVISIONS
        canvas.create_text(x, y, text=freq, anchor=tkinter.E)

def plot_ticks(canvas):
    """
    Draws tick marks on the left side of the frame.
    """
    height = canvas.winfo_height()
    for i in range(NUM_VERTICAL_DIVISIONS + 1):
        x0 = LEFT_MARGIN - TICK_WIDTH / 2
        y0 = VERTICAL_MARGIN + i * (height - 2 * VERTICAL_MARGIN) / NUM_VERTICAL_DIVISIONS
        x1 = LEFT_MARGIN + TICK_WIDTH / 2
        y1 = y0
        canvas.create_line(x0, y0, x1, y1, width=LINE_WIDTH)
        

def convert_counts_to_frequencies(word_data):
    """
    This code is provided to you! 

    It converts a dictionary 
    of word counts into a dictionary of word frequencies by 
    dividing each count for a given gender by the total number 
    of words found in reviews about professors of that gender.
    """ 
    K = 1000000
    total_words_men = sum([sum(counts[biasbarsdata.KEY_MEN]) for word, counts in word_data.items()])
    total_words_women = sum([sum(counts[biasbarsdata.KEY_WOMEN]) for word, counts in word_data.items()])
    for word in word_data:
        gender_data = word_data[word]
        for i in range(3):
            gender_data[biasbarsdata.KEY_MEN][i] *= K / total_words_men
            gender_data[biasbarsdata.KEY_WOMEN][i] *= K / total_words_women


# main() code is provided for you
def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    # Load data
    word_data = biasbarsdata.read_file(FILENAME)
    convert_counts_to_frequencies(word_data)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Bias Bars')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, word_data, plot_word, biasbarsdata.search_words)

    # draw_fixed once at startup so we have the borders and labels
    # even before the user types anything.
    draw_fixed_content(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()