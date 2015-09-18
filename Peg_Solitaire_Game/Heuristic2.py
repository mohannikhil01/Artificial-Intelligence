import heapq
import time

""" The board typically has three conditions :
1. No marble in the hole ( represented as '0' in the board ) 
2. Marble in the hole ( represented as '1' in the board )
3. No holes in the board ( represented as '-1' in the board )
"""

""" Global variables required declared from here"""


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


""" Path representation"""
ref = [[-1, -1, 0, 1, 2, -1, -1], [-1, -1, 3, 4, 5, -1, -1], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [-1, -1, 27, 28, 29, -1, -1], [-1, -1, 30, 31, 32, -1, -1]]

""" The game states that are just visited and stored in queue"""
visited = []

""" The game states already evaluated are stored in closed"""
closed = []

""" Reverse the path that is produced"""
reverse = []

""" Store the path from root to the goal state"""
path = []

""" Variable to store the initial time"""
time1 = 0


""" This class is used to create the path which is stored incrementally as the nodes are explored"""
class link:
    
    """ Initialize the data and the previous link"""
    def __init__(self, data, previous=None):
        self.data = map(list, data)
        self.previous = None
    
    """ Add the child to the previous link """   
    def addChild(self, node):
        self.children.append(node)
        
    """ Get the data from the node"""
    def getData(self):
        return self.data
    
    """ Set the previous link to the current node"""
    def setPrevious(self, previous):
        self.previous = previous
    
    """ Get the previous link to the current node"""
    def getPrevious(self):
        return self.previous

""" Store the current state in two nodes"""
node = link(a, None)
current = link(a, None)

""" The control starts here"""
def main():
    global time1
    time1 = time.time()
    node = heuristicSearch(a)
    if node == None:
        print 'There is no solution to this board'
    getPath(node)
    time2 = time.time()
    print 'The running time is :',time2 - time1
  
""" This method is to check if the state is a goal state or not"""
def goalReached(node):
    count = 0
    a = node.getData()
    for i in xrange(7):
        for j in xrange(7):
            if a[i][j] == 0 or a[i][j] == -1:
                count = count + 1
    if count == 48 and a[3][3] == 1:
        return True
    return False  

""" This method is responsible to generate the children for the particular state"""
def getAdjacentCells(a):
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

""" To count the number of nodes expanded   """ 
count = 0

""" Stores the initial state of the game"""
head = link(a, None)

""" Temporary variable to store the initial state"""
current = head

""" A* algorithm that is responsible to find the goal state"""
def heuristicSearch(a):
    global count
    print 'A* Algorithm Heuristic-2'
    global current
    heapq.heappush(visited, (getF(a, a), link(a, None)))
    while len(visited) != 0:
        f, node = heapq.heappop(visited)
        closed.append(node.getData())
        if goalReached(node):
            print 'There is a solution to this board'
            return node
        child = getAdjacentCells(node.getData())
        for x in xrange(len(child)):
            if child[x] not in closed:
                count = count + 1
                newNode = link(child[x], None)
                newNode.setPrevious(node) 
                heapq.heappush(visited, (getF(a, child[x]), newNode))
        
        
        
""" Calculate the function f(n) for a particular game state"""
def getF(a, currentNode):
    return getHeuristics(currentNode) + getG(a, currentNode)


""" Calculate the function g(n) for a particular game state"""
def getG(a, currentNode):
    sum1 = 0
    for i in xrange(7):
        for j in xrange(7):
            sum1 = sum1 + abs(a[i][j] - currentNode[i][j])
    return sum1

""" Calculate the heuristic for a particular game state. The heuristic is the distance of the pegs from the middle of the board. """
def getHeuristics(a):
    sum = 0
    for i in xrange(7):
        for j in xrange(7):
            if a[i][j] == 1:
                sum = sum + abs(3 - i)
    return sum

""" This method prints the final path to the goal state"""
def getPath(node):
    global compare
    stackReverse = []
    while node != None:
        stackReverse.append(node.getData())
        node = node.getPrevious()
        
    for k in reversed(stackReverse):
        reverse.append(k)
        
    for k in xrange(len(reverse)):
        if k >= 1:
            a1 = [[k - l for k, l in zip(i, j) ] for i, j in zip(reverse[k - 1], reverse[k])]
            logicPrint(a1)
    print ''
    print 'The number of nodes expanded', count+1


""" This method prints the expected format of the output path"""
def logicPrint(a):
    global ref
    for i in xrange(7):
        for j in xrange(7):
            if a[i][j] == -1:
                if j >= 2 and a[i][j - 2] == 1 and a[i][j - 1] == 1:
                    print '(', ref[i][j - 2] , '->' , ref[i][j], ')',
                if j + 2 < 7 and a[i][j + 2] == 1 and a[i][j + 1] == 1:
                    print '(', ref[i][j + 2], '->', ref[i][j], ')',
                if i >= 2 and a[i - 1][j] == 1 and a[i - 2][j] == 1:
                    print '(', ref[i - 2][j], '->', ref[i][j], ')',
                if i + 2 < 7 and a[i + 1][j] == 1 and a[i + 2][j] == 1:
                    print '(', ref[i + 2][j], '->', ref[i][j], ')',
                    

    
main()
