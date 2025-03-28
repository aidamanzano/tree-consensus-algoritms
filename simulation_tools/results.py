#set some thresholds for accept, unknown and reject 
#compare total weight and then classify accordingly 





def results(agent_list, class_category, claim_value):
    '''precision, recall and accuracy per class.
    class_category: -1 (False), 0 (Unknown), 1 (True)
    claim_value: 1, -1, 0'''
    True_Positives = 0
    True_Negatives = 0
    False_Positives = 0
    False_Negatives = 0

    #TODO: this needs to be changed, i need to check class_category against claim_value.
    #TODO: also algorithm_output is currently not being assigned anywhere.
    for agent in agent_list:
        if agent.algorithm_output == class_category and agent.claim == claim_value:
            True_Positives += 1
        if agent.algorithm_output != class_category and agent.claim == claim_value:
            False_Positives += 1
        if agent.algorithm_output == class_category and agent.claim != claim_value:
            False_Negatives += 1
        if agent.algorithm_output != class_category and agent.claim != claim_value:
            True_Negatives += 1

    class_precision = True_Positives / (True_Positives + False_Positives)
    class_recall = True_Positives / (True_Positives + False_Negatives)
    class_accuracy = True_Positives / (True_Positives + True_Negatives + False_Positives + False_Negatives)
    return class_precision, class_recall, class_accuracy