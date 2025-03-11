#set some thresholds for accept, unknown and reject 
#compare total weight and then classify accordingly 

#def results(agent_list:list):
'''precision, recall and accuracy per class.
class_category: True, False, Unknown
claim_value: 1, -1, 0'''

def results(agent_list, class_category, claim_value):
    True_Positives = 0
    True_Negatives = 0
    False_Positives = 0
    False_Negatives = 0
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