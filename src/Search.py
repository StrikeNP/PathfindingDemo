import math

from Graph import Graph
from Node import Node


class Search:
    '''

    '''

    def __init__(self, graph: Graph, k: int):
        '''

        '''
        self.graph = graph
        self.start = graph.start
        self.goal = graph.goal
        self.k = k
        self.expanded_nodes = []
        self.avail_node_costs = {self.start:(0,0)} # {node pointer: (path length, path cost)}

    def find_path(self):
        '''

        :return: an array of Node objects representing the path from start -> goal, returns emtpy array if no path found
        '''
        cheapest_node = self.start
        while cheapest_node is not self.goal:
            if self.get_cheapest_node() is None:
                break # TODO is there a better way to handle this?
            cheapest_node = self.get_cheapest_node()
            for adj_node in self.get_adj_nodes(cheapest_node):
                prev_path_len, prev_path_cost = self.avail_node_costs[cheapest_node]
                distance = self.graph.calc_dist(cheapest_node, adj_node)
                self.avail_node_costs[adj_node] = prev_path_len + 1, prev_path_cost + distance
                if adj_node.parent is None:
                    adj_node.parent = cheapest_node
            self.expanded_nodes.append(cheapest_node)
            del self.avail_node_costs[cheapest_node]

        solution_path = []
        temp_node = self.goal
        while temp_node is not self.start:
            solution_path.append(temp_node)
            temp_node = temp_node.parent
        solution_path.append(self.start)
        solution_path.reverse() # Reverse because we built it backwards goal -> start
        return solution_path

    def get_cheapest_node(self):
        '''
        Find the node in available_nodes with the lowest cost to expand
        :return: The node in available_nodes with the lowest cost
        '''
        lowest_cost = math.inf
        cheapest_node = None
        for node, (k,cost) in self.avail_node_costs.items():
            if cost < lowest_cost:
                lowest_cost = cost
                cheapest_node = node

        return cheapest_node

    def get_adj_nodes(self, node: Node):
        '''
        Return a list of nodes that contain a direct path (of length 1)
        to the specified node

        :param node: Look for nodes directly connected to this node
        :return: A list of nodes that are directly connected to the given node
        '''
        return self.graph.adjacencies[node.x_pos][node.y_pos]