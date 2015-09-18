# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        """
        Return the maximum score for the pacman to succeed
        Parameters to consider :
        1. Nearest distance of pacman from the ghost
        2. Inverse the distance of the nearest food to the pacman
        3. Number of food pellets left in the game
        4. Maximum scared time
        """
        """First find the nearest distance of pacman from the ghost"""
        
        minGhostDist = 0
        totalMaxScore = 0
        for ghostDist in newGhostStates:
            gd = util.manhattanDistance(ghostDist.getPosition(), newPos)
            if gd <= 2:
                minGhostDist = gd
                """ Providing heavy penalty to the game when the minimum distance of the ghost reaches within 2 so as to escape from the ghost"""
                totalMaxScore = -500000
        
        ghostScore = minGhostDist
        
        """ Now calculate the distance of nearest food from pacman"""
        food = newFood.asList()
        """ Taking the maximum possible value which cannot exist for the nearest food"""
        nearestFood = 500
        fd = 0
        for f in xrange(len(food)):
            fd = util.manhattanDistance(food[f], newPos)
            if fd <= nearestFood:
                nearestFood = fd
        if fd==0:
            nearestFood = 1
        """Calculating the food score by inversing the distance to the nearest food inorder to provide the importance for the nearest food"""
        foodScore = 1.0/ (nearestFood * 10)
        
        """calculating the number of food pellets for the pacman to eat"""
        food = newFood.asList()
        foodPelletScore = len(food)
        
        
        """Calculating the maximum scared time of the ghosts"""
        maxGhostScared = newGhostStates[0].scaredTimer
        for x in newGhostStates:
            gs = x.scaredTimer
            if gs >= minGhostDist:
                maxGhostScared = gs
        """Adding up the score from the scared ghost as the ghost can be eaten and the pacman can move freely"""
        maxScaredTimeScore = maxGhostScared
        
        """Total score that is sent from the evaluation function that sums up the possible bonus and penalties"""
        totalMaxScore = totalMaxScore + ghostScore + foodScore + foodPelletScore + maxScaredTimeScore
        
        """Heavy penalty is given to the pacman so as to prevent it from stopping during the game"""
        if action == "Stop":
            totalMaxScore = -1000000
            
        return successorGameState.getScore() + totalMaxScore

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """
    

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        
        """Calling the minimax method"""
        action,requiredValue = self.miniMax(gameState,0,gameState.getNumAgents()*self.depth,True)
        
        """Returning the required action to be taken"""
        return action
          
          
    """MiniMax Algorithm
    1. GameState - this is the state provided to calculate the various factors of the game
    2. agentNumber - this stores the total number of agents in the game
    3. depth - this is the total depth for the game given at runtime
    4. switchPlayer - this is used to switch between pacman and ghost
    5. action - stores the possible action for each state
    """
    def miniMax(self,gameState, agentNumber, depth, switchPlayer,action=Directions.STOP):
        agent = (agentNumber)%gameState.getNumAgents()
        if agent==0:
            switchPlayer = True
            
        """This code returns when the depth reached is zero or the game has ended or won"""
        if gameState.isLose() or gameState.isWin() or depth == 0:
            return action,self.evaluationFunction(gameState)
        
        """First part of the code is for the pacman and second part of the code is for the ghost"""
        if switchPlayer:
            legalMoves  = gameState.getLegalActions(0)
            requiredValue = float("-inf")
            
            """Remove the STOP direction to speed up the pacman movements : Hint taken from the question"""
            if Directions.STOP in legalMoves:
                legalMoves.remove(Directions.STOP)
            requiredAction = Directions.STOP
            
            """Calculating the possible moves for the pacman state"""
            for localAction in legalMoves:
                fl,value = self.miniMax(gameState.generateSuccessor((agentNumber)%gameState.getNumAgents(),localAction),(agentNumber+1)%gameState.getNumAgents(),depth-1,False,localAction)
                if value >= requiredValue:
                    requiredValue = value
                    requiredAction = localAction
            return requiredAction,requiredValue
        else:
            legalMoves  = gameState.getLegalActions((agentNumber)%gameState.getNumAgents())
            requiredValue = float("inf")
            
            """Remove the STOP direction to speed up the ghost movements : Hint taken from the question"""
            if Directions.STOP in legalMoves:
                legalMoves.remove(Directions.STOP)
            requiredAction = Directions.STOP
            
            """Calculating the possible moves for the ghost state"""
            for localAction in legalMoves:
                fl,value = self.miniMax(gameState.generateSuccessor((agentNumber)%gameState.getNumAgents(),localAction),(agentNumber+1)%gameState.getNumAgents(),depth-1,False,localAction)
                if value <=requiredValue:
                    requiredValue = value
                    requiredAction = localAction
            return requiredAction,requiredValue
        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        
        """Calling the aplhaBetaPruning method"""
        action,requiredValue = self.aplhaBetaPruning(gameState,0,gameState.getNumAgents()*self.depth,True,float("-inf"),float("inf"))
        """Returning the required action to be taken"""
        return action
          
          
    """alphaBetaPruning Algorithm
    1. GameState - this is the state provided to calculate the various factors of the game
    2. agentNumber - this stores the total number of agents in the game
    3. depth - this is the total depth for the game given at runtime
    4. switchPlayer - this is used to switch between pacman and ghost
    5. alpha - this value is taken by the pacman to compare the existing value with the new value
    6. beta - this value is taken by the ghosts to compare the existing value with the new value
    7. action - stores the possible action for each state
    """
    def aplhaBetaPruning(self,gameState, agentNumber, depth, switchPlayer,alpha,beta,action=Directions.STOP):
        agent = (agentNumber)%gameState.getNumAgents()
        if agent==0:
            switchPlayer = True
            
        """This code returns when the depth reached is zero or the game has ended or won"""
        if gameState.isLose() or gameState.isWin() or depth == 0:
            return action,self.evaluationFunction(gameState)
        
        """First part of the code is for the pacman and second part of the code is for the ghost"""
        if switchPlayer:
            legalMoves  = gameState.getLegalActions(0)
            requiredValue = float("-inf")
            
            """Remove the STOP direction to speed up the pacman movements : Hint taken from the question"""
            if Directions.STOP in legalMoves:
                legalMoves.remove(Directions.STOP)
            requiredAction = Directions.STOP
            
            """Calculating the possible moves for the pacman state"""
            for localAction in legalMoves:
                fl,value = self.aplhaBetaPruning(gameState.generateSuccessor((agentNumber)%gameState.getNumAgents(),localAction),(agentNumber+1)%gameState.getNumAgents(),depth-1,False,alpha,beta,localAction)
                if value >= requiredValue:
                    requiredValue = value
                    requiredAction = localAction
                if value > alpha:
                    alpha = requiredValue
                    
                """pruning the tree when the alpha value is greater than the beta value"""
                if beta < alpha:
                    break
            return requiredAction,requiredValue
        else:
            legalMoves  = gameState.getLegalActions((agentNumber)%gameState.getNumAgents())
            requiredValue = float("inf")
            
            """Remove the STOP direction to speed up the pacman movements : Hint taken from the question"""
            if Directions.STOP in legalMoves:
                legalMoves.remove(Directions.STOP)
            requiredAction = Directions.STOP
            
            """Calculating the possible moves for the ghost state"""
            for localAction in legalMoves:
                fl,value = self.aplhaBetaPruning(gameState.generateSuccessor((agentNumber)%gameState.getNumAgents(),localAction),(agentNumber+1)%gameState.getNumAgents(),depth-1,False,alpha,beta,localAction)
                if value <=requiredValue:
                    requiredValue = value
                    requiredAction = localAction
                if value < beta:
                    beta = requiredValue
                    
                """pruning the tree when the alpha value is greater than the beta value"""
                if beta < alpha:
                    break
            return requiredAction,requiredValue

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

