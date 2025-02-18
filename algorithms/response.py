from components.agent import Agent

def response(child:Agent, parent:Agent):
    response = parent.claim * child.response
    return response