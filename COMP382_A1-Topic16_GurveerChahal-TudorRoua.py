# Defining the set of states for two NFAs
states1 = {'q1', 'q2', 'q3', 'q4'}
states2 = {'s1', 's2', 's3', 's4'}

# Defining the alphabet set for two NFAs
alphabet1 = {'a', 'b', 'c'}
alphabet2 = {'x', 'y', 'z'}

# Defining dictionaries of the transitions in two NFAs
transitions1 = {
    ('q1', 'a'): {'q1'},
    ('q1', 'b'): {'q1', 'q2'},
    ('q1', 'c'): {'q2'},
    ('q2', 'a'): {'q3'},
    ('q2', 'b'): {'q3'},
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

# Defining the start and accept states of two NFAs
start1 = 'q1'
start2 = 's1'
accept1 = {'q4'}
accept2 = {'s3', 's4'}

class NFA:
    def __init__(self, states, alphabet, transitions, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accept = accept
    
    #def checkWord():
        

    # The concatenate method returns the NFA produced by concatenating the first NFA to the second
    def concatenate(NFA1, NFA2):
        #states =
        #alphabet =
        #transitions = 
        start = NFA1.start
        accept = NFA2.accept

        #return(NFA(states, alphabet, transitions, start, accept))


N1 = NFA(states1, alphabet1, transitions1, start1, end1)

N2 = NFA(states2, alphabet2, transitions2, start2, end2)

#N = NFA.concatenate(N1, N2)

        
