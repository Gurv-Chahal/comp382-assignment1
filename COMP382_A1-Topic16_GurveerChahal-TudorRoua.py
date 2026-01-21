

# Defining the set of states for two NFAs (set of nodes)
states1 = {'q1', 'q2', 'q3', 'q4'}
states2 = {'s1', 's2', 's3', 's4'}

# Defining the alphabet set for two NFAs (acceptable input chars)
alphabet1 = {'a', 'b', 'c'}
alphabet2 = {'x', 'y', 'z'}

# Defining dictionaries of the transitions in two NFAs (edges)
transitions1 = {
    # (node, input): (next node)
    ('q1', 'a'): {'q1'},
    ('q1', 'b'): {'q1', 'q2'},
    ('q1', 'c'): {'q2'},
    ('q2', 'a'): {'q3'},
    ('q2', 'b'): {'q3'},
    # (node, epsilon): (next node)
    ('q2', None): {'q3'},
    ('q3', 'a'): {'q3', 'q4'},
    ('q3', 'c'): {'q3'}
}

transitions2 = {
    ('s1', 'y'): {'s1'},
    ('s1', 'z'): {'s2'},
    ('s1', None): {'s2'},
    ('s2', 'x'): {'s2', 's3'},
    ('s2', 'y'): {'s2', 's4'},
    ('s3', 'z'): {'s4'},
    ('s3', None): {'s4'},
    ('s4', 'x'): {'s3'}
}

# Defining the start and accept states of two NFAs (starting and final nodes)
start1 = 'q1'
start2 = 's1'

accept1 = {'q4'}
accept2 = {'s3', 's4'}


# 1. implementing a class
class NFA:

    # 3. constructor - initialize NFA states
    def __init__(self, states, alphabet, transitions, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accept = accept

    # 2. the concatenate method returns the NFA produced by concatenating the first NFA to the second
    def concatenate(NFA1, NFA2):

        # going to union all fields from both NFAs to concatenate each one

        # NFA1 states (Union) NFA2 states
        states = NFA1.states.union(NFA2.states)
        alphabet = NFA1.alphabet.union(NFA2.alphabet)

        # for transitions we don't want to use union because there will be conflicting
        # keys in the dict, that is why instead we will have to use a different method
        transitions = {}

        # NFA1 - iterate over each (key,value) pair
        for key, value in NFA1.transitions.items():
            # store it in inside transitions
            transitions[key] = value.copy()

        # same thing for NFA2
        for key , value in NFA2.transitions.items():

            # if theres a conflict then add the value to transitions using the same key
            if key in transitions:
                # take each value out of values
                for values in value:
                    # add it directly to the key inside transitions dict
                    transitions[key].add(values)

            # otherwise if the key doesn't exist then add the key-value normally
            if key not in transitions:
                transitions[key] = value.copy()

        # link accept state to the
        # start state of the second graph by using an epsilon (None)
        for node in NFA1.accept:
            key = (node, None)
            transitions[key] = {NFA2.start}


        start = NFA1.start
        accept = NFA2.accept

        return NFA(states, alphabet, transitions, start, accept)


    # 4. check input words
    def checkWord(self, word):

        # we need to build this helper function so that when at a state
        # an epsilon (None) is checked for, otherwise no inputs will work correctly
        def checkIfEpsilon(state):

            # states discovered so far
            closure = {}
            closure[state] = 0

            # create a stack of states/nodes
            closureStack = [state]

            # explore every reachable state
            while len(closureStack) > 0:
                # pop off first state
                state = closureStack.pop(0)

                # look through transitions dict and get values for (state, none)
                # keys, which are next nodes epsilon reaches
                epsilonStates = self.transitions.get((state, None), set())

                # any nodes that epsilon points to add to the stack
                for next in epsilonStates:
                    if next not in closure:
                        closure[next] = 0
                        closureStack.append(next)

            # return all nodes that can be reached by epsilon in graph in a set
            return set(closure.keys())



        # from start node save all nodes that can be reached by epsilon
        currentStates = checkIfEpsilon(self.start)

        for ch in word:

            if ch not in self.alphabet:
                return False

            future = set()

            # iterate over each node that can be reached by epsilon in the beginning
            for state in currentStates:
                # return value of (node, char) if exists which is a state
                for next in self.transitions.get((state, ch), set()):
                    # add value to set
                    future.add(next)

            newSet = set()

            # iterate over every state from nodes that can be reached by epsilon
            for state in future:
                # check if epsilon exists fromn that node
                epsStates = checkIfEpsilon(state)
                # add nodes that can be reached by epsilon into a new set
                for s in epsStates:
                    newSet.add(s)

            # update
            currentStates = newSet

        # iterate through each node
        for state in currentStates:
            # if the node is a final node (accept node)
            if state in self.accept:
                return True
        return False


if __name__ == "__main__":

    # create n1, n2, then concatenate using N
    N1 = NFA(states1, alphabet1, transitions1, start1, accept1)
    N2 = NFA(states2, alphabet2, transitions2, start2, accept2)
    N  = NFA.concatenate(N1, N2)

    tests = [
        ("N1", N1, "ca"),
        ("N1", N1, "ba"),
        ("N1", N1, "a"),
        ("N2", N2, "x"),
        ("N2", N2, "y"),
        ("N2", N2, "z"),
        ("N",  N,  "cax"),
        ("N",  N,  "ca"),
        ("N",  N,  "x"),
    ]

    # print
    for name, machine, word in tests:
        print(f"{name}.checkWord('{word}') -> {machine.checkWord(word)}")
