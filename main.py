"""
state: [M,C,B]
initial: [M,C,1]
goal: [0,0,0]

"""

M = 3
C = 3

class State():
    def __init__(self, missionary, cannibal, boat):
        self.m = missionary
        self.c = cannibal
        self.b = boat
        self.prev = None
        self.move = ''

    def __eq__(self, other):
        return self.m == other.m and \
               self.c == other.c and \
               self.b == other.b

    def __str__(self):

        return "{}\n[{},{},{}]".format(self.move, self.m, self.c, self.b)

    def is_goal(self):
        if self.m == 0 and self.c == 0 and self.b == 0:
            return True
        return False


def isValid(state):
    if (state.m >= state.c) and ((M - state.m) >= (C - state.c)) or state.m == M or state.m == 0:
        return True
    return False

init = State(M, C, 1)
init.prev = init
goal = State(0, 0, 0)

frindge = []
frindge.append(init)

visited = []


n = 0
while frindge:

    n = n + 1
    state = frindge.pop()

    if state in visited:
        continue
    else:
        visited.append(state)

    if state.is_goal():
        print('Find the goal')
        result = []
        while state != init:
            result.append(state)
            state = state.prev
        result.append(init)
        for item in reversed(result):
            print(item)
        break



    if state.b == 1:
        # M - 1
        if state.m >= 1:
            newState = State(state.m - 1, state.c, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '1 Missionary to opposite'
                frindge.append(newState)

        # M - 2
        if state.m >= 2:
            newState = State(state.m - 2, state.c, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '2 Missionaries to opposite'
                frindge.append(newState)

        # C - 1
        if state.c >= 1:
            newState = State(state.m, state.c - 1, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '1 Cannibal to opposite'
                frindge.append(newState)

        # C - 2
        if state.c >= 2:
            newState = State(state.m, state.c - 2, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '2 Cannibals to opposite'
                frindge.append(newState)

        # M - 1 and C - 1
        if state.m >= 1 and state.c >= 1:
            newState = State(state.m - 1, state.c - 1, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '1 Missionary and 1 Cannibal to opposite'
                frindge.append(newState)

    elif state.b == 0:
        # M + 1
        if state.m < M:
            newState = State(state.m + 1, state.c, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '1 Missionary back to this side'
                frindge.append(newState)

        # M + 2
        if state.m <= M - 2:
            newState = State(state.m - 2, state.c, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '2 Missionaries back to this side'
                frindge.append(newState)

        # C + 1
        if state.c < C:
            newState = State(state.m, state.c + 1, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '1 Cannibal back to this side'
                frindge.append(newState)

        # C + 2
        if state.c <= C - 2:
            newState = State(state.m, state.c + 2, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '2 Cannibals back to this side'
                frindge.append(newState)

        # M + 1 and C + 1
        if state.m < M and state.c < C:
            newState = State(state.m + 1, state.c + 1, 1 - state.b)
            if isValid(state):
                newState.prev = state
                newState.move = '1 Missionary and 1 Cannibal back to this side'
                frindge.append(newState)