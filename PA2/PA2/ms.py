"""
Complete the ms() program so that it will try to find a magic square
of of size n using a CSP solver.  

You will need to install two packages with pip: python-constraint and
timeout-decorator. On gl, you can install packages using the
user flag:
  pip install --user python-constraint
  pip install --user wrapt-timeout-decorator
"""

#  Seth Chu LI22854

import constraint as c
import wrapt_timeout_decorator as t
import time

def init_positions(n:int):
    positions = {}
    horiz = []
    vert = []
    diag = []
    
    # horizontal group positions
    for i in range(n):
        horiz.append([i * n + j for j in range(n)])
    
    # vertical group positions
    for i in range(n):
        vert.append([j * n + i for j in range(n)])
    
    # upper left to bottom right diagonal
    diag.append([i * (n + 1) for i in range(n)])
    # upper right to bottom left diagonal
    diag.append([(i + 1) * (n - 1) for i in range(n)])

    positions = {"horizontals": horiz, "verticals": vert, "diagonals": diag}
    
    return positions

def init_domain(n:int):
    i = 1
    domain = []
    while (i <= n**2):
        domain.append(i)
        i += 1
    return domain

def MS(n:int, magic_sum:int, solver:c.Solver)->list:
    """ 
    Solve a magic squares problem for a nxn grid and given
    magic_sum or computing a default magic sum if none is given using
    the given solver 
    returns a list of dicts, where each dict is a valid solution. A valid solution
    is a dict of len n, where the keys are ints in (0,1,,,n^2-1), and the values are also
    ints in (1,,,n^2), without repetition. 
    """
    positions = []
    domains = []
    solutions = []
    

    # if solver is not given
    if solver is None:
        solver = c.Problem() 

    # init problem
    prob = c.Problem(solver)
    # add constraint so that each solution needs the exact sum to be the magic sum
    prob.addConstraint(c.ExactSumConstraint(magic_sum))
    prob.addConstraint(c.AllDifferentConstraint())
    
    # the size of the square
    positions = init_positions(n=n)
    # the possible numbers the square can be
    domain = init_domain(n=n)

    for v in positions.values():
        for group in v:
            print(group)
            prob.addVariables(group, domain)
     
            for sln in prob.getSolutions():
                solutions.append(sln)

    return solutions 










