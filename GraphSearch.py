# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:46:15 2019

@author: spencer.stewart
"""

from boltons.queueutils import PriorityQueue
from boltons.queueutils import SortedPriorityQueue
from collections import defaultdict

def previsit(v):
    print("Visiting: %s" % v)


def postvisit(v):
    print("done Visiting: %s" % v)


def depthFirstSearch(passedAdjacencyList, startNode, targetNode):

    """

    :param passedAdjacencyList: This is an adjacency list that represents
    a graph.
    :param startNode: what node we are starting on.
    :param targetNode: what node we want to find
    :return: We will return a list of nodes indicating
    the path from the startIndex to the targetIndex
    or if that doesn't exist, we will return that there is non.
    
    
    q = PriorityQueue()
    clock = 0
    q.push(s, priority = 0)
    
    parent = {}
    cost = {}
    
    while q is not empty:
        
        p = q.pop()
        
        if p == destination then return path (p, parents)
        
        for b in g[p]:
                
            if parent[b] = p
            cost[b] = cost[p] + weight(p,b)
            q.path(b, priority = -clock++)

    https://stackoverflow.com/questions/12864004/tracing-and-returning-a-path-in-depth-first-search
    """

    nodePath = PriorityQueue()

    clock = 0
    nodePath.add(startNode, clock)

    parent = []

    parentMap = []

    isVisited = []

    print("Starting the next depthFirstSearch")

    while len(nodePath) != 0:

        print("Start of while loop")
        #print(printOutNodePath(nodePath))

        p = nodePath.pop()
        print("This is p right after we pop", p.getNodeIndex())
        print("This is our parent", parentMap)

        print("p is currently", p.getNodeIndex())

        curr = targetNode

        if p == targetNode:
            while(p != None):
                print("We are returning target node")

                parent.append(p)
                p = parentMap[curr]

            return parent


        for b in passedAdjacencyList[p.getNodeIndex()]:

            if b.isVisited == False:
                print("b is currently", b.getNodeIndex())
                clock = clock + 1
                nodePath.add(b, clock)
                parentMap[b.getNodeIndex()] = p

                print("We are peeking:", nodePath.peek().getNodeIndex())
                print("passing into the printout", b.getNodeIndex())
                #printOutNodePath(nodePath)

        print("")


    return parent

def printOutNodePath(nodePath2):

    print("")
    print("Start printing out")
    for b in range(len(nodePath2)):
        print("Printing out nodePath:", nodePath2.peek().getNodeIndex())

    print("Stop printing out")
    print("")


##############################################################
#                            Tests                           #
##############################################################


def test_DepthFirstSearch():

    adjacencyList1 = defaultdict(list)

    adjacencyList1[0].extend([1, 4])
    adjacencyList1[1].extend([3])
    adjacencyList1[2].extend([5])
    adjacencyList1[3].extend([])
    adjacencyList1[4].extend([6, 7])
    adjacencyList1[5].extend([1])
    adjacencyList1[6].extend([0])
    adjacencyList1[7].extend([2])

    assert depthFirstSearch(adjacencyList1, 0, 5) == [0,4,7,2,5]
    assert depthFirstSearch(adjacencyList1, 4, 5) == [4,7,2,5]
    assert depthFirstSearch(adjacencyList1, 6, 3) == [6, 0, 1, 3]


def test_PriorityQueueExperimentation():

    pQueue = PriorityQueue()

    pQueue.add(6)
    pQueue.add(5)
    pQueue.add(3)
    pQueue.add(7)
    pQueue.add(8)

    assert pQueue.pop() == 6
    assert pQueue.pop() == 5
    assert pQueue.pop() == 3

    pQueue = PriorityQueue()

    pQueue.add(1,1)
    pQueue.add(4,2)

    assert pQueue.pop() == 4
    assert pQueue.pop() == 1



def test_SortedPriorityQueueExperimentation():

    sPQ = SortedPriorityQueue()

    sPQ.add(6,6)
    sPQ.add(5,5)
    sPQ.add(3,3)
    sPQ.add(7,7)
    sPQ.add(8,8)

    assert sPQ.pop() == 8
    assert sPQ.pop() == 7
    assert sPQ.pop() == 6










