import math
import random
from tqdm import tqdm
from model.var_from_cfg import min_edge_weight, percent_select_node


class DeepWalk:
    def __init__(self, graph):
        self.G = graph
        self.nodes = {n for n, d in self.G.nodes(data=True) if d['bipartite'] == 0}

        self.min_weight = min_edge_weight  # include edges only that have this minimum weight
        self.k = percent_select_node  # percentage of nodes to select

        # finding the best neighbor for each nodes
        self.sorted_selected_neighbors = {}
        for node in self.G.nodes:
            # extracting all the neigbors of this node
            selected = self.G[node].items()

            # sorting all neighbor nodes based on weight
            selected = sorted(selected, key=lambda x: x[1]['weight'], reverse=True)

            # extracting the nodes name with given weight
            selected = [i[0] for i in selected if i[1]['weight'] >= self.min_weight]

            # finding the number of nodes to be selected at last
            till = math.ceil(len(selected) * self.k / 100)

            # selecting the calculated number of nodes
            self.sorted_selected_neighbors[node] = selected[:till]

    def select_neighbor(self, walk):
        """
         Select a neighbor from the walk. This is used to select a randomly selected node in the tree
         
         @param walk - list of nodes that are walked
         
         @return node selected or None if no node is selected ( in which case we don't know
        """
        node = walk[-1]
        criteria = self.sorted_selected_neighbors[node]
        try:
            return random.choice(criteria)
        except:
            pass

    def random_walk(self, start_node, max_walk_length):
        """
         Returns a random walk starting from start_node up to max_walk_length.
         
         @param start_node - The node to start the walk from.
         @param max_walk_length - The maximum length of the walk.
         
         @return A list of nodes that are walked from start
        """
        walk = [start_node]
        for _ in range(max_walk_length - 1):
            node = self.select_neighbor(walk)
            if node == None: break
            walk.append(node)

        # removing user nodes from the graph
        walk = [node for i, node in enumerate(walk) if i % 2 == 0]

        return walk

    def get_walks(self, max_walk_length, num_walks_per_node):
        """
        Get a list of walks. This is a generator function that iterates over the nodes in the graph and returns a list of randomly generated walks.
        
        @param max_walk_length - The maximum length of a walk in the graph.
        @param num_walks_per_node - The number of walks to generate per node.
        
        @return A list of : class : ` ~gensim. models. walk. Walk `
        """

        max_walk_length = max_walk_length * 2  # as there are users also included in the walk

        walks = []
        with tqdm(total=num_walks_per_node * len(self.nodes)) as pbar:  # using tqdm to measure progress
            for node in self.nodes:
                for _ in range(num_walks_per_node):
                    walk = self.random_walk(node, max_walk_length)
                    walks.append(walk)
                    pbar.update(1)

        return walks