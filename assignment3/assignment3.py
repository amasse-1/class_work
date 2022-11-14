"""
Class: CSC6013 - Discrete Structures and Algorithms

Assignment: Programming Assignment 3

Author: Anthony Masse

Created: 11/7/2022

Updated: 11/7/2022 
"""
from binSearchTree import Tree
from string import ascii_uppercase



class assignment3:
    
    def __init__(self, file):
        
        self.verticies = [] # list of verticies
        self.graph = [] # graph data structure
        self.file = file #file
        numbers = open(self.file, 'r') 
        tree = Tree() # tree object
        count = 0 #count of numbers being inserted into tree
        for line in numbers:
            tree.insert(int(line)) # insert into tree
            count += 1
        #close the file
        numbers.close()

        print("Tree (Preorder):\n-------------------")
        tree.printPreorder() #prints tree in preorder

        self.add_vertex(tree.Root, count) # adds the root uses recursion to go down the tree
        self.add_edge(tree.Root, self.graph) # adds the connection between the verticies
        
        print("\nTree as a Graph:\n-------------------")
        self.printGraph(self.graph) #preints the graph



    def add_vertex(self, node, count):
        if(node != None):
            self.verticies.append(node.Data) # adds the data to a list of verticies

            row = [] #an empty row
            while(len(row) != count):
                row.append(0) #fills rows with zeros
            self.graph.append(row) #adds rows to the graphs
        if(node.Left != None):
            self.add_vertex(node.Left, count) #recursion to left
        if(node.Right != None):
            self.add_vertex(node.Right, count) #recursion to the right

    def printGraph(self, graph):
        for i in graph:
            print(f'{i}\n') #prints each row

    def add_edge(self, node, graph):
        if(node != None and node.Left != None):
            weight = abs(node.Data - node.Left.Data) # absolute value of the weight
            index1 = self.verticies.index(node.Data) #gets the index of the vertex
            index2 = self.verticies.index(node.Left.Data) #gets the index of the vertex
            graph[index1][index2] = weight #adds the weight
            self.add_edge(node.Left, graph) 
        if(node != None and node.Right != None):
            weight = abs(node.Data - node.Right.Data)# absolute value of the weight
            index1 = self.verticies.index(node.Data) #gets the index of the vertex
            index2 = self.verticies.index(node.Right.Data) #gets the index of the vertex
            graph[index1][index2] = weight #adds the weight
        if(node.Left != None):
            self.add_edge(node.Left, graph) #recursion for left
        if(node.Right != None):
            self.add_edge(node.Right, graph) # recursion for right
        
""" 
The reason each method starts with the node, then the left, then the right is because 
that is the order that for preorder: Node, Left, Right. 
"""


if __name__ == '__main__':
    assignment3('numbers.txt')
