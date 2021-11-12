"""
One-dimensional cellular automata
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class Grid:
    """
    Object that implements the full CA state over time
    """

    def __init__(self):
        self.dimension = 1
        self.generation = 0
        self.size = 100
        self.state = np.zeros((1, self.size), dtype=int)

    def initialise(self, IC = None):
        """
        Initial state (default: one live cell in centre)
        """
        if IC == None:
            self.state[0, [self.size // 2]] = 1
        else:
            self.state = IC

    def evolve(self, rule):
        """
        Take the state of the current generation and update to next generation
        according to some rule (input)
        """

        update = rule.apply(self.state[self.generation,:])
        self.state = np.concatenate((self.state, [update]), axis=0)
        self.generation += 1

    def plot(self):
        """
        Plot full CA state
        """
        plt.imshow(self.state, cmap='gist_gray') #,interpolation='gaussian')
        plt.show()


class Rule:
    """
    Object that implements a 1D CA rule
    """

    def __init__(self, rule):
        # Check a valid rule is supplied
        if isinstance(rule, dict):
            self.rule = rule
        else:
            raise TypeError('No valid rule supplied')


    def apply(self, current_state):
        """
        Apply the given 1D CA rule (dict) to a state (current_state)
        """

        size = current_state.size
        new_state = np.zeros(size, dtype=int)
        for i, element in enumerate(current_state):
            # New state applies rule to old state including periodic boundary conditions
            new_state[i] = self.rule['{0}{1}{2}'.format(current_state[i-1],
                                                        current_state[i],
                                                        (current_state[i+1] if i < size - 1 else current_state[0]))]

        return new_state


# Generate all 256 nearest-neighbour 1D rules (Wolfram convention)
rules = []
for i in range(256):
    # Rule i in 8 bit binary format
    binary = f'{i:08b}'
    rule = {'111': binary[0], '110': binary[1], '101': binary[2], '100': binary[3], '011': binary[4],
            '010': binary[5], '001': binary[6], '000': binary[7]}
    rules.append(Rule(rule = rule))

# Initialise the grid
grid = Grid()
grid.initialise()

# Number of generations that the state shall evolve
num_generations = 200

"""
# Update grids with a rule
for j in range(256):
    grid = Grid()
    grid.initialise()
    i = 0
    while (i := i + 1) < num_generations:
        grid.evolve(rules[j])
    print(j)
    plt.clf()
    grid.plot()
"""

i = 0

while True:
    grid = Grid()
    grid.initialise()
    i = 0
    while (i := i + 1) < num_generations:
        r = np.random.randint(0,256)
        grid.evolve(rules[r])
    plt.clf()
    grid.plot()