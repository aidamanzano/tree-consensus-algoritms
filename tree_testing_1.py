

#parent names children
#parent appends children to 'children' list in dictionary
#add agent instance to the dictionary 'instance'
#TODO: set the parent agent in the next depth level

from random import sample
from components.agent import Agent
from algorithms.neighbours import get_neighbours

agents_list = [Agent(p_response=[0.1, 0.5, 0.4], p_claim=[0.1, 0.5, 0.4], environment_bounds=[[0, 1], [0,1]]) for _ in range(20)]

#agents_dict contains as keys the agents' positions, and the agent instance as the value. 
agent_dictionary = {(agent.x_position, agent.y_position):agent for agent in agents_list}

#nodes = [[prover],[]]
depth = 2
n_d = [2, 3]

prover = agents_list[0]
starting_dict = { 0: {prover: {'children': [],
                        'instance': 'AgentInstance',
                        'parent': None}}}

#--------------THIS IS THE CODE TO ADD THE CHILDREN TO THE PARENT AT THAT DEPTH LEVEL----------------------
for depth_level in range(depth):

    for parent in starting_dict[depth_level]:
        print('parent: ', parent)
        
        parent.neighbours = get_neighbours(parent, agent_dictionary)
        children = sample(parent.neighbours, n_d[depth_level])
        #set the parent of these children to equal parent here. 
        #print(children)
        starting_dict[depth_level][parent]['children'] = children
        
        parent_dict = {}
        for child in starting_dict[depth_level][parent]['children']:
            #print(child)
        #make a new depth level dictionary
            running_children_dict = {child: {'children': [],
                            'instance': child,
                            'parent': parent}}
            #then we put this dictionary in the NEXT depth level
            #and then we re call the function. 
            #starting_dict.update({depth_level + 1: depth_level_Dict})
            
            #THIS SEEMS CLOSE:
            #starting_dict[depth_level] = starting_dict[depth_level] | depth_level_Dict
            
            parent_dict = parent_dict | running_children_dict
        starting_dict.update({depth_level + 1: parent_dict})
            
print(starting_dict)

'''
for each parent at that depth level:
    sample some children
    add the children to the parent
    make each child's parent the parent
    add the children as parents, to the next depth level
    repeat
    '''