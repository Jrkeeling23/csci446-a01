import queue


# TODO: Always check for shortest length of all nodes connected to current node and follow that path.
# -each node has a list of nodes with distance attached
# expands closest node to goal

class GREEDY:

    def __init__(self):

        self.frontier_list = []
        self.current_node = None

        self.x = 0
        self.y = 0

        self.visited_list = []

        self.test_list = []

    # EXPANDS THE FRONTIER TO THE LEAST COSTLY PATH UNTIL SOLUTION IS FOUND
    def solve_maze(self, start_node, end_node):
        self.last_node = end_node

        # should grab a list of cords
        lastNodeCords = end_node.coordinates
        self.y = lastNodeCords[0]
        self.x = lastNodeCords[1]

        # TODO: replace this junk with loop for the frontier list
        self.current_node = start_node
        self.currentPos = 0
        self.add_to_frontier()

        # Will continue until the maze is solved
        while not self.current_node.is_end or self.frontier_list.empty():

            #inits the smallest frontier node's node to the first one in the list
            smallester = self.find_connected_nodes(self.frontier_list[0])
            posTemp = 0
            tempiter = 0

            #sets smallest to the node we will be expanding, and marks it's position in the frontier
            for n in self.frontier_list:
                #find connected nodes should return the node with the smallest distance to the goal
                tempNodes = self.find_connected_nodes(n)
                if (tempNodes != None):
                    if(self.getManToEnd(tempNodes)<self.getManToEnd(smallester)):
                        posTemp = tempiter
                        smallester = n
                else:
                    pass
                    #self.remove_from_frontier(tempiter)
                    #print("REMOVED: "+str(tempiter))
                    #tempiter -= 1
                tempiter += 1

            possible_node = smallester  # Will be 'None' or the node with the shortest path from the beginning.

            if possible_node is None:
                print(posTemp)
                self.remove_from_frontier(posTemp) # Remove from list since there are no  unvisited connecting nodes.
            else:
                print("uNIQUE")
                self.current_node = possible_node  # Make current node now the unvisited returned node.
                self.add_to_frontier()  # Add unvisited node to list
        return 0, 0, self.test_list

    def add_to_frontier(self):
        print("ADD CALL: ")
        self.frontier_list.append(self.current_node)
        self.change_visited_status()
        self.test_list.append(self.current_node)

    # Removes the targeted node from the frontier
    def remove_from_frontier(self, pos):
        print("REMOVAL CALL: "+str(pos))
        node = self.frontier_list.__getitem__(pos)
        self.frontier_list.remove(node)

        self.visited_list.append(node)

        if(len(self.frontier_list)>0):
            self.current_node = self.frontier_list[0]
        else:
            print("list has nulled out")

    def check_if_visited(self, connecting_node):
        if connecting_node.visited is True:
            return True
        else:
            return False

    def change_visited_status(self):
        self.current_node.visited = True

    # Gets the Manhatten distance based off the Node's position & the End node's position
    def getManToEnd(self, node):
        # replace this with actual node, where we get its cords
        nX,nY = node.coordinates

        print(str(nX)+","+str(nY))

        Xdistance = abs(self.x - nX)
        Ydistance = abs(self.y - nY)

        distance = Xdistance + Ydistance

        return distance

    # Check for which one has the shortest manhatten distance, and return it
    def find_connected_nodes(self,node):
        #self.current_node in place of node
        connected_nodes = node.get_local_nodes().copy()
        nodeList = []
        # Put all of the connected nodes into a list
        while len(connected_nodes) >= 0:
            if len(connected_nodes) is 0:
                break
            else:
                # adds just the node to the list, stripping away the other distance
                connecting_node = connected_nodes.pop()
                nodeList.append(connecting_node[1])

        # initializes the smallest node as None
        smallest = nodeList[0]

        # TODO: make loop for checking the smallest of all the nodes on the frontier to expand?
        # iterate through connected nodes to find the smallest
        for node in nodeList:
            # sets smallest to the current node if null, or if the smallest's distance to the end is larger than the current node's
            if ((smallest == None) or (self.getManToEnd(smallest) > self.getManToEnd(node))):
                if(self.check_if_visited(smallest) == False):
                    smallest = node
                    #print("Smallest found!:"+str(smallest))

        return (smallest)


"""
        def find_connected_nodes(self):
            connected_nodes = self.current_node.get_local_nodes()  # A list of all connecting nodes

            # initializes the smallest node as the first one on the stack
            closestNode = None

            # TODO: Fix Getting stuck in here? NO end state?
            while len(connected_nodes) >= 0:
                if len(connected_nodes) is 0:
                    break
                else:
                    print("Alive")
                    connecting_node = connected_nodes.pop()
                    # If the node has not been visited
                    if self.check_if_visited(connecting_node[1]) is False:
                        # compares the values of the two manhatten distances
                        if ((connected_nodes[0] < closestNode[0]) or (closestNode == None)):
                            closestNode = connected_nodes
                    else:
                        if len(connected_nodes) is 0:
                            return None
                    # returns the node with the smallest manhatten distance
                    return closestNode[1]
"""
