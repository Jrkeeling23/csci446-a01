"""
Authors: George Engel, Cory Johns, Justin Keeling 
"""

running = True


def read_in_maze(string):
    global running

    def __build_maze(file):
        nonlocal maze_xy
        # open file, make a 2d list of each letter
        # with covers try-catch business, '__' prefix is 'private' sort of
        with open(file) as __f:
            for __line in __f:
                # build up a row, then add it to the maze
                __x_tmp = []
                for __char in __line:
                    # don't add newline chars
                    if __char != '\n':
                        __x_tmp.append(__char)
                maze_xy.append(__x_tmp)

    # the maze will go here, overwrites for each run
    maze_xy = []
    # maze txt files must be in the same directory with the given names
    if string == 'O' or string == 'o':
        __build_maze("open maze.txt")
    elif string == 'M' or string == 'm':
        __build_maze("medium maze.txt")
    elif string == 'L' or string == 'l':
        __build_maze("large maze.txt")
    elif string == 'Q' or string == 'q':
        # quit the loop
        running = False
    else:
        print("Please enter O, M, or L")

    for __row in maze_xy:
        print(__row)


while running:
    inp = "" + input("Enter the maze type you would like to run, M for medium maze,"
                     " O for open maze, and L for large maze, and Q to quit: ")
    read_in_maze(inp)
