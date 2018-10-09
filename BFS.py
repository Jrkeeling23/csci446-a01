import queue


class BFS:
    def __init__(self):
        self.frontier_queue = queue.Queue(maxsize=0)
        self.current_node = None
        self.visited = []

    def solve_maze(self, start_node, end_node):
        """
        solves maze by calling multiple functions
        :param start_node:
        :return list of visited nodes:  whatever nodes were visited will be in list
        """
        self.current_node = start_node  # set current equal to starting point
        self.change_visited_status(self.current_node)  # changed visited status when node is expanded
        while self.current_node.is_end is False:  # stop when current is end
            connecting_nodes = self.find_connected_nodes()  # get list of connected nodes

            print(len(connecting_nodes))
            if len(connecting_nodes) > 0 or len(connecting_nodes) is not None:  # if the the list has nodes
                for i in range(len(connecting_nodes)):  # iterate through nodes to add to the queue
                    if i is 0:  # save as temp to make current node later
                        self.add_to_frontier(connecting_nodes[i])  # add node to queue
                    else:  # make current node equal to connecting node [i] to add to frontier
                        self.add_to_frontier(connecting_nodes[i])  # add node to queue
                self.remove_from_frontier()  # remove from queue when all connected nodes are in queue
            else:  # if the list does not have nodes
                self.remove_from_frontier()

        return 0, self.visited

    def add_to_frontier(self, adding_node):  # adds the current node to the queue
        self.frontier_queue.put(adding_node)  # add current_node to queue
        # self.visited.append(self.current_node)  # add current node to visited list
        self.change_visited_status(adding_node)  # Change visited to true

    def remove_from_frontier(self):  # remove node from tree
        self.current_node = self.frontier_queue.get()

    def change_visited_status(self, adding_node):  # change the current nodes visited to true
        adding_node.visited = True
        self.visited.append(adding_node)

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

    def find_connected_nodes(self):
        connected_nodes = self.current_node.get_local_nodes().copy()  # makes a copy of list, so original is safe
        list_of_unvisited = []  # holds values of unvisited connected nodes of current node
        while len(connected_nodes) >= 0:  # while there are still nodes in list

            if len(connected_nodes) is 0:  # force break if before pop the length is 0
                break
            else:  # if there are still connected nodes
                connecting_node = connected_nodes.pop()  # connecting node removed from list to obtain value
                if self.check_if_visited(connecting_node[1]) is False:  # if the connected node hasn't been visited
                    list_of_unvisited.append(connecting_node[1])  # add the the unvisited local list
                else:
                    if len(connected_nodes) is 0:  # since list is popped after first if statement, it will make it
                        break  # force break to return unvisited list
        return list_of_unvisited
