from random import sample
import sys
import os

# Get the absolute path of the project root (two levels up)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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



agents_list = [Agent(p_response=[0.1, 0.5, 0.4], p_claim=[0.1, 0.5, 0.4], environment_bounds=[[0, 1], [0,1]]) for _ in range(8)]

#agents_dict contains as keys the agents' positions, and the agent instance as the value. 
agent_dict = {(agent.x_position, agent.y_position):agent for agent in agents_list}
prover = agents_list[0]
tree3 = Tree(prover=prover, depth=2, number_of_nodes_per_depth=[2, 3], agent_dictionary=agent_dict)
print(tree3.nodes)



