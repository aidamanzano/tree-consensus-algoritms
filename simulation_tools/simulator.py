from algorithms.recurse_tree import recursive_build_tree
from algorithms.tpop import TPoP
import pandas as pd


def simulator(p_response, p_claim, dimensions, threshold, agents, N) -> pd.DataFrame:
    '''
    dimensions = [depth, n_d]
    p_response = [p_accept, p_reject, p_ignore]
    p_claim = [p_true, p_false, p_unverifiable]
    agents = [agent_list, agent_dict]
    '''
    
    depth, n_d = dimensions
    p_accept, p_reject, p_ignore = p_response
    p_true, p_false, p_unverifiable = p_claim
    agents_list, agents_dict = agents

    assert len(agents_dict) == N == len(agents_list)

    data = []
    for i in range(N):
        prover = agents_list[i]
        starting_dict = { 0: {prover: {'children': [],
                                'instance': 'AgentInstance',
                                'parent': None}}}
        tree = recursive_build_tree(starting_dict, agents_dict, 0, depth, n_d= n_d)
        valid_tree, responses_sum = TPoP(tree, n_d=n_d, depth = depth, threshold = threshold)
        
        #data.append((p_accept, p_reject, p_ignore, p_true, p_false, p_unverifiable, valid_tree, responses_sum))
        data.append({
            'p_accept': p_accept,
            'p_reject': p_reject,
            'p_ignore': p_ignore,
            'p_true': p_true,
            'p_false': p_false,
            'p_unverifiable': p_unverifiable,
            'valid_tree': valid_tree,
            'responses_sum': responses_sum
        })
    df = pd.DataFrame(data)
    #df = pd.DataFrame(data, columns = ['p_accept', 'p_reject', 'p_ignore', 'p_true', 'p_false', 'p_unverifiable', 'valid_tree', 'responses_sum'])
    return df