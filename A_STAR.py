#TODO: Implement A* heuristic function
#TODO: set up to take in start node
#TODO: Make return  a list of solution nodes

#BE thorough w/ function 'get_local_nodes'

import queue

class A_STAR:

    def __init__(self, start_node,size):

        self.frontier_queue = queue.Queue(size)

        self.current_node = start_node

        self.visited_list = []

        #What is the test list for?
        self.test_list = []


    def solve_maze(self, start_node):
        self.current_node = start_node
        self.add_to_frontier()
        while self.current_node.is_end is not True:  # continue until end of maze.

            possible_node = self.find_connected_nodes()  # Will be 'None' or a node.

            if possible_node is None:
                self.remove_from_frontier()  # Remove from stack since there are no  unvisited connecting nodes.
            else:
                self.current_node = possible_node  # Make current node now the unvisited returned node.
                self.add_to_frontier()  # Add unvisited node to stack

                self.test_list.append(self.current_node)
        return self.test_list

    def add_to_frontier(self):
        self.frontier_stack.put(self.current_node)
        self.change_visited_status()

    def remove_from_frontier(self):
        node = self.frontier_stack.get()
        self.visited_list.append(node)
        self.current_node = self.frontier_stack.get()
        self.frontier_stack.put(self.current_node)

    def check_if_visited(self, connecting_node):
        if connecting_node.visited is True:
            return True
        else:
            return False

    def change_visited_status(self):
        self.current_node.visited = True

    def find_connected_nodes(self):
        connected_nodes = self.current_node.get_local_nodes()  # A list of all connecting nodes

        while len(connected_nodes) >= 0:
            if len(connected_nodes) is 0:
                break
            else:
                connecting_node = connected_nodes.pop()
                # If the node has not been visited
                if self.check_if_visited(connecting_node[1]) is False:
                    return connecting_node[1]  # break from while-loop to return the unvisited connecting node
                else:
                    if len(connected_nodes) is 0:
                        return None

