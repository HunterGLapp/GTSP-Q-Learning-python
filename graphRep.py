import math

def distance((x1, y1), (x2, y2)):
    return math.sqrt((x1 - x2) ** 2 + (y2 - y1) **2)

def possibleNextNodes (graph, visited):
    g = len(graph)
    v = len(visited)
    if v == g:
        return [graph[0]]
    if v > g:
        return []
    if v < g:
        return list (set(graph) - set(visited))

def pathCost(path):
    totalCost = 0
    for i in range(len(path) - 1):
        totalCost += distance(path[i], path[i + 1])
    return totalCost

def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def indexS(graph, state):
    ps =sorted([sorted(x) for x in powerset(graph)])
    stateSet = sorted(state)
    l = list(graph)
    l.append(graph[0])
    if stateSet == sorted(l):
        return len(graph) 
    else:
        return ps.index(stateSet)

def indexA(graph, action):
    return graph.index(action)



    
