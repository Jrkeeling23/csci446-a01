import io
running = True

def readInMaze(string):
    if(string == 'O'):
        print("O")
    elif(string == 'M'):
        print("M")
    elif(string == 'L'):
        print('L')

while(running):
    string = ""+input("Enter the maze type you would like to run, M for medium maze, O for open maze, and L for large maze: ")
    readInMaze(string)
