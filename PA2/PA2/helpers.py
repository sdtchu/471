'''
some helper functions for testing; you don't need to modify
'''

from math import sqrt
from collections import Counter
from typing import List, Dict

# Function to count duplicate dictionaries
def count_duplicates(dict_list: List[Dict]) -> int:
    # Convert each dictionary to a frozenset of tuples (or you can convert to a sorted tuple)
    dict_as_tuples = [tuple(sorted(d.items())) for d in dict_list]
    
    # Count the occurrences of each dictionary
    duplicates_count = Counter(dict_as_tuples)
    
    # Sum the counts of all dictionaries that have duplicates
    duplicate_entries = sum(count for count in duplicates_count.values() if count > 1)
    
    return duplicate_entries

# support for a simple timeout mechanism
class TimeoutException(Exception): 
    pass 

def timeout(signum, frame):
    raise TimeoutException('Timed Out')

def ms_check(s:dict,magic_sum:int)->bool:
    """ Check magic square solution """
    if type(s) is not dict:
        # if not a potential solution, just return False
        return False
    size = int(sqrt(len(s)))
    #magic_sum = size * (size*size + 1) / 2
    # check all numbers different
    if len(set(s)) != len(s):
        return False
    # check rows and columns sum to magic_sum
    for i in range(size):
        if sum([s[i*size+j] for j in range(size)]) != magic_sum:
            return False
        if sum([s[i+j*size] for j in range(size)]) != magic_sum:
            return False
    # check if diagonals sum to magic_sum
    if sum([s[i*(size+1)] for i in range(size)]) != magic_sum:
        return False
    if sum([s[i*(size-1)+size-1] for i in range(size)]) != magic_sum:
        return False
    return True

def ms_str(d:dict)->str:
    """ returns a magic square solution dictionary d in a more readable form. """
    if not type(d) is dict:
        return
    size = sqrt(len(d))
    output=""
    for i in range(len(d)):
        if i%size == 0:
            output+="\n"
        output+="%3d" % d[i]
    output+="\n"
    return output