import time

""" The board typically has three conditions :
1. No marble in the hole ( represented as '0' in the board ) 
2. Marble in the hole ( represented as '1' in the board )
3. No holes in the board ( represented as '-1' in the board )
"""

""" Global variables required declared from here"""

""" Stack used to store the states of the game"""
Stack = []

""" Variable to store initial time"""
time1 = 0

""" This list stores the path from initial state to goal state"""
path = []

""" Flag to get to know the goal state"""
goal = False

""" Variable to keep track of the number of nodes expanded"""
number = 0

""" Reverse the given order of the path"""
reverse = []

""" Goal Node state"""
goalNode = [[-1, -1, 0, 0, 0, -1, -1], [-1, -1, 0, 0, 0, -1, -1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, -1, 0, 0, 0, -1, -1], [-1, -1, 0, 0, 0, -1, -1]]

""" Path representation"""
ref = [[-1, -1, 0, 1, 2, -1, -1], [-1, -1, 3, 4, 5, -1, -1], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [-1, -1, 27, 28, 29, -1, -1], [-1, -1, 30, 31, 32, -1, -1]]


""" Sample states declared here for testing
    Below are the different use cases defined respectively
    Uncomment each of the use cases while commenting the other use cases to see the respective behavior"""

"""========================================================================================================================================="""    
"""Case 1: This is given in the assignment as an example"""
a = [[-1,-1,0,0,0,-1,-1],[-1,-1,0,1,0,-1,-1],[0,0,1,1,1,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]

"""Case 2: Another initial state for whom the goal state exists"""
#a = [[-1,-1,0,0,0,-1,-1],[-1,-1,0,1,0,-1,-1],[0,0,0,1,0,0,0],[0,1,1,1,1,1,0],[0,0,0,1,0,0,0],[-1,-1,0,1,0,-1,-1],[-1,-1,0,0,0,-1,-1]]

"""Case 3: Another initial state for whom the goal state exists"""
#a = [[-1, -1, 1, 1, 1, -1, -1], [-1, -1, 1, 1, 1, -1, -1], [0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [-1, -1, 0, 0, 0, -1, -1], [-1, -1, 0, 0, 0, -1, -1]]

"""Case 4: Negative Test Case to test the result of board reaching the end state without reaching the goal for the given state or no pegs in the board in the given state"""
#a = [[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]
"""========================================================================================================================================="""
    

""" Control starts from here"""
def main():
    global time1
    time1 = time.time()
    iterativeDeepeningSearch(a)
    getPath(path, goalNode)

    
""" This method is to check if the state is a goal state or not"""
def goalReached(a):
    count = 0
    for i in xrange(7):
        for j in xrange(7):
            if a[i][j] == 0 or a[i][j] == -1:
                count = count + 1
    if count == 48 and a[3][3] == 1:
        return True
    return False

""" This method generates the possible children of a particular state. Here 'i' denotes 'row' and 'j' denotes 'column'"""
def generateChildren(a):
    children = []
    for i in xrange(7):
        for j in xrange(7):
            if a[i][j] == 1:
                
                """ To move right"""
                if j + 2 < 7 and a[i][j + 1] == 1 and a[i][j + 2] == 0:
                    b = map(list, a)
                    b[i][j + 2] = 1
                    b[i][j + 1] = 0
                    b[i][j] = 0
                    children.append(b)
                    
                """ To move left"""
                if j - 2 > 0 and a[i][j - 1] == 1 and a[i][j - 2] == 0:
                    c = map(list, a)
                    c[i][j - 2] = 1
                    c[i][j - 1] = 0
                    c[i][j] = 0
                    children.append(c)

                """ To move top"""
                if i - 2 > 0 and a[i - 1][j] == 1 and a[i - 2][j] == 0:
                    d = map(list, a)
                    d[i - 2][j] = 1
                    d[i - 1][j] = 0
                    d[i][j] = 0
                    children.append(d)

                """ To move down"""
                if i + 2 < 7 and a[i + 1][j] == 1 and a[i + 2][j] == 0:
                    e = map(list, a)
                    e[i + 2][j] = 1
                    e[i + 1][j] = 0
                    e[i][j] = 0
                    children.append(e)
    return children

""" This method is the depth limited search of the particular state given. For every state the depth is incremented recursively."""
def depthLimitedSearch(a, max_depth):
    children = None
    if max_depth == 0:
        return
    global goal
    global number
    global goalNode
    Stack.append(a)
    while len(Stack) != 0:
        node = Stack.pop()
        number = number + 1
        reach = goalReached(node)
        if reach == True:
            print 'There exists solution to this board'
            goal = True
            path.append(goalNode)
            return 
        if max_depth == 0:
            break
        else:
            child = generateChildren(node)
            for x in xrange(len(child)):
                children = generateChildren(child[x])
            if children==None:
                return None
            for x in xrange(len(child)):
                depthLimitedSearch(child[x], max_depth - 1)
                if goal == True:
                    break
        
        if goal == True:
                    path.append(node)
    return node   

""" This method is the iterative deepening search of the given initial state. Here the depthLimitedSearch is called everytime after the exhaustion of the particular depth"""
def iterativeDeepeningSearch(a):
    print 'Iterative DLS'
    Stack = []
    y = 0
    while True:
        print 'Iteration', y
        result = depthLimitedSearch(a, y)
        if y>0 and result==None:
            print 'There exists no solution to this board'
            break
        if goal == True:
            break
        y = y + 1
   
""" This method prints the final path to the goal state"""
def getPath(path, goalNode):
    for k in reversed(path):
        reverse.append(k)
  
    for k in xrange(len(reverse)):
        if k >= 1:
            a1 = [[k - l for k, l in zip(i, j) ] for i, j in zip(reverse[k - 1], reverse[k])]
            logicPrint(a1)
    print ''    
    print 'The number of nodes expanded', number
    time2 = time.time()
    print 'The running time is :', time2 - time1

""" This method prints the expected format of the output path"""
def logicPrint(a):
    global ref
    for i in xrange(7):
        for j in xrange(7):
            if a[i][j] == -1:
                if j >= 2 and a[i][j - 2] == 1 and a[i][j - 1] == 1:
                    print '(', ref[i][j - 2] , '->' , ref[i][j], ')' ,
                if j + 2 < 7 and a[i][j + 2] == 1 and a[i][j + 1] == 1:
                    print '(', ref[i][j + 2], '->', ref[i][j], ')',
                if i >= 2 and a[i - 1][j] == 1 and a[i - 2][j] == 1:
                    print '(', ref[i - 2][j], '->', ref[i][j], ')',
                if i + 2 < 7 and a[i + 1][j] == 1 and a[i + 2][j] == 1:
                    print '(', ref[i + 2][j], '->', ref[i][j], ')',
                
main()    
