from components.agent import Agent
from response import response

#TODO: should the threshold be the same in terms of approval percentage and number of approvals in the tree?
def checks(parent:Agent, child:Agent, threshold:float, tree:dict, named_agents:list, nodes_per_depth:list, depth_level:int)-> bool:
    #do some checks
    '''if:
    child approves parent :ie: if the child's approval confidence is above a threshold
    and
    parent named enough children
    and 
    child is not in named_agents
    and 
    all named children are distinct

    return True
    else:
    return False
    '''
    assert parent == child.parent
    if (
        response(child, child.parent) >= threshold
        and
        len(tree[depth_level][parent]['children']) >= nodes_per_depth[depth_level] * threshold
        and
        child not in named_agents
        and
        len(set(named_agents)) == len(named_agents)
    ):
        return True
    else:
        return False


def TPoP(prover:Agent, tree:dict, threshold:float)-> bool:
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

    
