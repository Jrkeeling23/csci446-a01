"""
TODO: Print maze with '.' where it has been visited.
May need a maze passed in as array, or try to print from main.

"""


def check_if_visited(connecting_node):
    if connecting_node.visited:
        return True
    else:
        return False


def change_visited_status(current_node):
    current_node.visited = True


def find_connected_nodes(current_node):
    connected_nodes = current_node.get_local_nodes()  # A list of all connecting nodes
    connecting_node = connected_nodes.pop()  # A connecting node from the list.

    found = False
    while found:
        if not check_if_visited(connecting_node):  # If the node has not been visited
            break  # break from while-loop to return the unvisited connecting node
        elif check_if_visited(connecting_node):  # If the node has been visited
            if len(connected_nodes) < 2:  # If the list only contains 1 value, which is visited, return null
                return None  # Returns 'null' if all the nodes are visited
            else:
                connecting_node = connected_nodes.pop()  # Obtains the next connecting node

    return connecting_node  # Returns the unvisited connecting node


class DFS:

    def __init__(self, start_node):
        self.frontier_stack = []
        self.current_node = start_node
        self.add_to_frontier()
        self.visited = []

    def solve_maze(self):
        while not self.current_node.is_end:  # continue until end of maze.
            possible_node = find_connected_nodes(self.current_node)  # Will be 'None' or a node.
            if possible_node is None:
                self.remove_from_frontier()  # Remove from stack since there are no  unvisited connecting nodes.
            else:
                self.current_node = possible_node  # Make current node now the unvisited returned node.
                self.add_to_frontier()  # Add unvisited node to stack

    def add_to_frontier(self):
        self.frontier_stack.append(self.current_node)
        change_visited_status(self.current_node)

    def remove_from_frontier(self):
        self.visited.append(self.frontier_stack.pop())
