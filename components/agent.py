
from typing import Optional, List
import uuid

import numpy as np
class Agent:
    """
    environment_bounds: List[[min_x, max_x], [min_y, max_y]]
    """
    def __init__(self, p_response:List, p_claim, environment_bounds: List, parent: Optional["Agent"] = None):
        self.parent = parent
        self.child = None
        self.neighbours = None

        self.range_of_sight = 1.0
        #default to not-pruned. 
        self.pruned = False

        self.algorithm_output = None

        self.min_x = environment_bounds[0][0]
        self.max_x = environment_bounds[0][1]
        self.min_y = environment_bounds[1][0]
        self.max_y = environment_bounds[1][1]
        
        self.x_position = self.generate_position(self.min_x, self.max_x)
        self.y_position = self.generate_position(self.min_y, self.max_y)

        self.agent_id = self.generate_unique_id()

        self.response = self.generate_statement(p_response, choices = [True, False, None])
        self.claim = self.generate_statement(p_claim, choices = [True, False, None])

    @staticmethod
    def generate_position(min:float, max:float):        
        return float(np.random.uniform(low=min, high=max))
    
    @staticmethod
    def generate_unique_id():
        return uuid.uuid4()
    
    @staticmethod
    def generate_statement(prob_vector:list, choices):
        """p_response = [p_approval, p_rejection, p_ignore]
            p_claim = [p_true_claim, p_false_claim, p_unverifiable_claim]"""

        rng = np.random.default_rng()

        # Draw a random choice based on probabilities
        output = rng.choice(choices, p=prob_vector)
        return output

