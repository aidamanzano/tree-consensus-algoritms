from scipy.spatial import KDTree
from components.agent import Agent


#agent_dictionary input for this function REQUIRES list in the format of:
#agents_list = [Agent(p_response=[p1, p2, p3], p_claim=[p1, p2, p3], environment_bounds=[[0, 1], [0,1]]) for _ in range(N_agents)]
#agents_dict contains as keys the agents' positions, and the agent instance as the value. It looks like:
#agent_dict = {(agent.x_position, agent.y_position):agent}



def get_neighbours(parent: Agent, agent_dictionary:dict) -> list:
    
    neighbours = []
    tree = KDTree(list(agent_dictionary.keys()))
    neighbours_indicies = tree.query_ball_point((parent.x_position, parent.y_position), parent.range_of_sight)
    for neighbour_index in neighbours_indicies:
        neighbour_agent = list(agent_dictionary.values())[neighbour_index]
        neighbours.append(neighbour_agent)
    return neighbours

