import math, random, itertools
import graphRep
from graphRep import *
class Qagent:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [graph[0]]
        self.pathCost = 0
        self.epsilon = 1
        self.alpha = .9
        self.gamma = .9
        q_values = [[0 for i in range(len(graph) + 1)] for j in range(2 ** (len(graph)) + 1)]
        self.q_values = q_values

    def getQ(self):
        return self.q_values
    
    def getQvalue(self, state, action):
        return self.q_values[indexS(self.graph, state)][indexA(self.graph, (action))]

    def getNextState(self, action):
        l = self.visited
        l.append(action)
        return l

    def getReward(state, action):
        return (distance(state[-1], action))
    
    def getValue(self, state):
        actions = graphRep.possibleNextNodes(self.graph, state)
        if actions == []:
            return 0
        else:
            random.shuffle(actions)
            minVal = 100000
            bestAction = actions[0]
            for action in actions:
                curr = self.getQvalue(state, action)
                if curr <= minVal:
                    minVal = curr
                    bestAction = action
            
            return minVal

    def getPolicy(self, state):
        actions = graphRep.possibleNextNodes(self.graph, state)
        if actions == []:
            return []
        else:
            random.shuffle(actions)
            minVal = 100000
            bestAction = actions[0]
            for action in actions:
                curr = self.getQvalue(state, action)
                if curr <= minVal:
                    minVal = curr
                    bestAction = action
            return bestAction

    def getAction(self):
        rand = random.random()
        possibilities =  graphRep.possibleNextNodes(self.graph, self.visited)
        if possibilities == []:
            #print "no possible new nodes"
            return []
        else:
            if (rand <= self.epsilon):
                #print "taking random"
                return random.choice(possibilities)
            else:
                #print "taking best policy"
                return self.getPolicy(self.visited)
        
    
    def update(self, action):
        alpha = self.alpha
        nextState = self.getNextState(action)
        reward = graphRep.distance (self.visited[-1], action)
        self.q_values[indexS(self.graph, self.visited)][indexA(self.graph, (action))] = (1 - alpha) * self.q_values[indexS(self.graph, self.visited)][indexA(self.graph, (action))] + alpha * (reward + self.gamma * self.getValue(nextState))
        self.visited = nextState


def greedyGTSP(graph):
    visited = [graph[0]]
    unvisited = list(set(graph) - set(visited))
    while unvisited != []:
        visited.append(closest(visited[-1], unvisited, graph[0]))
        unvisited = list(set(graph) - set(visited))
    return visited + [graph[0]]
    
    

def closest(point, graph, init):
    minDist = 10000000
    if graph == []:
        return init
    else:
        closest = ()
        for i in range(len(graph)):
            if graphRep.distance(point, graph[i]) < minDist:
                minDist = graphRep.distance(point, graph[i])
                closest = graph[i]
        return closest
    
    
def main(graph, trialNos):
    myAgent = Qagent(graph)
    for i in range(trialNos):
        nextAction = True
        myAgent.visited = [graph[0]]
        myAgent.epsilon = 1 / math.sqrt(i + 1)
        while(nextAction != []):
            nextAction = myAgent.getAction()
            if(nextAction != []):
                myAgent.update(nextAction)
    return myAgent.visited, graphRep.pathCost(myAgent.visited)
     
def genRandomGraph(numPoints):
    l = list()
    for i in range(numPoints):
        x = random.randint(1,100)
        y = random.randint(1,100)
        l.append((x, y))
    return l
   
testGraph = genRandomGraph(10)
allPermutations = list(itertools.permutations(testGraph[1:]))
print "Starting Graph:", testGraph
for i in range(len(allPermutations)):
    allPermutations[i] = list(allPermutations[i])
    allPermutations[i] = [testGraph[0]] + allPermutations[i] + [testGraph[0]]
minDist = 10000000000
minPath = list()
for i in range(len(allPermutations)):
    if graphRep.pathCost(allPermutations[i]) < minDist:
        minDist = graphRep.pathCost(allPermutations[i])
        minPath = allPermutations[i]
print "Minimum path length:", minDist
print "Shortest path:", minPath
print "Greedy path length:", graphRep.pathCost(greedyGTSP(testGraph))
print "Greedy path:", greedyGTSP(testGraph)
print "after 1 trial:", (main(testGraph, 1))
print "after 10 trials:", (main(testGraph, 10))
print "after 100 trials:", (main(testGraph, 100))
print "after 200 trials:", (main(testGraph, 200))



