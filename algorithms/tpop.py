
def check_enough_nodes(tree, nodes_per_depth, depth, threshold):
    for d in range(depth):
        for parent in tree[d]:
            
            #print(tree[d][parent]['children'])
            if len(tree[d][parent]['children']) < nodes_per_depth[d] * threshold:
                return False
            else:
                return True

def check_nodes_are_unique(tree):
    tree_nodes_set = set()

    for depth_level in tree.values():  # Iterate over depth levels
        tree_nodes_set.update(depth_level.keys())

    if len(tree_nodes_set) == sum(len(parents) for parents in tree.values()):
        return True
    else:
        return False


def tree_checks(threshold:float, tree:dict, nodes_per_depth:list, depth:int)-> bool:
    """check the tree architecture is valid.
    check that: all nodes in the tree are unique
    enough nodes have been named."""
    
    condition1 = check_enough_nodes(tree, nodes_per_depth, depth, threshold)
    condition2 = check_nodes_are_unique(tree)

    if (condition1 and condition2) == True:
        return True
    else:
        return False

def reset_nodes(tree):
    # Reset the state of the output dictionary and in_tree attributes
    for depth_level in tree:
        for parent in tree[depth_level]:
            parent.in_tree = True
            for child in tree[depth_level][parent]['children']:
                child.in_tree = True

def classifier(tpop_output, t1, t2):
    #TODO: modify the agent's algorithm.output variable here?
    if tpop_output < t1:
        #classify the prover's claim as false
        return -1
    if t1 <= tpop_output < t2:
        #classify the prover's claim as unknown/unverifiable
        return 0
    if tpop_output >= t2:
        #classify the prover's claim as true
        return 1

def TPoP(tree:dict, n_d:list, depth:int, threshold:float)-> bool:
    #n_d is nodes_per_depth_level
    """
    For each depth level:
    For each parent in that level:
    for each of its children:
        run the checks function
        update the number of approvals of the parent
    if the parent has enough approvals:
        keep it in the tree (ie it should be considered a valid child in the depth level above)
    otherwise:
        prune it from the tree (ie: do not visit it)
    repeat"""
    #ensure all nodes are reset again to be in the tree
    reset_nodes(tree)

    #check that the tree meets all other necessary criteria
    checks = tree_checks(threshold, tree, n_d, depth)
    if checks == True:
        valid_tree = True

        responses_sum = 0
        for depth_level in range(depth, -1, -1):
            
            depth_level_counter = 0
            for parent in tree[depth_level]:
                parent_approval_counter = 0
                
                #print(parent.in_tree)
                if parent.in_tree == True:
                    children = tree[depth_level][parent]['children']
                    if children:
                        for child in children:
                            
                            response = child.response
                            parent_approval_counter += response
                            responses_sum += response
                            #print(f"parent approval counter in loop {parent_approval_counter}")
                    
                        #print(f"parent approval counter out of loop {parent_approval_counter}")

                        if parent_approval_counter <= n_d[depth_level-1]*threshold:
                            #print(f"parent approval counter {parent_approval_counter}, nd*t {n_d[depth_level-1]*threshold}")
                            parent.in_tree = False
                            #print(f"Depth {depth_level}, Response {child.response}, Parent in tree {parent.in_tree}")
                        else:
                            depth_level_counter += 1
                            parent.in_tree = True #TODO: should i do this? or is it dangerous?
        
    else:
        valid_tree = False
        responses_sum = None
        
    return valid_tree, responses_sum

        #print(depth_level_counter) #this will output 0 or 1. O if parent does not stay in the tree, and 1 if it does.
        #print(parent_approval_counter) #this will output the sum the responses of the children of the root (at that last depth level).
        #TODO: CLASSIFY RESPONSE SUM WITH THRESHOLD 
        
    

