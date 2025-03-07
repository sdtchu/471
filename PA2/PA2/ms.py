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


def MS(n:int, magic_sum:int, solver:c.Solver)->list:
    """ 
    Solve a magic squares problem for a nxn grid and given
    magic_sum or computing a default magic sum if none is given using
    the given solver 
    returns a list of dicts, where each dict is a valid solution. A valid solution
    is a dict of len n, where the keys are ints in (0,1,,,n^2-1), and the values are also
    ints in (1,,,n^2), without repetition. 
    """
    solver.addConstraint(c.ExactSumConstraint(n))
    solver.getSolution()
    pass