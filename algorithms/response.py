from components.agent import Agent

def response(child:Agent, parent:Agent):
    response = parent.claim * child.response
    return response
    #TODO: currently returns a float. Should we add a line in here to say if the value is less than 1*threshold then output is 0, otherwise it is 1?