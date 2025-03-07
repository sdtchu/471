""" starter file for pa1: dogcat """

"""
*** DISCLAIMER FROM THE AUTHOR ***
I did have to install numpy to my python environment. I have
attached and submitted the virtual environment directory for
your convenience.
"""

import search       # AIMA module for search problem
import gzip         # read from a gzip'd file

# file name for the dictionary, with one word per line.  Each line
# will have a word followed by a tab followed by a number, e.g.
#   and     0.07358445
#   for     0.18200336

dict_file = "words34.txt.gz"

# dictionary is a dict to hold legal 3 and 4 letter words with their
# frequencies based on a sample of a large text corpus. The dict's
# keys are the words and its values are their frequencies

# load words into the dictionary dict
dictionary = {}
for line in gzip.open(dict_file, 'rt'):
    word, n = line.strip().split('\t')
    n = float(n)
    dictionary[word] = n

class DC(search.Problem):
    """DC is a subclass of the AIMA search files's Problem class. Its init
       method takes three arguments: the initial word, goal word, and cost method.
       A state is represented as a lowercase string of three or four
       ascii characters.  Both the initial and goal states must be
       words of the same length and they must be in the dict
       dictionary. The cost argument specifies how to measure the
       cost of an action and can be 'steps', 'scrabble' or 'frequency'
       """

    def __init__(self, initial='dog', goal='cat', cost='steps'):
        # set instance attributes ...
        self.initial = initial.lower()
        self.goal = goal.lower() 
        self.cost = cost
        # make sure arguments are legal, raising an error if any are bad.
        if (len(initial) != len(goal) or
            initial not in dictionary or
            goal not in dictionary):
            raise ValueError("Bad initial or goal state")
        
        if (cost != 'steps' and cost != 'scrabble' and cost != 'frequency'):
            raise ValueError("Bad cost method")

    def actions(self, state):
        """ Given a state (i.e., a word), return a list or iterator of
        all possible next actions.  An action is defined by position
        in the word and a character to put in that position.  But the
        result must be a legal word, i.e., in our dictionary, and it
        should not be the same as the state, i.e., don't replace a
        character with the same character """

        word_test = ""

        # [ letter, index ]
        possible_actions = []

        # all possible letters
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for letter in alpha:
            # iterate through state
            for i in range(len(state)):
                if letter != state[i]:
                    word_test = state
                    # Puts letter at indexed location
                    word_test = word_test[:i] + letter + word_test[i + 1:]
                    # if word is in dictionary
                    if word_test in dictionary:
                        # append letter and index to possible actions
                        possible_actions.append([letter, i])
        return possible_actions
    
    def result(self, state, action):
        """ takes a state and an action and returns a new state """
        new_word = state
        index = action[1]
        new_let = action[0]
        new_word = new_word[:index] + new_let + new_word[index + 1:]
        return new_word


    def goal_test(self, state):
        """ returns True iff state is a goal state for this problem instance """ 
        if (state == self.goal):
            return True
        return False

    def path_cost(self, c, state1, action, state2):
        """ Returns the cost to get to state2 by applying action in
        state1 given that c is the cost to get up to state1. For the 
        the dc problem, you will have to check what
        cost metric (self.cost) is being used for this problem instance,
        i.e., is it steps, scrabble or frequency """
        total_cost = c
        
        if (self.cost == 'steps'):
            # Steps is just the number of steps in the sequence from state1 to state2
            total_cost += 1
        elif (self.cost == 'scrabble'):
            cost1_replace = "aeioulnstr"
            cost2_use = "dg"
            cost3_replace = "bcmp"
            cost4_use = "fhvwy"
            cost5_replace = "k"
            cost6_use = "jx"
            cost7_replace = "z"

            if action[0] in cost1_replace:
                total_cost += 1
            if action[0] in cost2_use:
                total_cost += 2
            if action[0] in cost3_replace:
                total_cost += 3
            if action[0] in cost4_use:
                total_cost += 4
            if action[0] in cost5_replace:
                total_cost += 5
            if action[0] in cost6_use:
                total_cost += 6
            if action[0] in cost7_replace:
                total_cost += 7 
        elif (self.cost == 'frequency'):
            if state2 in dictionary:
                total_cost += (1 + int(dictionary[state2]))
        else:
            raise ValueError("Bad Cost Method")
        
        return total_cost

    def __repr__(self):
        """" return a suitable string to represent this problem instance """
        return f'{self.initial}, {self.goal}, {self.cost}'

    def h(self, node):
        """Heuristic: returns an estimate of the cost to get from the
        state of the node to the goal state. The heuristic's value should
        depend on the Problem's cost parameter, self.cost (i.e., steps, scrabble
        or frequency), as this will effect the estimate cost to get to
        the nearest goal. """
        est_cost = 0
        state = node.state
        cost1_replace = "aeioulnstr"
        cost2_use = "dg"
        cost3_replace = "bcmp"
        cost4_use = "fhvwy"
        cost5_replace = "k"
        cost6_use = "jx"
        cost7_replace = "z"


        if (self.cost == 'steps'):
            for i in range(len(state)):
                if state[i] != self.goal[i]:
                    est_cost += 1
            return est_cost
        elif (self.cost == 'scrabble'):
            for i in range(len(state)):
                if state[i] != self.goal[i]:
                   est_cost += 1 
            return est_cost
        elif (self.cost == 'frequency'):
            for i in range(len(state)):
                if state[i] != self.goal[i]:
                    est_cost += 1
            return est_cost
        else:
            raise ValueError("Bad Cost Method")
        
