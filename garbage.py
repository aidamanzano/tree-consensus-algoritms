from random import sample
from components.agent import Agent
from algorithms.neighbours import get_neighbours

# Initialize the starting dictionary
starting_dict = {
    0: {
        'prover': {
            'children': [],
            'instance': 'AgentInstance',
            'parent': None
        }
    }
}

# Initialize agents
agents_list = [
    Agent(p_response=[0.1, 0.5, 0.4], p_claim=[0.1, 0.5, 0.4], environment_bounds=[[0, 1], [0, 1]])
    for _ in range(10)
]

# Create a dictionary mapping agent positions to instances
agent_dictionary = {(agent.x_position, agent.y_position): agent for agent in agents_list}

'''
for each parent at that depth level:
    sample some children
    add the children to the parent's children 
    make each child's parent the parent
    add the children as parents, to the next depth level
    recurse
    '''

def recursive_build_tree(starting_tree, agent_dictionary, depth_level, max_depth, n_d):
    if depth_level == max_depth:
        return starting_tree
    
    # Ensure the next depth level exists
    if depth_level + 1 not in starting_tree:
        starting_tree[depth_level + 1] = {depth_level + 1: {}}

    for parent in starting_tree[depth_level]:
        parent.neighbours = get_neighbours(parent, agent_dictionary)
        children = sample(parent.neighbours, n_d[depth_level])
        
        starting_dict[depth_level][parent]['children'] = children
        #set the parent of these children to equal parent here. 
        #print(children)
        
        for child in children: #TODO: is this the same as starting_dict[depth_level][parent]['children']?
            child.parent = parent
            child_dict = {child: {'children': [],
                            'instance': child,
                            'parent': parent}}
            
            #if child not in starting_tree[depth_level+1]:
            starting_tree[depth_level + 1].update(child_dict)
                #TODO
            
    return recursive_build_tree(starting_tree, agent_dictionary, depth_level + 1, max_depth, n_d)
    

output = {0: 
            {<components.agent.Agent object at 0x1103a1f00>: 
            {'children': [<components.agent.Agent object at 0x11258c490>, <components.agent.Agent object at 0x11155d270>], 
            'instance': 'AgentInstance', 
            'parent': None}}, 

        1: {<components.agent.Agent object at 0x11258c490>: 
            {'children': [<components.agent.Agent object at 0x112699060>, <components.agent.Agent object at 0x11266d210>, <components.agent.Agent object at 0x11246dd50>], 
            'instance': <components.agent.Agent object at 0x11258c490>, 
            'parent': <components.agent.Agent object at 0x1103a1f00>}, 
            
            <components.agent.Agent object at 0x11155d270>: 
            {'children': [<components.agent.Agent object at 0x1103a35b0>, <components.agent.Agent object at 0x1076bd5d0>, <components.agent.Agent object at 0x11265dbd0>], 
            'instance': <components.agent.Agent object at 0x11155d270>, 
            'parent': <components.agent.Agent object at 0x1103a1f00>}}, 
            
        2: {<components.agent.Agent object at 0x112699060>: 
            {'children': [], 
            'instance': <components.agent.Agent object at 0x112699060>, 
            'parent': <components.agent.Agent object at 0x11258c490>}, 
            
            <components.agent.Agent object at 0x11266d210>: 
            {'children': [], 
            'instance': <components.agent.Agent object at 0x11266d210>, 
            'parent': <components.agent.Agent object at 0x11258c490>}, 
            
            <components.agent.Agent object at 0x11246dd50>: 
            {'children': [], 
            'instance': <components.agent.Agent object at 0x11246dd50>, 
            'parent': <components.agent.Agent object at 0x11258c490>}, 
            
            <components.agent.Agent object at 0x1103a35b0>: 
            {'children': [], 
            'instance': <components.agent.Agent object at 0x1103a35b0>, 
            'parent': <components.agent.Agent object at 0x11155d270>},
            
            <components.agent.Agent object at 0x1076bd5d0>: 
            {'children': [], 
            'instance': <components.agent.Agent object at 0x1076bd5d0>, 
            'parent': <components.agent.Agent object at 0x11155d270>}, 
            
            <components.agent.Agent object at 0x11265dbd0>: 
            {'children': [], 
            'instance': <components.agent.Agent object at 0x11265dbd0>, 
            'parent': <components.agent.Agent object at 0x11155d270>}}}
