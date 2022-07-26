# WoflowInterviewQuestions
Repo to for Woflow Interivew 

Answers: 
> 1. What is the total number of unique nodes?

  **30**

> 2. Which node ID is shared the most among all other nodes?

  **a06c90bf-e635-4812-992e-f7b1e2408a3f**

# Solution 
The crux of this problem is understanding how to do graph/tree traversals as well and some basic network request formating and response handling.

This solution is an iterative Depth First Search (DFS) trace algorithm that visits each node, adds it to a unique list, and then adds its children to a stack of nodes to be explored. Due to the nature of the questions, it is required to vist all nodes, at least once to make sure we can an accurate count and whole picture of the graph. 

# Limitations and Potential Optimizations

1) It is slow due to processing each node 1 at a time - no multithreading is used when exploring children. Due to the slow nature of making and recieving froma remote place, this is where processing time could best be reduced. 
2) It naively traces each node no matter what. This could be optimized in some way by marking nodes with no children, or nodes that have already been visited, 



