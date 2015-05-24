"""
 Author:     henry, henrylu518@gmail.com
 Date:       May 24, 2015
 Problem:    Clone Graph
 Difficulty: Easy
 Source:     http://oj.leetcode.com/problems/clone-graph/
 Notes:
 Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
 
 OJ's undirected graph serialization:
 Nodes are labeled from 0 to N - 1, where N is the total nodes in the graph.
 We use # as a separator for each node, and , as a separator for each neighbor of the node.
 As an example, consider the serialized graph {1,2#2#2}.
 The graph has a total of three nodes, and therefore contains three parts as separated by #.
 Connect node 0 to both nodes 1 and 2.
 Connect node 1 to node 2.
 Connect node 2 to node 2 (itself), thus forming a self-cycle.
 Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

 Solution:  BFS.  
            DFS. just change pop(0) to pop()
            
            Solution 2 is wrong. Although this Solution could pass the test, and accepted,
            but it's still wrong. 
            For example, [4,4], the 4 should be the same node
            and here, it's different node, just have the same value.
 """

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
#     def __str__(self):
#         return str(self.label)
#     def __repr__(self):
#         return str(self)  


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        if node == None: return None
        startNode = UndirectedGraphNode(node.label)
        oldGraphQueue, newGraphQueue = [node], [startNode]
        explored = set()
        nodes = {}
        while oldGraphQueue:
            oldNode, current = oldGraphQueue.pop(0), newGraphQueue.pop(0)
            if oldNode not in explored:
                explored.add(oldNode)
                for n in oldNode.neighbors:
                    oldGraphQueue.append(n)
                    newNode = nodes.get(n.label, UndirectedGraphNode(n.label))
                    nodes[n.label] = newNode
                    current.neighbors.append(newNode)
                    newGraphQueue.append(newNode)
        return startNode

    def cloneGraph_Wrong(self, node):
        """
            Although this Solution could pass the test, and accepted,
            but it's still wrong. 
            For example, [4,4], the 4 should be the same node
            and here, it's different node, just have the same value.
        """
        if node == None: return None
        startNode = UndirectedGraphNode(node.label)
        oldGraphQueue, newGraphQueue = [node], [startNode]
        explored = set()
        while oldGraphQueue:
            oldNode, current = oldGraphQueue.pop(0), newGraphQueue.pop(0)
            if oldNode not in explored:
                explored.add(oldNode)
                for n in oldNode.neighbors:
                    oldGraphQueue.append(n)
                    newNode = UndirectedGraphNode(n.label)
                    current.neighbors.append(newNode)
                    newGraphQueue.append(newNode)
        return startNode