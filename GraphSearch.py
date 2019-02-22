# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:46:15 2019

@author: spencer.stewart
"""

from boltons.queueutils import PriorityQueue
from boltons.queueutils import SortedPriorityQueue
from collections import defaultdict


class Node:

    def __init__(self, number):
        self._nodeIndex = number


    def getNodeIndex(self):
        return self._nodeIndex

    _nodeIndex = 0
    _preClock = 0
    _postClock = 0

    isVisited = False



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

    """

    nodePath = PriorityQueue()

    nodePath.add(startNode)

    print("Starting the next depthFirstSearch MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

    previsit(startNode.getNodeIndex())

    for nextNode in passedAdjacencyList[startNode.getNodeIndex()]:

        print("This is the next node:", nextNode.getNodeIndex())

        startNode.isVisited = True;
        nodePath = Explore(nextNode, passedAdjacencyList, nodePath, targetNode)

    print("After the search")

    nodePathList = []



    for eachNode in range(len(nodePath)):
        print("This is the value:", nodePath.peek())
        nodePathList = nodePathList + [nodePath.pop().getNodeIndex()]


    postvisit(startNode.getNodeIndex())

    return nodePathList



def Explore(currentNode, passedAdjacencyList, nodePath, targetNode):

    previsit(currentNode.getNodeIndex())


    if currentNode == targetNode:
        nodePath.add(targetNode)
        return nodePath

    currentNode.isVisited = True

    #print("Next Node,", passedAdjacencyList[currentNode.getNodeIndex()])

    for nextNode in passedAdjacencyList[currentNode.getNodeIndex()]:

        if not nextNode.isVisited == True:


            nodePath = Explore(nextNode, passedAdjacencyList, nodePath, targetNode)


    nodePath.add(currentNode)

    postvisit(currentNode.getNodeIndex())

    return nodePath





##############################################################
#                            Tests                           #
##############################################################


def test_DepthFirstSearch():

    adjacencyList1 = defaultdict(list)

    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    assert node0.getNodeIndex() == 0
    assert node1.getNodeIndex() == 1
    assert node2.getNodeIndex() == 2
    assert node3.getNodeIndex() == 3
    assert node4.getNodeIndex() == 4
    assert node5.getNodeIndex() == 5
    assert node6.getNodeIndex() == 6
    assert node7.getNodeIndex() == 7

    adjacencyList1[0].extend([node1, node4])
    adjacencyList1[1].extend([node3])
    adjacencyList1[2].extend([node5])
    adjacencyList1[3].extend([])
    adjacencyList1[4].extend([node6, node7])
    adjacencyList1[5].extend([node1])
    adjacencyList1[6].extend([node0])
    adjacencyList1[7].extend([node2])

    assert adjacencyList1[0][0].getNodeIndex() == node1.getNodeIndex()
    assert adjacencyList1[0][1].getNodeIndex() == node4.getNodeIndex()
    assert adjacencyList1[7][0].getNodeIndex() == node2.getNodeIndex()

    assert depthFirstSearch(adjacencyList1, node0, node5) == [0,4,7,2,5]


def test_NodeClassNodeIndexWorks():

    node1 = Node(1)

    assert node1.getNodeIndex() == 1


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










