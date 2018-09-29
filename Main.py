running = True


def read_in_maze(string):
    if string == 'O':
        print("O")
    elif string == 'M':
        print("M")
    elif string == 'L':
        print('L')
    else:
        print("Please enter O, M, or L")


while running:
    inp = "" + input("Enter the maze type you would like to run, M for medium maze,"
                     " O for open maze, and L for large maze: ")
    read_in_maze(inp)
