
from neighbours import get_neighbours
from random import sample

def recursive_build_tree(starting_tree:dict, agent_dictionary:dict, depth_level:int, max_depth:int, n_d:list):
    if depth_level == max_depth:
        return starting_tree
    
    # Ensure the next depth level exists
    if depth_level + 1 not in starting_tree:
        starting_tree[depth_level + 1] = {}

    for parent in starting_tree[depth_level]:
        print('parent: ', parent)
        parent.neighbours = get_neighbours(parent, agent_dictionary)
        children = sample(parent.neighbours, n_d[depth_level])
        
        starting_tree[depth_level][parent]['children'] = children
        #set the parent of these children to equal parent here. 
        #print(children)
        
        for child in children: #TODO: is this the same as starting_dict[depth_level][parent]['children']?
            child.parent = parent
            child_dict = {child: {'children': [],
                            'instance': child,
                            'parent': parent}}
            
            #if child not in starting_tree[depth_level+1]:
            starting_tree[depth_level + 1].update(child_dict)

    return recursive_build_tree(starting_tree, agent_dictionary, depth_level + 1, max_depth, n_d)