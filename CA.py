"""
One-dimensional cellular automata
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


class Rule:
    """
    Object that implements a 1D CA rule
    """

    def __init__(self, rule: dict):

        # Check a valid rule is supplied
        if isinstance(rule, dict):
            self.rule = rule
            # Size of the past that influences the current automata state
            if len(rule) == 8:
                self.history = 1
            elif len(rule) == 64:
                self.history = 2
        else:
            raise TypeError('No valid rule supplied')


    def apply(self, current_state: list):
        """
        Apply the given 1D CA rule (dict) to a state (current_state)
        """

        size = (current_state.size if self.history == 1 else current_state[0].size)
        new_state = np.zeros(size, dtype=int)
        for i in range(size):

            if self.history == 1:
                # New state applies rule to old state including periodic boundary conditions
                new_state[i] = self.rule['{0}{1}{2}'.format(current_state[i-1],
                                                            current_state[i],
                                                            (current_state[i+1] if i < size - 1 else current_state[0]))]

            elif self.history == 2:
                new_state[i] = self.rule['{0}{1}{2}{3}{4}{5}'.format(current_state[0][i-1],
                                                            current_state[0][i],
                                                            (current_state[0][i+1] if i < size - 1 else current_state[0][0]),
                                                            current_state[1][i-1],
                                                            current_state[1][i],
                                                            (current_state[1][i+1] if i < size - 1 else current_state[1][0]))]        
        return new_state


class Grid:
    """
    Class that implements the full CA state over discrete time
    """

    def __init__(self, history = 1):
        self.history = history
        self.dimension = 1
        self.generation = 0
        self.size = 200
        self.state = np.zeros((1, self.size), dtype=int)

    def initialise(self, IC: list = None):
        """
        Initial state (default: one live cell in centre)
        """
        if isinstance(IC, list):
            if len(IC) == self.size:
                self.state = IC
            else:
                raise TypeError('Not a valid initial condition')
            raise TypeError('Not a valid initial condition')
        else:
            if self.history == 1:
                self.state[0, [self.size // 2]] = 1
            elif self.history == 2:
                self.state = np.zeros((2, self.size), dtype=int)
                self.state[0:2, [self.size // 2]] = 1

    def evolve(self, rule: Rule):
        """
        Take the state of the current generation and update to next generation
        according to some rule (input)
        """
        if self.history == 1:
            update = rule.apply(self.state[self.generation,:])
        elif self.history == 2:
            update = rule.apply(self.state[self.generation:self.generation+2,:])
        self.state = np.concatenate((self.state, [update]), axis=0)
        self.generation += 1

    def plot(self):
        """
        Plot full CA state
        """
        plt.clf()
        plt.imshow(self.state, cmap='gist_gray', aspect='equal')
        plt.show()


