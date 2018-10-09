import queue


class DFS:

    def __init__(self):
        self.frontier_stack = queue.LifoQueue(maxsize=0)  # use queue fifo for stack
        self.current_node = None  # set current node to 'none' until sort maze is called
        self.visited_list = []  # a list of visited nodes along the path
        self.test_list = []

    def solve_maze(self, start_node, end_node):
        """
        solves the maze by using a while loop and calling other methods.
        :param start_node: the starting point of the maze.
        :return visited_list:  a list of all visited nodes while completing search
        """
        nodes_in_solution = 0
        self.current_node = start_node  # give current_node a value of the starting node.
        self.add_to_frontier()  # add current node to the stack.
        while self.current_node.is_end is not True:  # continue until end of maze.

            possible_node = self.find_connected_nodes()
            # possible node will be 'None' if all connecting nodes are visited or a connecting node.

            if possible_node is None:
                self.remove_from_frontier()  # remove current from stack since there are no unvisited connecting nodes
                nodes_in_solution -= 1
            else:
                self.current_node = possible_node  # make current node now the unvisited returned node
                self.add_to_frontier()  # add unvisited node to stack
                nodes_in_solution += 1
        return nodes_in_solution, self.visited_list

    def add_to_frontier(self):  # adds the current node to the frontier stack
        self.visited_list.append(self.current_node)
        self.frontier_stack.put(self.current_node)  # use put function to add to stack, from queue import
        self.change_visited_status()  # must change the current node's visited to true

    def remove_from_frontier(self):  # remove the current node from the stack
        node = self.frontier_stack.get()  # set a new local variable 'node' equal to the node leaving stack
        # self.test_list.append(node)
        if self.current_node is node:
            self.current_node = self.frontier_stack.get()  # remove another node and set current node equal to it
            self.frontier_stack.put(self.current_node)  # add the current node back to frontier
        else:
            self.current_node = node

    def check_if_visited(self, connecting_node):
        """
        checks and returns if the connecting node is visited or not
        :param connecting_node: a connecting node to current node
        :return True or False:  if connecting node is visited, True, if not visited, false
        """
        if connecting_node.visited is True:
            return True
        else:
            return False

    def change_visited_status(self):  # Changes current nodes visited to true and only true
        self.current_node.visited = True

    def find_connected_nodes(self):
        """
        Finds the connecting nodes of the current node. Checks if they have been visited or not.
        :return unvisited node or None:
        """
        connected_nodes = self.current_node.get_local_nodes().copy()  # makes a copy of list, so original is safe

        while len(connected_nodes) >= 0:  # continues until forced break
            if len(connected_nodes) is 0:  # the length is 0, break from loop
                break
            else:  # if the length of connecting nodes is greater than 0
                connecting_node = connected_nodes.pop()  # set new variable for single connecting node

                if self.check_if_visited(connecting_node[1]) is False:  # if the node has not been visited
                    return connecting_node[1]  # return the unvisited connecting node
                else:  # node has been visited
                    if len(connected_nodes) is 0:  # if last/only connecting node is already visited
                        return None
