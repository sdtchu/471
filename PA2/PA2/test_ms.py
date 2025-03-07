import sys
import time
import signal
from typing import Callable
from constraint import BacktrackingSolver, RecursiveBacktrackingSolver, MinConflictsSolver
import wrapt_timeout_decorator as t
from custom_min_conflict_solver import CustomMinConflictsSolver
from math import sqrt
# load the CSP problems for magic squares
from ms import MS
from helpers import *

#SIGALRM is only usable on a unix platform
signal.signal(signal.SIGALRM, timeout)


# test a CSP problem
def tester(constraint_problem:Callable, sizes:list, max_time:int,sum_list:int):
    """ show the time it takes to solve a constraint problem
        varying sizes using different solvers. """
    
    solvers = [BacktrackingSolver, CustomMinConflictsSolver]

    TIMEOUT="Timeout" # function timed out
    FAILURE="Failure" # no solutions found
    SUCCESS="Success" # solutions were found

    for n in sizes:
        for magic_sum in sum_list:
            print(f"Size {n} with sum = {magic_sum}")
            for s in solvers:
                solver_type=s.__name__
                start = time.time()
                solution_list =[]
                incorrect=0
                duplicates=0
                try:
                    # set the alarm for max_time seconds
                    signal.alarm(max_time)
                    solution_list =  constraint_problem(n, magic_sum,s())
                    # clear alarm since it didn't go off
                    signal.alarm(0)
                    
                    if solution_list is None or len(solution_list)==0:
                        result=FAILURE
                        len_sol=0
                    else:
                        
                        result=SUCCESS
                        len_sol=len(solution_list)
                        duplicates=count_duplicates(solution_list)
                        for s in solution_list:
                            if ms_check(s,magic_sum) is False:
                                incorrect+=1
                                print("invalid: ", ms_str(s))
                except TimeoutException:
                    result=TIMEOUT
                    len_sol=0
                elapsed = time.time() - start
                print(f"\t Solver: {solver_type} Result: {result} Time Elapsed: {elapsed:.2f} Solutions: {len_sol}")
                if incorrect>0:
                    print(f"\t\t{len_sol-incorrect}/{len_sol} correct")
                if duplicates>0:
                    print(f"\t\t {duplicates} duplicates")
                

    
if __name__ == "__main__":
    # default timeout in seconds
    timeout = 30
    if len(sys.argv) > 1:
        timeout = int(sys.argv[1])

    # test the magic squares problem
    print("\nMagic Squares")
    sizes=[2,3,4]
    sum_list=[n * (n*n + 1) / 2 for n in sizes]
    tester(MS, sizes, timeout,sum_list)
         
