import queue


def change_visited_status(current_node):
    current_node.visited = True


def check_if_visited(connecting_node):
    if connecting_node.visited:
        return True
    else:
        return False


def find_connected_nodes(current_node):
    connected_nodes = current_node.get_local_nodes()  # A list of all connecting nodes
    list_of_unvisited = []
    while connected_nodes.count >= 1:
        connecting_node = connected_nodes.pop()
        if not check_if_visited(connecting_node):
            list_of_unvisited.append(connecting_node)
    return list_of_unvisited


class BFS:
    def __init__(self, start_node, size):
        self.frontier_queue = queue.Queue(size)
        self.current_node = start_node
        self.add_to_frontier()
        self.visited = []

    def solve_maze(self):
        while not self.current_node.is_end or self.frontier_queue.empty():
            # once the current node equals the end state or the queue is empty
            connecting_nodes = find_connected_nodes(self.current_node)
            if connecting_nodes.__sizeof__() > 0:
                self.remove_from_frontier()  # remove the current node from queue
                for size in range(len(connecting_nodes)):
                    self.current_node = connecting_nodes[size]
                    self.add_to_frontier()
            else:
                self.current_node = self.frontier_queue.get()
        return self.visited

    def add_to_frontier(self):
        self.frontier_queue.put(self.current_node)  # add current_node to queue
        change_visited_status(self.current_node)  # Change visited to true

    def remove_from_frontier(self):
        self.visited.append(self.frontier_queue.get())    # Remove from queue
