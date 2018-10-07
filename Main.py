"""
Authors: George Engel, Cory Johns, Justin Keeling 
"""
from MazeNode import MazeNode
from DFS import DFS
from BFS import BFS

running = True
start_indicator = 'P'  # string representing the start of the maze
end_indicator = '*'  # string representing the end of the maze
wall_indicator = '%'  # string representing a wall in the maze


def read_in_maze(string):
    global running

    def __build_maze(file):
        """
        Builds a node matrix from the input file
        :param file: containing the maze in text form
        :return: the root node of the matrix
        """
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
        # convert into nodes
        return __build_nodes()

    def __build_nodes():
        """
        Build the matrix of nodes from the maze array
        
        Important design points:
        - conversion starts at index (0, 0) and progresses along a row
          and adds/connects nodes (row+1, col) and (row, col+1) if they are not walls
        - this allows us to hit all the nodes without checking the same node twice and 
          guarantees the that the nodes we are testing are not made already
        - the program will return the node that contains the start, this will act as the 'root' and 
          will consequently lose all islands not reachable from the root
        
        :return: start_node, the node containing the start of the maze, which functions as the 'root' node
        """

        def add_unique_node(row, col):
            """
            Add a new node, if it has not been made already at the given row, col
            or returns the existing node
            :param row: row of the new node
            :param col: col of the new node
            :return: node, the new or already existing node at row, col OR None if the target is a wall
            """
            nonlocal start_node

            # only add a node if it is not a wall
            if maze_xy[row][col] != wall_indicator:
                # check if there is a node there, add if there is not
                if tmp_node_list[row][col] is None:
                    node = MazeNode(row, col)
                    tmp_node_list[row][col] = node
                else:
                    node = tmp_node_list[row][col]

                # check if this node is the start / end
                if maze_xy[row][col] == start_indicator:
                    node.is_start = True
                    start_node = node
                elif maze_xy[row][col] == end_indicator:
                    node.is_end = True

                # return the node for the row, col
                return node
            else:
                return None

        def check_next_node(go_right, current_node):
            """
            Checks if the adjacent node to the right/ below the given node is connected,
            will make a new node there and connect it if it is note present if the space is not a wall
            :param go_right: True if testing the node to the right, False if testing the node below
            :param current_node: the node to start from
            """
            # get delta coordinates for the target node
            delta_col = int(go_right)
            delta_row = int(not go_right)
            # get coordinates of the current node
            current_row, current_col = current_node.coordinates

            # test if in bounds
            if current_row + delta_row < len(maze_xy) and current_col + delta_col < len(maze_xy[0]):
                # add target node
                local_node = add_unique_node(current_row + delta_row, current_col + delta_col)

                if local_node is None:
                    # node was a wall
                    return
                else:
                    # connect current node and target node
                    current_node.add_local_node(local_node, 1)

        global start_indicator
        nonlocal maze_xy
        # placeholder for the start / root node
        start_node = None
        # make empty 2d list to temporarily index the nodes
        tmp_node_list = [i[:] for i in [[None] * len(maze_xy[0])] * len(maze_xy)]

        # make the node mesh
        for r in range(len(tmp_node_list)):
            for c in range(len(tmp_node_list[r])):
                # add the node
                this_node = add_unique_node(r, c)

                # check if location was not a wall
                if this_node is not None:
                    # check lower
                    check_next_node(False, this_node)
                    # check right
                    check_next_node(True, this_node)

        # start_node and tmp_node_list are updated in the helper functions
        return start_node

    def print_maze(maze, sub_list=None, sub_char="."):
        """
        Prints out the maze while substituting the given list of [row, col] locations for the sub_char
        :param maze: the base maze
        :param sub_list: list in form [[row, col], [...], ...] of sub locations
        :param sub_char: char to replace the locations in sub_list with
        :return: Nothing
        """

        for i in range(len(maze)):
            for j in range(len(maze[i])):
                sub = False
                # find if current square should be substituted
                if sub_list is not None:
                    for x, y in sub_list:
                        if i == x and j == y:
                            sub = True
                            break
                if sub and maze[i][j] != start_indicator and maze[i][j] != end_indicator:
                    print(sub_char, end="")
                elif maze[i][j] == wall_indicator:
                    print("%", end="")
                else:
                    print(maze[i][j], end="")
            print("")

    def top_level_search(func):
        """
        Finds the solution to the maze with start location 'root' using DFS, BFS, Greedy, or A*.
        Also prints the solution to standard output.
        
        :param func: the search function to use, the search function should take the root node as an input
        and return a list of each node visited along the path.
        :return : Nothing
        """
        # get list of path nodes
        solution_list = func()

        sub_list = []
        # convert solution to sub points
        for node in solution_list:
            sub_list.append(node.coordinates)

        # print solution
        print_maze(maze_xy, sub_list)

        # reset all nodes back to unvisited
        for node in solution_list:
            node.visited = False

    # the maze will go here, overwrites for each run
    maze_xy = []
    root_node = None

    # maze txt files must be in the same directory with the given names
    if string == 'O' or string == 'o':
        root_node = __build_maze("open maze.txt")
    elif string == 'M' or string == 'm':
        root_node = __build_maze("medium maze.txt")
    elif string == 'L' or string == 'l':
        root_node = __build_maze("large maze.txt")
    elif string == 'Q' or string == 'q':
        # quit the loop
        running = False
    else:
        print("Please enter O, M, or L")

    dfs_obj = DFS(root_node)
    bfs_obj = BFS(root_node, len(maze_xy)*len(maze_xy[0]))
    search_function_list = [["Depth First Search", dfs_obj.solve_maze],
                            ["Breadth First Search", bfs_obj.solve_maze]]

    # print the results of each search
    for fname, f in search_function_list:
        print("Now running " + fname + ": ")
        top_level_search(f)


while running:
    inp = "" + input("Enter the maze type you would like to run, M for medium maze,"
                     " O for open maze, and L for large maze, and Q to quit: ")
    read_in_maze(inp)
