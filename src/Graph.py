import math
import random
import matplotlib.pyplot as plt

from src import Node


class Graph:
    def __init__(self, max_x = 10, max_y = 10, node_chance = 25, adj_chance = 30, nearby_threshold = 3):
        '''
        Initialize a new graph
        :param max_x: Horizaontal size of the graph
        :param max_y: Vertical size of the graph
        :param node_chance: Percent chance of creating a node (0-100)
        :param adj_chance: Percent chance of creating a connection between two nearby nodes (0-100)
        :param nearby_threshold: The threshold distance at which a node is considered nearby enough to attempt to create a connection to
        '''
        self.max_x = max_x
        self.max_y = max_y
        self.node_chance = node_chance
        self.adj_chance = adj_chance
        self.nearby_threashold = nearby_threshold
        self.nodes = []
        self.adjacencies = [[[] for i in range(max_y)] for j in range(max_x)]
        self.fill_graph()
        self.start = self.nodes[random.randint(0,len(self.nodes))]
        self.goal = self.start
        self.solution = []
        while self.goal == self.start and len(self.nodes) >= 2:
            self.goal = self.nodes[random.randint(0,len(self.nodes))]

    def calc_dist(self, nodeA: Node, nodeB: Node):
        '''
        Get the weight of a path between two nodes. This
        equates to the manhatten distance between the two
        nodes

        :return: the distance between the two nodes
        '''
        x_diff = math.fabs(nodeB.x_pos - nodeA.x_pos)
        y_diff = math.fabs(nodeB.y_pos - nodeA.y_pos)
        return math.sqrt((x_diff ** 2) + (y_diff ** 2))

    def generate_node(self):
        '''
        Genereates an instance of a node compatible with
        the current graph (e.g. not in an existing location,
        and not out of bounds) but does not assign it to the graph
        (i.e. add it to nodes[]).

        :return: and instance of a node that's compatible with the current graph
        '''
        valid_node_found = False
        while not valid_node_found:
            x_pos = random.randint(0,self.max_x + 1)
            y_pos = random.randint(0,self.max_y + 1)
            if not self.node_at_pos_exists(x_pos, y_pos):
                valid_node_found = True
        new_node = Node(x_pos, y_pos)
        return new_node

    def node_at_pos_exists(self,x_pos: int, y_pos:  int):
        '''
        Determine if a node exists at a given point on the graph

        :param x_pos: The x position to evaluate
        :param y_pos: The y position to evaluate
        :return: True if a node exists at the pos, false if not
        '''

        node_found = False
        for node in self.nodes:
            if node.x_pos == x_pos and node.y_pos == y_pos:
                node_found = True
                break
        return node_found

    def gen_node_at_pos(self, x_pos, y_pos):
        '''
        Genereates a new node at a given position and
        adds it to the graph. This will also create any
        necessary edges
        :param x_pos: x position to add a node at
        :param y_pos: y position to add a node at
        :return: none
        '''
        new_node = Node.Node(x_pos, y_pos)
        self.nodes.append(new_node)
        for node in self.nodes:
            if self.nodes_are_close(new_node, node) and new_node is not node:
                # self.adjacencies[new_node.name+'To'+node.name] = (new_node, node, self.calc_dist(new_node, node))
                self.adjacencies[new_node.x_pos][new_node.y_pos].append(node)

    def nodes_are_close(self, nodeA: Node, nodeB: Node):
        '''
        Deteremines if two nodes are 'nearby' one another, as defined
        by the threshold set at the graph's creation
        :param nodeA: The first node to consider
        :param nodeB: The second node to consider
        :return: True if the nodes are within nearby_threshold distance of eachother, false otherwise
        '''
        if self.calc_dist(nodeA, nodeB) < self.nearby_threashold:
            return True
        else:
            return False

    def fill_graph(self):
        '''
        Fills the emtpy graph (self) with generated nodes
        :return:  none
        '''
        for x in range(self.max_x):
            for y in range(self.max_y):
                create_node = random.randrange(100) < self.node_chance
                if create_node:
                    self.gen_node_at_pos(x, y)

    def save(self, filename):
        '''
        Save the graph to a .png file
        :param filename: Name of the file to save the graph to (do not include the .png ext)
        :return: none
        '''

        plt.figure()
        plt.subplot(111)

        # Plot each node
        for node in self.nodes:
            plt.plot(node.x_pos, node.y_pos, 'bo', markersize=2.0)

        # Plot each node connection
        for x in range(self.max_x):
            for y in range(self.max_y):
                for adj_node in self.adjacencies[x][y]:
                    plt.plot([x,adj_node.x_pos], [y, adj_node.y_pos], 'b-', linewidth=0.2)

        # Plot solution
        for i in range(0,len(self.solution) - 1):
            nodeA = self.solution[i]
            nodeB = self.solution[i + 1]
            plt.plot([nodeA.x_pos,nodeB.x_pos], [nodeA.y_pos, nodeB.y_pos], 'm-')

        # Plot starting and goal nodes
        plt.plot(self.start.x_pos, self.start.y_pos, 'go', markersize=5.0)
        plt.plot(self.goal.x_pos, self.goal.y_pos, 'ko', markersize=5.0)

        plt.savefig(filename + '.png')
