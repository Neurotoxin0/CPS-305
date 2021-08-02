import random

class Node(object):
    def __init__(self, v= None, p=None, l=None, r=None):
        self.value = v                                              # node's value
        self.parent = p                                             # its parent
        self.leftchild = l
        self.rightchild = r

    def hasLeftChild(self):                                         # will return its left child if have one and none for not
        return self.leftchild

    def haxRightChild(self):
        return self.rightchild

    def isLeftChild(self):                                          # determine if given node is a left / right child
        return self.parent and self.parent.leftchild==self

    def isRightChild(self):
        return self.parent and self.parent.rightchild==self


class BSTNode(object):
    def __init__(self):
        self.size = 0                                               # size of the tree; init = 0
        self.RootNode = None


    def insert(self, item):
        NewNode = Node(item)

        if not self.RootNode:                                       # if no root node: set current as root
            self.RootNode = NewNode
            self.size += 1

        else:
            tmp = self.RootNode                                     # current processing position
            finished = False

            while not finished:
                if item < tmp.value:
                    if tmp.leftchild:                               # if already have left child: restart with the left child
                        tmp = tmp.leftchild
                    else:                                           # if no left child: status = finished; set it as left child
                        tmp.leftchild = NewNode
                        NewNode.parent = tmp
                        self.size += 1
                        finished = True
                        break

                elif item > tmp.value:                              # same process but with the right child
                    if tmp.rightchild:
                        tmp = tmp.rightchild
                    else:
                        tmp.rightchild = NewNode
                        NewNode.parent = tmp
                        self.size += 1
                        finished = True
                        break
                else:                                               # no proper position & node already exist
                    finished = True
                    break


    def find(self, item):                                           # used to find / see if the node is in the tree
        if not self.RootNode:
            return None
        else:
            node = self.find_sub(self.RootNode, item)               # have to use a sub function to go through the tree; start with root
            if node:    return node
            else:       return None

    def find_sub(self, node, item):                                 # sub function for find function
        if not node:
            return None
        elif node.value == item:                                    # node found
            return node
        elif item < node.value:
            return self.find_sub(node.leftchild, item)
        elif item > node.value:
            return self.find_sub(node.rightchild, item)


    def remove(self, item):
        if self.size == 0:                                          # if no more node: time to stop; used only in demo in the last (line 223)
            print()

        elif self.size == 1:                                        # if only root, direct remove
            self.RootNode = None
            self.size = 0

        elif self.size > 1:                                         # if it's a tree: use sub function to consider scenerios
            tmp = self.find(item)
            if tmp:
                self.remove_sub(tmp)
                self.size -= 1

        else:
            print("Given value is not in the tree")

    def remove_sub_least(self, node):                               # sub function for sub function - remove_sub
        if node:                                                    # use to find the least node
            tmp = node
            while tmp.leftchild:
                tmp = tmp.leftchild
            return tmp

    def remove_sub(self, node):
        if (not node.leftchild) and (not node.rightchild):          # 1: if no child: direct remove
            if node.isLeftChild():
                node.parent.leftchild = None
            else:
                node.parent.rightchild = None

        elif node.leftchild and node.rightchild:                    # 2: have two children (easier than just one child)
            tmp = self.remove_sub_least(node.rightchild)            # use its the least child node to replace; use sub_sub function
            node.value = tmp.value
            self.remove_sub(tmp)

        else:                                                       # 3: have either left or right child or itself is root
            if node.hasLeftChild():
                if node.isLeftChild():                              # itself is a left child
                    node.leftchild.parent = node.parent
                    node.parent.leftchild = node.leftchild
                elif node.isRightChild():                           # itself is a right child
                    node.leftchild.parent = node.parent
                    node.parent.rightchild = node.leftchild
                else:                                               # special scenerio: node is root: use smaller child to replace
                    self.RootNode = node.leftchild
                    node.leftchild.parent = None
                    node.leftchild = None
            else:                                                   # have a right child; similar process
                if node.isLeftChild():
                    node.rightchild.parent = node.parent
                    node.parent.leftchild = node.rightchild
                elif node.isRightChild():
                    node.rightchild.parent = node.parent
                    node.parent.rightchild = node.rightchild
                else:
                    self.RootNode = node.rightchild
                    node.rightchild.parent = None
                    node.rightchild = None


    def Max(self):                                                  # find max node in current tree
        tmp = self.RootNode
        while tmp.rightchild:
            tmp = tmp.rightchild
        return tmp.value


    def Min(self):                                                  # find min node in current tree
        tmp = self.RootNode
        while tmp.leftchild:
            tmp = tmp.leftchild
        return tmp.value


    def Depth(self):                                                # find the depth of the tree
        tmp1 = self.RootNode
        maxdepth1 = 0
        tmp2 = self.RootNode
        maxdepth2 = 0

        while tmp1.leftchild:
            tmp1 = tmp1.leftchild
            maxdepth1 += 1
        while tmp2.rightchild:
            tmp2 = tmp2.rightchild
            maxdepth2 += 1

        if maxdepth1 > maxdepth2:   return maxdepth1
        else:                       return maxdepth2


    def inorder(self):
        self.inorder_sub(self.RootNode)
        print()

    def inorder_sub(self, node):
        if node:
            self.inorder_sub(node.leftchild)                        # first print the least node and print a slight bigger one
            print(node.value, end=" ")                              # after printed nodes that are smaller than root, print root
            self.inorder_sub(node.rightchild)                       # print nodes that are larger than root


    def traverse(self):                                             # print the tree with its size, max, min and nodes
        if self.size > 0:
            print('-------------------------')
            print("size of the tree: " + str(bst.size))
            print("Depth: " + str(self.Depth()))
            print("Maximun: " + str(self.Max()))
            print("Minimun: " + str(self.Min()))
            print("InOrder Traversal:")
            self.inorder()

        else:                                                       # when there is no node in tree: time to stop, rem not to use max / min function in case of error
            print("-------------------------")
            print("size of the tree: " + str(bst.size))
            print("InOrder Traversal:")
            self.inorder()

            print("end")




# Demo:
array = random.sample(range(1,100),20)
bst = BSTNode()

for i in array:
    bst.insert(i)
    bst.traverse()

print("\n----------------------------------------------Deletion Below:----------------------------------------------\n")

random.shuffle(array)                                               # disrupt array's sequence and go through each node
for node in array:                                                  # this will cover all scenarios:
    bst.remove(node)                                                    # node removed is a leaf
    bst.traverse()                                                      # node has one child
                                                                        # node has two children