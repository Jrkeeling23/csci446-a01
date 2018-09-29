import queue


class MazeNode:
    """
    Basic class for Nodes in the maze, a Node is defined as a square in the maze where ether a corner or 
    a choice exists. Each node will contain a list of connected nodes and the distance to each as well as 
    a visited flag and the nodes true x, y coordinates in the maze.
    
    Important points:
    - uses a function to update local_nodes list
    - distance in local_nodes list is the path length between the nodes
    - local_nodes is a priority queue on distance
    
    More information on python classes: https://docs.python.org/3/tutorial/classes.html
    More information on python builtin queues: https://docs.python.org/3/library/queue.html
    """
    def __init__(self, x_loc, y_loc):
        self.coordinates = [x_loc, y_loc]
        self.visited = False

        # provides a function for updating the local node list
        self.__local_nodes = queue.PriorityQueue()    # add in form put([distance, MazeNode]) to order by distance

    def add_local_node(self, node, distance):
        """
        Adds the given node at the given distance to the list of local nodes
        :param node: the local node
        :param distance: the distance to the node
        """
        self.__local_nodes.put([distance, node])

