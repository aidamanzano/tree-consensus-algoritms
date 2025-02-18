from components.agent import Agent
from typing import List

def agent_generator(p_response:List, p_claim:List, environment_bounds:List, number_of_agents) -> list:
    agent_list = [Agent(p_response, p_claim, environment_bounds) for _ in range(number_of_agents)]
    return agent_list

def agent_positions_dict(agent_list:list) -> dict:
    agents_dictionary = {(agent.x_position, agent.y_position):agent for agent in agent_list}
    return agents_dictionary

