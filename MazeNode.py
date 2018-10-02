class MazeNode:
    """
    Basic class for Nodes in the maze, a Node is defined as a square in the maze where ether a corner or 
    a choice exists. Each node will contain a list of connected nodes and the distance to each as well as 
    a visited flag and the nodes true x, y coordinates in the maze.
    
    Important points:
    - uses a function to update local_nodes list
    - distance in local_nodes list is the path length between the nodes
    - local_nodes is a list
    
    More information on python classes: https://docs.python.org/3/tutorial/classes.html
    More information on python builtin queues: https://docs.python.org/3/library/queue.html
    """
    def __init__(self, x_loc, y_loc):
        self.coordinates = [x_loc, y_loc]
        self.visited = False

        # provides a function for updating the local node list
        self.__local_nodes = []    # add in form [distance, MazeNode]

    def add_local_node(self, node, distance):
        """
        Adds the given node at the given distance to the list of local nodes
        :param node: the local node
        :param distance: the distance to the node
        """
        # connect node if it is not connected already
        if not self.is_connected(node):
            self.__local_nodes.append([distance, node])
        # from node, connect this node if it is not already connected
        node.add_local_node(self, distance)

    def is_connected(self, other_node):
        """
        Checks if other_node is already connected to this node
        :param other_node: the node to check for connection
        :return: True / False
        """
        for node in self.__local_nodes:
            # if list is empty, false
            if node is None:
                return False
            # nodes are uniquely defined by there coordinates
            if node.coordinates == other_node.coordinates:
                return True
        # didn't find any matching nodes, so other_node is not currently connected
        return False

