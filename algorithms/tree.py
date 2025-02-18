from random import sample
from components.agent import Agent
from algorithms.neighbours import get_neighbours

class Tree:

    def __init__(self, prover:Agent, depth:int, number_of_nodes_per_depth:list, agent_dictionary):
        self.prover = prover
        self.nodes = [[prover]]
        self.depth = depth
        self.n_d = number_of_nodes_per_depth

        for depth_level in range(self.depth):
            depth_level_node_list = []

            for parent in self.nodes[depth_level]:
                parent.neighbours = get_neighbours(parent, agent_dictionary)
                children = sample(parent.neighbours, self.n_d[depth_level])
                depth_level_node_list.append(children)
            self.nodes.extend(depth_level_node_list)

            
                    
#prover = neighbour_list[0]
#tree1 = Tree(prover, 3, [2, 3, 2], neighbour_list)
#print(tree1.nodes)