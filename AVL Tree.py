'''Code advanced from file Binary_Search_Tree.py'''

import random

class Node(object):
    def __init__(self, value):
        '''unnecessary functions/ values removed'''
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.height = 0                                                                     # height of th node in the tree


class AVLTree(object):
    def __init__(self):
        self.RootNode = None


    def height(self, node):                                                                 # if find node, return height
        if node is None:
            return -1
        else:
            return node.height


    def find(self, value):                                                                  # used to find / see if the node is in the tree
        if not self.RootNode:
            return None
        else:
            return self.find_sub(value, self.RootNode)                                      # have to use a sub function to go through the tree; start with root

    def find_sub(self, value, node):                                                        # sub function for find function
        if node is None:
            return None
        elif value < node.value:
            return self.find_sub(value, self.leftchild)
        elif value > node.value:
            return self.find_sub(value, self.rightchild)
        else:
            return node


    def Max(self):                                                                          # find max node in current tree
        if not self.RootNode:
            return None
        else:
            return self.Max_sub(self.RootNode)

    def Max_sub(self, node):                                                                # sub: used to find max child of given node
        if node.rightchild:                                                                 # if use with Max(): find the max of the tree
            return self.Max_sub(node.rightchild)
        else:
            return node


    def Min(self):                                                                          # find min node in current tree
        if not self.RootNode:
            return None
        else:
            return self.Min_sub(self.RootNode)

    def Min_sub(self, node):
        if node.leftchild:
            return self.Min_sub(node.leftchild)
        else:
            return node


    '''Four routine methods below: '''                                                      # Lab 7 part 2 content: routine
    def singleLeftRotate(self, node):
        tmp = node.leftchild
        node.leftchild = tmp.rightchild
        tmp.rightchild = node

        node.height = max(self.height(node.rightchild), self.height(node.leftchild)) + 1    # update height to switched nodes
        tmp.height = max(self.height(tmp.leftchild), node.height) + 1

        return tmp

    def singleRightRotate(self, node):
        tmp = node.rightchild
        node.rightchild = tmp.leftchild
        tmp.leftchild = node

        node.height = max(self.height(node.rightchild), self.height(node.leftchild)) + 1
        tmp.height = max(self.height(tmp.rightchild), node.height) + 1

        return tmp

    def doubleLeftchildRotate(self, node):
        node.leftchild = self.singleRightRotate(node.leftchild)
        return self.singleLeftRotate(node)

    def doubleRightchildRotate(self, node):
        node.rightchild = self.singleLeftRotate(node.rightchild)
        return self.singleRightRotate(node)


    def insert(self, value):
        if not self.RootNode:
            self.RootNode = Node(value)
        else:
            self.RootNode = self.insert_sub(value, self.RootNode)

    def insert_sub(self, value, node):
        if node is None:                                                                    # new added: if node not found in the tree, create a new node in Node();
            node = Node(value)                                                              # prevent case: if already a node named A in Node(), add another node 'A' wil casue bug; back in Lab6

        elif value < node.value:                                                            # if smaller than the current processing node: restart with the left child
            node.leftchild = self.insert_sub(value, node.leftchild)                         # will go deeper until find a proper position

            if (self.height(node.leftchild) - self.height(node.rightchild)) == 2:           # after added: if not balanced
                if value < node.leftchild.value:
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftchildRotate(node)

        elif value > node.value:                                                            # if larger than the current processing node: restart with the right child
            node.rightchild = self.insert_sub(value, node.rightchild)

            if (self.height(node.rightchild) - self.height(node.leftchild)) == 2:
                if value < node.rightchild.value:
                    node = self.doubleRightchildRotate(node)
                else:
                    node = self.singleRightRotate(node)

        node.height = max(self.height(node.rightchild), self.height(node.leftchild)) + 1    # caculate the new node's height
        return node

    def remove(self, value):
        self.RootNode = self.remove_sub(value, self.RootNode)

    def remove_sub(self, value, node):
        if node is None:
            print("node not found in the tree")                                             # given value is not in the tree
            return

        elif value < node.value:
            node.leftchild = self.remove_sub(value, node.leftchild)                         # search left child and its child

            if (self.height(node.rightchild) - self.height(node.leftchild)) == 2:           # not balanced after delete
                if self.height(node.rightchild.rightchild) >= self.height(node.rightchild.leftchild):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightchildRotate(node)

            node.height = max(self.height(node.leftchild), self.height(node.rightchild)) + 1

        elif value > node.value:                                                            # search right child and its child
            node.rightchild = self.remove_sub(value, node.rightchild)

            if (self.height(node.leftchild) - self.height(node.rightchild)) == 2:
                if self.height(node.leftchild.leftchild) >= self.height(node.leftchild.rightchild):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftchildRotate(node)

            node.height = max(self.height(node.leftchild), self.height(node.rightchild)) + 1

        # node found:
        elif node.leftchild and node.rightchild:                                            # if found: if deleting node have both left and right child
            if node.leftchild.height <= node.rightchild.height:
                minNode = self.Min_sub(node.rightchild)
                node.value = minNode.value
                node.rightchild = self.remove_sub(node.value, node.rightchild)
            else:
                maxNode = self.Max_sub(node.leftchild)
                node.value = maxNode.value
                node.leftchild = self.remove_sub(node.value, node.leftchild)
            node.height = max(self.height(node.leftchild), self.height(node.rightchild)) + 1

        else:
            if node.rightchild:                                                             # if have only right child
                node = node.rightchild
            else:                                                                           # if have only left child
                node = node.leftchild

        return node


    def inorder(self, node):
        if node:
            self.inorder(node.leftchild)                                                    # first print the least node and print a slight bigger one
            print(node.value, end=" ")                                                      # after printed nodes that are smaller than RootNode, print RootNode
            self.inorder(node.rightchild)                                                   # print nodes that are larger than RootNode


    def traverse(self):                                                                     # print the tree
        print('-------------------------')
        print("InOrder Traversal:")
        self.inorder(self.RootNode)
        print()


# Demo:
array = random.sample(range(1, 100), 20)
bst = AVLTree()

for i in array:
    bst.insert(i)
    bst.traverse()

print("\n----------------------------------------------Deletion Below:----------------------------------------------\n")

random.shuffle(array)                                                                       # disrupt array's sequence and go through each node
for node in array:
    bst.remove(node)
    bst.traverse()