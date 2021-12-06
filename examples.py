"""
1D CA examples...
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from CA import Grid, Rule

def plotAllRules():
    """ Plot all 1D CA as per Wolfram convention """
    
    # Generate all 256 nearest-neighbour 1D rules (Wolfram convention)
    rules = []
    for i in range(256):
        # Rule i in 8 bit binary format
        binary = f'{i:08b}'
        rule = {'111': binary[0], '110': binary[1], 
                '101': binary[2], '100': binary[3],
                '011': binary[4], '010': binary[5], 
                '001': binary[6], '000': binary[7]}
        rules.append(Rule(rule = rule))

    # Number of generations that the state shall evolve
    num_generations = 1000

    # Plot the result of each rule
    for j in range(256):
        grid = Grid()
        grid.initialise()
        i = 0
        while (i := i + 1) < num_generations:
            grid.evolve(rules[j])
        print(f'Rule: {j}')
        grid.plot()

def plotParticularRule(rule_num = 30):
    """ Plot a particular rule """

    # Generate all 256 nearest-neighbour 1D rules (Wolfram convention)
    rules = []
    for i in range(256):
        # Rule i in 8 bit binary format
        binary = f'{i:08b}'
        rule = {'111': binary[0], '110': binary[1], 
                '101': binary[2], '100': binary[3],
                '011': binary[4], '010': binary[5], 
                '001': binary[6], '000': binary[7]}
        rules.append(Rule(rule = rule))

    # Initialise the grid
    grid = Grid()
    grid.initialise()

    # Number of generations that the state shall evolve
    num_generations = 1000

    # Evolve
    while (i := i + 1) < num_generations:
        grid.evolve(rules[rule_num])
    grid.plot()

def plotRandomRulePerGeneration():
    """ Plot a 1D CA that proceeds with a random rule at each generation """

    # Generate all 256 nearest-neighbour 1D rules (Wolfram convention)
    rules = []
    for i in range(256):
        # Rule i in 8 bit binary format
        binary = f'{i:08b}'
        rule = {'111': binary[0], '110': binary[1], 
                '101': binary[2], '100': binary[3],
                '011': binary[4], '010': binary[5], 
                '001': binary[6], '000': binary[7]}
        rules.append(Rule(rule = rule))

    # Number of generations that the state shall evolve
    num_generations = 1000

    # Apply random rules at each stage of the evolution
    grid = Grid()
    grid.initialise()
    i = 0
    while (i := i + 1) < num_generations:
        r = np.random.randint(0,256)
        grid.evolve(rules[r])
    grid.plot()


def plotRandomRuleTwoStep():
    """ Plot random CA rule with two-step history (specified with 64 parameters) """
    
    # Initialise the grid
    grid = Grid(history = 2)
    grid.initialise()

    # Number of generations that the state shall evolve
    num_generations = 1000

    ## Random rule
    test_rule = {}
    for i in range(64):
        test_rule[f'{i:06b}'] = np.random.randint(0,2)
    rule = Rule(rule = test_rule)

    # Evolve
    while (i := i + 1) < num_generations:
        grid.evolve(rule)
    grid.plot()



while True:
    plotRandomRuleTwoStep()
#plotAllRules()
#plotParticularRule()
#plotRandomRulePerGeneration()