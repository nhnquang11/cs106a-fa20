from graphics import Canvas
import tkinter as tk

CANVAS_WIDTH = 720
CANVAS_HEIGHT = 720

DOT_COLOR = "red"
DOT_RADIUS = 10
TEXT_COLOR = "black"
FRIENDS_FILE = 'users.txt'
COORDINATES_FILE = 'coords.txt'

def draw_friend_graph(canvas, friends_file, coordinates_file):
    """
    Draws a graph representing the friend network. For each user, 
    draw a circle at their respective coordinates and a label with their name. 
    Next, draw lines connecting that circle to the circle of each person they
    follow. 
    """
    network = create_friends_dict(friends_file)
    coord = create_coords_dict(coordinates_file)
    draw_coordinates(canvas, coord)
    draw_networks(canvas, coord, network)

def create_friends_dict(friends_file):
    """
    Process the friends file and return a dictionary where keys are the name
    and values are lists of that name's friends.
    """
    network = dict()
    with open(friends_file) as file:
        for line in file:
            name_and_friends = line.split(':')
            name = name_and_friends[0]
            friends = [friend.strip() for friend in name_and_friends[1].split(',')]
            network[name] = friends
    return network

def create_coords_dict(coordinates_file):
    coord = dict()
    with open(coordinates_file) as file:
        for line in file:
            name_and_coordinate = line.split(':')
            name = name_and_coordinate[0]
            coordinate = tuple(map(int, name_and_coordinate[1].split(',')))
            coord[name] = coordinate
    return coord

def draw_coordinates(canvas, coord):
    """
    Draw dots on the canvas.
    Each dot represents a person in the coordinate dictionary.
    """
    for name in coord:
        x, y = coord[name]
        canvas.create_oval(
            x - DOT_RADIUS / 2,
            y - DOT_RADIUS / 2,
            x + DOT_RADIUS / 2,
            y + DOT_RADIUS / 2,
            outline=DOT_COLOR,
            fill=DOT_COLOR
        )
        canvas.create_text(
            x, 
            y-12, 
            anchor='c', 
            fill=TEXT_COLOR, 
            text=name, 
            font=('Calibri', 10)
        )
    canvas.update()

def draw_networks(canvas, coord, network):
    """
    Draw lines connect the dots if they have relationship.
    """
    for name in network:
        for friend in network[name]:
            x0, y0 = coord[name]
            x1, y1 = coord[friend]
            canvas.create_line(x0, y0, x1, y1, arrow=tk.LAST)

canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Sunset')
draw_friend_graph(canvas, FRIENDS_FILE, COORDINATES_FILE)
canvas.mainloop()
